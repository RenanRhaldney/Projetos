from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
sleep(10)

#contatos = 'College Work Group'
#mensagem = 'iae isso aqui é um teste do meu bot ignorem'

# copyable-text selectable-text


campo_pesquisa = driver.find_element(By.XPATH, '//div[contains(@class, "copyable-text selectable-text")]')
sleep(6)
campo_pesquisa.click()
campo_pesquisa.send_keys('College Work Group')
campo_pesquisa.send_keys(Keys.ENTER)
sleep(3)

campo_mensagem = driver.find_elements(By.XPATH, '//div[contains(@class, "copyable-text selectable-text")]')[1]
sleep(3)
campo_mensagem.click()
sleep(3)
campo_mensagem.send_keys('iae isso aqui é um teste do meu bot ignorem')
campo_mensagem.send_keys(Keys.ENTER)
sleep(30)



