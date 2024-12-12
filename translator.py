from googletrans import Translator

# Dictionary of available languages
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh-cn",
    "Hindi": "hi"
}

def translate_text():
    # Show available languages
    print("Available Languages:")
    for language, code in languages.items():
        print(f"{language}: {code}")

    # Get user inputs
    source_text = input("\nEnter the text you want to translate: ")
    target_language_input = input("Enter the target language name or code (e.g., English or en): ").strip()

    # Validate the input and determine the target language code
    if target_language_input in languages.keys():  # If input is a language name
        target_language = languages[target_language_input]
    elif target_language_input in languages.values():  # If input is a language code
        target_language = target_language_input
    else:
        print("Invalid language input. Please select from the available options.")
        return

    # Perform the translation
    try:
        translator = Translator()
        translation = translator.translate(source_text, dest=target_language)
        print("\nTranslated Text:")
        print(translation.text)
    except Exception as e:
        print(f"An error occurred during translation: {e}")

# Run the translation function
if __name__ == "__main__":
    translate_text()
