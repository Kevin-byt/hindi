from googletrans import Translator, LANGUAGES
import requests
from bs4 import BeautifulSoup
import random

# user_agents_list = [
#     'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
#     'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
# ]

# # URL of the webpage to scrape
# # URL = "https://realpython.github.io/fake-jobs/"
# URL = "https://www.classcentral.com"
# # URL = "https://www.imdb.com/"

# # Make a GET request to the webpage
# page = requests.get(URL,headers={'User-Agent': random.choice(user_agents_list)})

# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(page.content, 'html.parser')

# # Get the text content of the webpage
# text = soup.get_text()

# # Create an instance of the Translator class
# translator = Translator()

# # Detect the language of the text
# detected_lang = translator.detect(text).lang

# # Translate the text to Hindi
# if detected_lang != 'hi':
#     hindi_text = translator.translate(text, src=detected_lang, dest='hi').text
# else:
#     hindi_text = text

# #Write the page contents to a html file
# # with open('trans/index.html','w') as file:
# #     file.write(hindi_text)

# with open('trans/index.html', 'w', encoding='utf-8') as f:
#     f.write('<html>\n<head>\n<meta charset="utf-8">\n<title>Python (प्रोग्रामिंग भाषा)</title>\n</head>\n<body>\n')
#     f.write(hindi_text)
#     f.write('\n</body>\n</html>')

# # # Initialize the Translator object
# # translator = Translator()

# # # Define the input text to translate
# # text = 'Hello, world!'

# # # Check if the input text is valid
# # if text and text.strip():
# #     # Detect the language of the input text
# #     detected_lang = translator.detect(text).lang

# #     # Translate the text to Hindi
# #     if detected_lang != 'hi':
# #         hindi_text = translator.translate(text, src=detected_lang, dest='hi').text
# #     else:
# #         hindi_text = text

# #     # Print the translated text
# #     print(hindi_text)
# # else:
# #     print("Input text is not valid.")

from googletrans import Translator
import requests
from bs4 import BeautifulSoup

# Set the URL of the webpage to translate
url = "https://en.wikipedia.org/wiki/Main_Page"

# Send a GET request to the URL and store the response in a variable
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the text content in the HTML using the "find_all" method
text_content = soup.find_all(text=True)

# Join the text content into a single string with newlines between each piece of content
text = "\n".join(text_content)

# Initialize the translator
translator = Translator()

# Translate the text to Hindi
translation = translator.translate(text, dest="hi")

# Create a new HTML file with the translated content
with open('trans/translated.html', 'w', encoding="utf-8") as f:
    f.write(translation.text)

