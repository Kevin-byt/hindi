import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# URL of the webpage to scrape
url = 'https://www.medium.com/'

# Make a GET request to the webpage
response = requests.get(url)
print(f'Response is {response}')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Get the text content of the webpage
text = soup.get_text()
print(f'Text is {text}')

# Create an instance of the Translator class
translator = Translator()

