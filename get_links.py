from bs4 import BeautifulSoup


# Load the index.html file to edit the links file
with open("page.html", "r") as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all the links in the HTML
links = soup.find_all("a")
count = 1
urls = []

# Edit the links
for link in links:
    if link.has_attr('href'):
        link_url = link['href']
        if link_url.startswith('http') or link_url.startswith('https'):
            newlink = link_url.replace(link_url, 'page2.html')
            link['href'] = newlink


    # Save the edited HTML
    with open("page.html", "w") as file:
        file.write(str(soup))
