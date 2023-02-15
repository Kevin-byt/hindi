from googletrans import Translator, LANGUAGES

# Initialize the Translator object
translator = Translator()

# Define the input text to translate
text = 'Hello, world!'

# Check if the input text is valid
if text and text.strip():
    # Detect the language of the input text
    detected_lang = translator.detect(text).lang

    # Translate the text to Hindi
    if detected_lang != 'hi':
        hindi_text = translator.translate(text, src=detected_lang, dest='hi').text
    else:
        hindi_text = text

    # Print the translated text
    print(hindi_text)
else:
    print("Input text is not valid.")
