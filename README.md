# Streamlit SEO Checker

Streamlit SEO Analyzer is a simple web application built using [Streamlit](https://streamlit.io/) that allows you to analyze the SEO attributes of a web page. It fetches the content of a given URL and provides insights into its metadata, headings, images without alt attributes, keyword frequencies, and bigrams.

## Features

- Check if title and description meta tags are present.
- Identify headings (h1 to h6) and check for the presence of an h1 tag.
- List images without alt attributes.
- Display the most common keywords and bigrams (i.e., two-word phrase) found in the page content.

## Installation

1. Clone this repository:

- git clone https://github.com/your-username/Streamlit-SEO-Analyzer.git
- cd Streamlit-SEO-Analyzer

2. Create a virtual environment (optional but recommended)*
- conda create -n myseo python=3.10
- conda activate myseo

3. Install the required packages:
- pip install -r requirements.txt

## Usage
- Run the Streamlit app:
- streamlit run seoChecker.py
- Enter the URL of the web page you want to analyze in the text input field and click the "Analyze" button.
- The app will provide insights into the SEO attributes of the web page, including metadata, headings, images, keywords, and bigrams.


## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.


## License
This project is licensed under the MIT License.


## Acknowledgements
This app was inspired by the need to quickly analyze the SEO attributes of web pages.
Built using the Streamlit framework.
Utilizes the requests library for HTTP requests and the BeautifulSoup library for HTML parsing.
Keyword and bigram extraction with NLTK.

## Reference
https://www.youtube.com/watch?v=SpAmkP1nqdo

