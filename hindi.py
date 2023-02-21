import requests
from bs4 import BeautifulSoup
import random
import time
import cloudscraper
import cfscrape
from googletrans import Translator

user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
]

google_cache = 'https://webcache.googleusercontent.com/search?q=cache:'
URL = "https://www.classcentral.com"

# Make a GET request to the webpage
target_page = google_cache+URL

#Create Cloud scraper instance
scraper = cfscrape.create_scraper(delay=20)

#scrape target
info = scraper.get(URL, headers={'User-Agent': random.choice(user_agents_list)})

#Write the page contents to a html file
with open('scrap/index.html','w') as file:
    file.write(info.text)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(info.content, 'html.parser')

# Get the text content of the webpage
text = soup.get_text()

# Find all the links in the webpage
links = soup.find_all('a')

linkcount = 0
pages = []
pagelink = {}

translator = Translator()

# Scrape the linked webpages and translate their contents to Hindi
for link in links:
    # Check if the link is valid
    if link.has_attr('href'):
        link_url_base = link['href']
        link_url = link['href']

        if link_url.startswith('http') or link_url.startswith('https'):
            link_url = link_url

        else:
            link_url = URL + link_url

        # Make a GET request to the linked webpage
        response = scraper.get(link_url, headers={'User-Agent': random.choice(user_agents_list)})

        if response.status_code != 200:
            time.sleep(2)
            print(f'Previous: {link_url} --> {response.status_code}')
            response = scraper.get(google_cache+link_url, headers={'User-Agent': random.choice(user_agents_list)})
            print(f'Curent: {link_url} --> {response.status_code}')

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Get the text content of the webpage
        text = soup.get_text()

        link_text = link.text.replace('\n', '').replace('\"', '').replace("\'", '').replace("?",'')
        clean_text = link_text.strip()
        # print(f'LINK: {clean_text}')

        link_ref= clean_text + str(linkcount) + '.html'
        pagelink[link_url_base] = link_ref

        # Create a new HTML page in Hindi
        with open('scrap/' + clean_text + str(linkcount) + '.html', 'w', encoding='utf-8') as f:     
            # print(f"Writing {linkcount} ....")           
            f.write(response.text)    
            # print(f"DONE Writing {linkcount}....")

        with open('scrap/' + clean_text + str(linkcount) + '.html', "r", encoding='utf-8') as file:
            html_content = file.read()

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")

        # Find all the links in the HTML
        imgs = soup.find_all("img")

        for img in imgs:
            if img.has_attr('data-src') and img.has_attr('src'):
                img['src'] = img['data-src']

        #Translate to Hindi
        # with open('scrap/' + clean_text + str(linkcount) + '.html', 'r', encoding='utf-8') as file:
        #     html = file.read()

        # soup = BeautifulSoup(html, 'html.parser')

        # for tag in soup.find_all(['p', 'div', 'span', 'h1', 'h2', 'h3', 'title']):
        #     if tag.string is not None:
        #         english_text = tag.text
        #         hindi_text = translator.translate(english_text, dest='hi').text
        #         tag.string = hindi_text

        #     with open('scrap/' + clean_text + str(linkcount) + '.html', 'w', encoding='utf-8') as file:
        #         file.write(str(soup))
        
        linkcount += 1
        time.sleep(2)

# Load the index.html file to edit the links file
# with open("scrap/index.html", "r") as file:
with open("scrap/main.html", "r", encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all the links in the HTML
links = soup.find_all("a")
imgs = soup.find_all("img")

# Edit the links
for link in links:
    if link.has_attr('href'):
        link_url = link['href']

        if link_url in list(pagelink.keys()):
            newlink = link_url.replace(link_url, pagelink[link_url])
            link['href'] = newlink

    # Save the edited HTML
    
    with open("scrap/index2.html", "w", encoding='utf-8') as file:
        file.write(str(soup))


#Translate index page to Hindi
# with open("scrap/index2.html", 'r', encoding='utf-8') as file:
#     html = file.read()

# soup = BeautifulSoup(html, 'html.parser')

# for tag in soup.find_all(['p', 'div', 'span', 'h1', 'h2', 'h3', 'title']):
#     if tag.string is not None:
#         english_text = tag.text
#         hindi_text = translator.translate(english_text, dest='hi').text
#         tag.string = hindi_text

#     with open("scrap/index2.html", 'w', encoding='utf-8') as file:
#         file.write(str(soup))
