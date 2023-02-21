# from bs4 import BeautifulSoup

# # read in the HTML file
# with open('page2.html', 'r') as f:
#     html = f.read()

# # create a BeautifulSoup object from the HTML
# soup = BeautifulSoup(html, 'html.parser')

# # extract all the text from the HTML
# text = soup.get_text()

# # print the text
# print(text)

# from google.cloud import translate_v2 as translate
# from bs4 import BeautifulSoup

# # instantiate the translation client
# client = translate.Client()

# # read in the input HTML file
# with open('input.html', 'r') as f:
#     html = f.read()

# # create a BeautifulSoup object from the HTML
# soup = BeautifulSoup(html, 'html.parser')

# # extract all the text from the HTML
# text = soup.get_text()

# # define the target language
# target_language = 'hi'

# # use the translation client to translate the text
# result = client.translate(text, target_language=target_language)

# # create a new BeautifulSoup object from the translated text
# translated_soup = BeautifulSoup(result['translatedText'], 'html.parser')

# # replace the original text with the translated text in the new BeautifulSoup object
# for original, translated in zip(soup.strings, translated_soup.strings):
#     original.replace_with(translated)

# # write out the translated HTML file
# with open('output.html', 'w') as f:
#     f.write(str(soup))

# from googletrans import Translator
# from bs4 import BeautifulSoup

# # Load the HTML file
# with open('trans/page2.html', 'r', encoding='utf-8') as f:
#     html_doc = f.read()

# # Parse the HTML content
# soup = BeautifulSoup(html_doc, 'html.parser')

# # Extract the English text from the HTML content
# english_text = soup.get_text()

# # Translate the English text to Hindi
# translator = Translator()
# hindi_text = translator.translate(english_text, dest='hi').text

# # Replace the English text with Hindi text in the HTML content
# soup.body.string = hindi_text

# # Save the translated HTML file
# with open('trans/output.html', 'w', encoding='utf-8') as f:
#     f.write(str(soup))

####################################################################################################################

# import requests
# from bs4 import BeautifulSoup
# from googletrans import Translator

# # Set the URL of the English webpage to translate
# # url = 'https://www.example.com'

# # Send a GET request to the URL
# # response = requests.get(url)

# # Load the HTML file
# with open('trans/page2.html', 'r', encoding='utf-8') as f:
#     html_doc = f.read()

# # Create a BeautifulSoup object with the response content
# soup = BeautifulSoup(html_doc, 'html.parser')

# # Translate the title of the webpage to Hindi
# translator = Translator()
# hindi_title = translator.translate(soup.title.string, dest='hi').text
# soup.title.string.replace(soup.title.string, hindi_title)

# # Translate all text in the HTML content to Hindi
# for tag in soup.find_all(True):
#     if tag.name not in ['script', 'style']:
#         translated_text = translator.translate(tag.text, dest='hi').text
#         tag.text.replace(tag.text, translated_text)

# # Create a new HTML file with the translated content
# with open('trans/translated_page.html', 'w', encoding='utf-8') as f:
#     f.write(str(soup))


##########################################################################################################

# from googletrans import Translator
# import re

# with open('trans/page2.html', 'r', encoding='utf-8') as file:
#     html = file.read()

# pattern = re.compile(r'>[^<]+<')
# english_text = ''
# for match in re.findall(pattern, html):
#     english_text += match[1:-1]

# translator = Translator()
# hindi_text = translator.translate(english_text, dest='hi').text

# output = re.sub(pattern, '>' + hindi_text + '<', html)

# with open('trans/output.html', 'w', encoding='utf-8') as file:
#     file.write(output)


####################################################################################
# from googletrans import Translator
# from bs4 import BeautifulSoup

# translator = Translator()

# with open('trans/page2.html', 'r', encoding='utf-8') as file:
#     html = file.read()

# soup = BeautifulSoup(html, 'html.parser')

# for tag in soup.find_all(['p', 'div', 'span', 'h1', 'h2', 'h3', 'title']):
#     english_text = tag.text
#     hindi_text = translator.translate(english_text, dest='hi').text
#     tag.string = hindi_text

# with open('trans/output.html', 'w', encoding='utf-8') as file:
#     file.write(str(soup))


############################################################################################################
# from bs4 import BeautifulSoup
# from googletrans import Translator
# import os

# def translate_text(text):
#     translator = Translator()
#     result = translator.translate(text, src='en', dest='hi')
#     return result.text


# def translate_html_file(file_path):
#     # Open the HTML file
#     with open(file_path, 'r', encoding='utf-8') as f:
#         html = f.read()

#     # Parse the HTML using BeautifulSoup
#     soup = BeautifulSoup(html, 'html.parser')

#     # Find all text elements and translate them
#     for element in soup.find_all(text=True):
#         # Only translate text that is not already in Hindi
#         if not element.parent.name in ['style', 'script'] and not element.strip().startswith('<'):
#             translated_text = translate_text(element.strip())
#             element.replace_with(translated_text)

#     # Save the translated HTML to a new file
#     translated_html = str(soup)
#     translated_file_path = os.path.splitext(file_path)[0] + '_hi.html'
#     with open(translated_file_path, 'w', encoding='utf-8') as f:
#         f.write(translated_html)


# folder_path = r'C:\Users\KK\Dropbox\Dev\Projects\python\hindi\trans'
# for file_name in os.listdir(folder_path):
#     if file_name.endswith('.html'):
#         file_path = os.path.join(folder_path, file_name)
#         translate_html_file(file_path)

################################################################################################################################

from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()

with open("trans/index2.html", "r", encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all the links in the HTML
content = soup.find_all(['p', 'div', 'span', 'h1', 'h2', 'h3', 'title'])
# content = soup.find_all()

for sentence in content:
    if sentence.string is not None:
        translation = translator.translate(sentence.text, dest='hi').text

        sentence.string = translation   

        with open("trans/output.html", "w", encoding='utf-8') as file:
            file.write(str(soup))



