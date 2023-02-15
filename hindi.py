import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# URL of the webpage to scrape
url = 'https://www.medium.com/'

# Make a GET request to the webpage
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Get the text content of the webpage
text = soup.get_text()

# Create an instance of the Translator class
translator = Translator()

# Detect the language of the text
detected_lang = translator.detect(text).lang

# Translate the text to Hindi
if detected_lang != 'hi':
    hindi_text = translator.translate(text, src=detected_lang, dest='hi').text
else:
    hindi_text = text

# Create a new HTML page in Hindi
with open('index.html', 'w', encoding='utf-8') as f:
    f.write('<html>\n<head>\n<meta charset="utf-8">\n<title>Python (प्रोग्रामिंग भाषा)</title>\n</head>\n<body>\n')
    f.write(hindi_text)
    f.write('\n</body>\n</html>')

# Find all the links in the webpage
links = soup.find_all('a')

# Scrape the linked webpages and translate their contents to Hindi
for link in links:
    # Check if the link is valid
    if link.has_attr('href'):
        link_url = link['href']
        if link_url.startswith('http') or link_url.startswith('https'):
            # Make a GET request to the linked webpage
            response = requests.get(link_url)

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Get the text content of the webpage
            text = soup.get_text()

            # Detect the language of the text
            detected_lang = translator.detect(text).lang

            # Translate the text to Hindi
            if detected_lang != 'hi':
                hindi_text = translator.translate(text, src=detected_lang, dest='hi').text
            else:
                hindi_text = text

            # Create a new HTML page in Hindi
            with open(link.text + '.html', 'w', encoding='utf-8') as f:
                f.write('<html>\n<head>\n<meta charset="utf-8">\n<title>')
                f.write(link.text)
                f.write('</title>\n</head>\n<body>\n')
                f.write(hindi_text)
                f.write('\n</body>\n</html>')
