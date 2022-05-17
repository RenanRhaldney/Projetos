from distutils import text_file
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
#from Funcoes.FuncoesUteis import esperarPaginaCarregar

browser = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://selenium.dunossauro.live/aula_05_c.html'
browser.get(url)


def preencherFurmulario(navegador, filme, email, telefone):
    navegador.find_element(By.NAME, 'filme').send_keys(filme)
    navegador.find_element(By.NAME, 'email').send_keys(email)
    navegador.find_element(By.NAME, 'telefone').send_keys(telefone)
    navegador.find_element(By.NAME, 'enviar').click()


preencherFurmulario(browser, 'Matrix', 'JoseReinaldo@DaSilva', '(081)987654321')


# preencher formulario sem utilizar a função
""" # Preenchendo formulario
filme = browser.find_element(By.NAME, 'filme')
filme.send_keys('Matrix')

#tempo(browser, 'input')
email = browser.find_element(By.NAME, 'email')
email.send_keys('JoseReinaldo@DaSilva')

telefone = browser.find_element(By.NAME, 'telefone')
telefone.send_keys('(081)987654321')

enviar = browser.find_element(By.NAME, 'enviar').click """