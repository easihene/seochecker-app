import streamlit as st
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
nltk.download('stopwords')
nltk.download('punkt')

# Function to get HTML content from a URL


def get_html_content(url):

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        st.error(f"Error: Unable to access the website - {e}")
        return None


def extract_metadata(soup):
    title = soup.find('title')
    description = soup.find('meta', attrs={'name': 'description'})
    return title, description


def extract_headings(soup):
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    return headings

# Function to extract images without alt attribute from a soup object
def extract_images_without_alt(soup):
    images_without_alt = soup.find_all('img', alt='')
    return images_without_alt

# Function to extract keywords and bigrams from a text
def extract_keywords_and_bigrams(text):
    words = [i.lower() for i in word_tokenize(text)]
    sw = nltk.corpus.stopwords.words('english')
    new_words = [word for word in words if word not in sw and word.isalpha()]

    bi_grams = ngrams(new_words, 2)
    freq_bigrams = nltk.FreqDist(bi_grams)
    bi_grams_freq = freq_bigrams.most_common(10)

    freq = nltk.FreqDist(new_words)
    keywords = freq.most_common(10)

    return keywords, bi_grams_freq

# Main Streamlit app
st.title('SEO CHECKER')
url = st.text_input('Enter URL')

if st.button('Check'):
    html_content = get_html_content(url)

    if html_content is not None:
        soup = BeautifulSoup(html_content, 'html.parser')
        title, description = extract_metadata(soup)
        headings = extract_headings(soup)
        images_without_alt = extract_images_without_alt(soup)

        good = []
        bad = []

        if title:
            good.append("Title Exists! Great!")
        else:
            bad.append("Title does not exist! Add a Title")

        if description:
            good.append("Description Exists! Great!")
        else:
            bad.append("Description does not exist! Add a Meta Description")

        h_tags = [h.name for h in headings]
        if 'h1' not in h_tags:
            bad.append("No H1 found!")

        for img in images_without_alt:
            bad.append(f"No Alt: {img}")

        body_text = soup.find('body').text
        keywords, bi_grams_freq = extract_keywords_and_bigrams(body_text)

        # Print the results using Streamlit tabs
        tab1, tab2, tab3, tab4 = st.tabs(
            ['Keywords', 'BiGrams', 'Good', 'Bad'])

        with tab1:
            for i in keywords:
                st.text(i)
        with tab2:
            for i in bi_grams_freq:
                st.text(i)
        with tab3:
            for i in good:
                st.success(i)
        with tab4:
            for i in bad:
                st.error(i)
