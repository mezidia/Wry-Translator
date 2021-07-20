def get_text(start_text: str) -> str:
    translated_text = start_text
    # Detect the language
    from langdetect import detect
    from_lang = detect(start_text)

    language_codes = [from_lang, 'es', 'uk', 'vi', 'tr', from_lang]

    for index in range(len(language_codes) - 1):
        from translate import Translator
        translator = Translator(from_lang=language_codes[index], to_lang=language_codes[index+1])
        translated_text = translator.translate(translated_text)

    return translated_text


print(get_text('Утер Светоносный'))
