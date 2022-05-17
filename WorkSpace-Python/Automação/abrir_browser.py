from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


def find_by_text(browser, tag, text):
    elementos = browser.find_elements(By.TAG_NAME, tag)

    for elemento in elementos:
        if elemento.text == text:
            return elemento
    return print('Link não encontrado.')

browser = webdriver.Chrome(ChromeDriverManager().install())

url = 'http://selenium.dunossauro.live/aula_04_b.html'

browser.get(url)
sleep(2)
elemento = find_by_text(browser, 'div', 'um')
elemento.click()

