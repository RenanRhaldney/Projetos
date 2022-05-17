from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from testes import Dados

url = 'https://rpachallenge.com/?lang=EN'
arquivoExcel = 'challenge.xlsx'
pasta_automacao = r'C:\Users\Renan Rhaldney\Documents\WorkSpace - PyCharm\WorkSpace-Python\Automação'
pasta_download = r'c:\Users\Renan Rhaldney\Downloads'

# 1 - Verificar se o arquivo existem na pasta, caso sim, exclui-los
if arquivoExcel in os.listdir(pasta_download):
    os.chdir(pasta_download)
    os.remove(arquivoExcel)
if arquivoExcel in os.listdir(pasta_automacao):
    os.chdir(pasta_automacao)
    os.remove(arquivoExcel)
if 'TelaDeConclusão.png' in os.listdir(pasta_automacao):
    os.remove('TelaDeConclusão.png')

# 2 - Abrir navegador e acessar site
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url)

# 3 - Fazer download
browser.find_element(By.XPATH, '//a[@target="_blank"]').click()

sleep(4)

# 4 - Mover o arquivo da pasta de download para a pasta de automacção, que é aonde estão os codigos python
os.rename(f'{pasta_download}\\{arquivoExcel}',
f'{pasta_automacao}\\{arquivoExcel}')

sleep(2)
# Pegar dados da planilha
dados_execel_df = pd.read_excel(arquivoExcel)

# Clicar no botão Start
browser.find_element(By.XPATH, '//button[contains(@class, waves-effect)]').click()

# Preencher os campos com os dados corretos (até ler a ultima linha do excel)
# e Dar submit
for indice, linha in dados_execel_df.iterrows():
    browser.find_element(By.XPATH, '//input[@ng-reflect-name="labelFirstName"]').send_keys(linha['First Name'])
    browser.find_element(By.XPATH, '//input[@ng-reflect-name="labelLastName"]').send_keys(linha['Last Name '])
    browser.find_element(By.XPATH, '//input[@ng-reflect-name="labelCompanyName"]').send_keys(linha['Company Name'])
    browser.find_element(By.XPATH, '//input[@ng-reflect-name="labelRole"]').send_keys(linha['Role in Company'])
    browser.find_element(By.XPATH, '//input[@ng-reflect-name="labelAddress"]').send_keys(linha['Address'])
    browser.find_element(By.XPATH, '//input[@ng-reflect-name="labelEmail"]').send_keys(linha['Email'])
    browser.find_element(By.XPATH, '//input[@ng-reflect-name="labelPhone"]').send_keys(str(linha['Phone Number']))
    # Clicar no botão de submit
    browser.find_element(By.XPATH, '//input[@class="btn uiColorButton"]').click()

# Tirar um print do navegador
browser.save_screenshot('TelaDeConclusão.png')

msg_de_conclusao = browser.find_element(By.XPATH, '//div[@class="message2"]').text

login = Dados.login
senha = Dados.senha

# create message object instance
msg = MIMEMultipart()

messagem = f"Segue em anexo print da tela de acertos e tempo de execução.\n\n{msg_de_conclusao}"
imagem = r'C:\Users\Renan Rhaldney\Documents\WorkSpace - PyCharm\WorkSpace-Python\Automação\TelaDeConclusão.png'

# setup the parameters of the message
password = senha
msg['From'] = login
msg['To'] = login
msg['Subject'] = 'Parabéns - Desafio concluido.'

msg.attach(MIMEText(messagem, 'plain'))

# Abre o arquivo em modo binario
with open(imagem, 'rb') as f:
    img_data = f.read()

# attach image to message body
msg.attach(MIMEImage(img_data, name=os.path.basename(imagem)))

# create server
server = smtplib.SMTP('smtp.gmail.com: 587')
server.ehlo() 
server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print (f"successfully sent email to {msg['To']}:")

sleep(5)
browser.quit()
