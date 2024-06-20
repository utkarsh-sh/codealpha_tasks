from googletrans import Translator

def translate_text_google(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text


text_to_translate = input("Enter any text you want to translate : ")
target_language = input("Enter the language in which you want to translate: ")
translated_text = translate_text_google(text_to_translate, target_language)
print(translated_text)

