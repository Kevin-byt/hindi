# Import required libraries
import os
from googletrans import Translator
from bs4 import BeautifulSoup

# Set the path to the folder containing HTML files
# path = r"C:\Users\KK\Dropbox\Dev\Projects\python\hindi\trans"
path  = r"C:\Users\KK\Desktop\Scrap"
transpath = r"C:\Users\KK\Dropbox\Dev\Projects\python\hindi\trans"

# Create an instance of the translator
translator = Translator()

translated_files = []
for file in os.listdir(transpath):
    translated_files.append(file)

# Loop through each file in the folder
for filename in os.listdir(path):
    if filename.endswith(".html"):
        # Read the contents of the file
        if filename not in translated_files:
            try:
                with open(os.path.join(path, filename), "r", encoding="utf-8") as f:
                    contents = f.read()

            except:
                with open(os.path.join(path, filename), "r") as f:
                    contents = f.read()

            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(contents, "html.parser")

            # content = soup.find_all(['p', 'div', 'span', 'h1', 'h2', 'h3', 'title', 'li', 'a'])
            content = soup.find_all()

            for sentence in content:
                if sentence.string is not None:
                    translation = translator.translate(sentence.text, dest='hi').text

                    if translation is not None:
                        sentence.string = translation   

                        # Save the translated contents back to the file
                        try:
                            with open(os.path.join(transpath, filename), "w", encoding="utf-8") as f:
                                f.write(str(soup))

                        except:
                            with open(os.path.join(transpath, filename), "w") as f:
                                f.write(str(soup))
    