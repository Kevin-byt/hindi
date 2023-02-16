import requests
from bs4 import BeautifulSoup
import random

user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
]

# URL of the webpage to scrape
# URL = "https://realpython.github.io/fake-jobs/"
URL = "https://www.classcentral.com"
# URL = "https://www.imdb.com/"

# Make a GET request to the webpage
page = requests.get(URL,headers={'User-Agent': random.choice(user_agents_list)})

#Write the page contents to a html file
with open('scrap/index.html','w') as file:
    file.write(page.text)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# Get the text content of the webpage
text = soup.get_text()

# Find all the links in the webpage
links = soup.find_all('a')

linkcount = 0
pages = []
pagelink = {}

# Scrape the linked webpages and translate their contents to Hindi
for link in links:
    # Check if the link is valid
    if link.has_attr('href'):
        link_url_base = link['href']
        link_url = link['href']
        # link_url = URL + link_url
        # print(link_url)
        if link_url.startswith('http') or link_url.startswith('https'):
            print(link_url)

        else:
            link_url = URL + link_url
            print(link_url)

        # Make a GET request to the linked webpage
        response = requests.get(link_url)

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
            f.write(response.text)    
            pages.append(link_ref)  
        
        linkcount += 1
# print('PAGES')
# print(pages)
# print()
# print()
# print('PAGELINK')
# for key, value in pagelink.items():
#     print(f"{key} : {value}")

# print()
# print()

# Load the index.html file to edit the links file
with open("scrap/index.html", "r") as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all the links in the HTML
links = soup.find_all("a")

# Edit the links
for link in links:
    if link.has_attr('href'):
        link_url = link['href']

        if link_url in list(pagelink.keys()):
            newlink = link_url.replace(link_url, pagelink[link_url])
            link['href'] = newlink

    # Save the edited HTML
    with open("scrap/index2.html", "w") as file:
        file.write(str(soup))



# # Edit the links
# for link in links:
#     if link.has_attr('href'):
#         link_url = link['href']
#         if link_url.startswith('http') or link_url.startswith('https'):
#             if link_url in pagelink.items():
#                 newlink = link_url.replace(link_url, pagelink[link_url])
#                 link['href'] = newlink

#     # Save the edited HTML
#     with open("scrap/index2.html", "w") as file:
#         file.write(str(soup))
