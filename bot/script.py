from translate import Translator


translator = Translator(to_lang="uk")
translation = translator.translate("Hello, dad")
print(translation)