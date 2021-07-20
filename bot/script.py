from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as BS
from langdetect import detect


def get_translated_text(start_text: str) -> str:
    """
    Translate text through six languages
    :param start_text: input text
    :return: translated text
    """
    translated_text = start_text
    from_lang = detect(start_text)
    language_codes = [from_lang, 'uk']

    driver = webdriver.Chrome('bot\chromedriver.exe')
    for index in range(len(language_codes) - 1):
        base_url = 'https://www.deepl.com/ru/translator#{}/{}/{}'
        driver.get(base_url.format(language_codes[index], language_codes[index+1], translated_text))
        sleep(5)
        html = driver.page_source
        soup  = BS(html)
        translated_text = soup.select('.lmt__translations_as_text__text_btn')[0].text
    return translated_text
