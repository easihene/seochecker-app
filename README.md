# SEO Checker

SEO Checker is a simple web application built using [Streamlit](https://streamlit.io/) that allows you to analyze the SEO attributes of a web page. It fetches the content of a given URL and provides insights into its metadata, headings, images without alt attributes, keyword frequencies, and bigrams (i.e., two-word phrases).


## Features

- Check if the title and description meta tags are present.
- Identify headings (h1 to h6) and check for the presence of an h1 tag.
- List images without alt attributes.
- Display the most common keywords and bigrams found in the page content.


## Installation

1. Clone this repository:

- git clone [https://github.com/your-username/Streamlit-SEO-Analyzer.git](https://github.com/easihene/seochecker-app.git)
- cd Streamlit-SEO-Analyzer

2. Create a virtual environment (optional but recommended)*
- conda create -n myseo python=3.10
- conda activate myseo

3. Install the required packages:
- pip install -r requirements.txt


## Usage
- Run the Streamlit app:
- streamlit run seoChecker.py
- Enter the web page URL you want to analyze in the text input field (e.g., https://www.ewanalytics.com/) and click the "Check" button.


## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


## License
This project is licensed under the MIT License.


## Acknowledgements
- This app was inspired by the need to analyze the SEO attributes of web pages quickly.
- Built using the Streamlit framework.
- Utilizes the requests library for HTTP requests and the BeautifulSoup library for HTML parsing.
- Keyword and bigram extraction with NLTK.


## Reference
https://www.youtube.com/watch?v=SpAmkP1nqdo

