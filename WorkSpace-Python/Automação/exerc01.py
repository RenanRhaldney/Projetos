from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
# from urllib.parse import urlparse

def get_links(browser, tag):
    elemento = browser.find_element(By.TAG_NAME, tag)
    ancoras = elemento.find_elements(By.TAG_NAME, 'a')
    textos_links = {}

    # Adiciona chave e valor no dicionario na ordem {texto : link}
    for ancora in ancoras:
        textos_links[ancora.text] = ancora.get_attribute('href')
        
    return textos_links


# Abre navegador
browser = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://selenium.dunossauro.live/aula_04.html'
# Acessa link da pagina informada
browser.get(url)
    
# Pegar e acessar link da tag que contem o texto "Exercício 3"
sleep(2)
exerc03 = get_links(browser, 'main')
browser.get(exerc03['Exercício 3'])

# Acessando link(começar por aqui)
sleep(2)
comecarPorAqui = get_links(browser, 'main')
browser.get(comecarPorAqui['Começar por aqui'])

# Acessando link (errado), mas que é o correto
main = browser.find_element(By.TAG_NAME, 'main')
ancoras = main.find_elements(By.TAG_NAME, 'a')
errado = {}

for ancora in ancoras:
    errado[ancora.get_attribute('attr')] = ancora.get_attribute('href')

sleep(2)
browser.get(errado['errado'])

# Acessando o link do 'href', que está na teg 'a', com o texto igual o titulo da pagina
sleep(8)
tituloPage = get_links(browser, 'main')
browser.get(tituloPage[browser.title])

# Acessando o link do 'href', que está na teg 'a', com o texto igual do path
sleep(2)
path_da_url = get_links(browser, 'main')
browser.get(path_da_url['page_3.html'])

sleep(2)
browser.refresh()
