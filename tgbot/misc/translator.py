from googletrans import Translator, LANGUAGES

from random import choice
from typing import Union


class TranslatorAPI:
    previous_code: str = ''
    codes = list(LANGUAGES.keys())

    def __init__(self):
        self.translator = Translator()
        self.final_dest = 'uk'

    def translate(self, text: str, dest: Union[str, list]) -> str:
        if isinstance(dest, list):
            dest = dest[0]
        translation = self.translator.translate(text, dest=dest)
        return translation.text
    
    def get_full_translation(self, text: str, epochs: int = 10) -> str:
        result = text
        source_code = self.detect_code(text)
        for _ in range(epochs):
            dest_code = self.get_code()
            result = self.translate(result, dest_code)
        result = self.translate(result, source_code)
        return result
    
    def detect_code(self, text: str) -> str:
        return self.translator.detect(text).lang
    
    @classmethod
    def get_code(cls) -> str:
        code = choice(cls.codes)
        while code == cls.previous_code:
            code = choice(cls.codes)
        cls.previous_code = code
        return code
