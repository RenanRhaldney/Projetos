from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from smtplib import SMTP
from testes import Dados
import os

url = 'https://quotes.toscrape.com'
pasta_automacao = r'c:\Users\Renan Rhaldney\Documents\WorkSpace - PyCharm\WorkSpace-Python\Automação'
arquivo = 'scraping.txt'

# 1 - Abrir navegador e acessar site
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url)

# 2 - Verificar se o arquivo existem na pasta, caso sim, exclui-los
if arquivo in os.listdir(pasta_automacao):
    os.chdir(pasta_automacao)
    os.remove(arquivo)
else:
    print('Arquivo não existe na pasta de automação.')

# 3 - Extraindo dados e adicionando em um arquivo .txt
contador = 1
# Abrir documento em modo append, caso ele não exista vai criar.
with open('scraping.txt', 'a', encoding="utf-8") as f:
    # Utilizando (try excepy) porque na ultima pagina não tem o botão de next e a automação vai tentar clicar dando erro em seguida
    try:
        while True:        
            textos = browser.find_elements(By.XPATH, '//span[@class="text"]')
            autores = browser.find_elements(By.XPATH, '//small[@class="author"]')
            f.write(f'-------------------PAGINA {contador}------------------- \n')
            
            # vai repetir de acordo com a quantidade de frases
            for i in range(len(textos)):
                # Escreve no arquivo txt a frase e o nome do autor
                f.write('Texto: ' + textos[i].text + '\n' + 
                'Autor: ' + autores[i].text + '\n\n')

            contador += 1
            botao = browser.find_element(By.XPATH, '//li[@class="next"]')
            botao.find_element(By.XPATH, 'a').click()
    except:
        print('Extração de dados concluida')

# 4 - Enviar email com anexo
server = SMTP('smtp.gmail.com', '587')
server.ehlo()
server.starttls()
server.login(Dados.login, Dados.senha)

corpo = 'Scraping feito com sucesso, segue em anexo arquivo com os dados de texto e autor de cada pagina.'

msg = MIMEMultipart()
msg['from'] = Dados.login
msg['to'] = Dados.login
msg['subject'] = 'Desafio 2 de Scraping feito com Selenium'
msg.attach(MIMEText(corpo, 'plain'))

# abrindo arquivo em modo leitura binaria
cam_arquivo = r'c:\Users\Renan Rhaldney\Documents\WorkSpace - PyCharm\WorkSpace-Python\Automação\scraping.txt'
ler_anexo = open(cam_arquivo, 'rb')

# ler o arquivo em binario e transforma o arquivo em base64 (que é oque o email entende)
anexo = MIMEBase('application', 'octet-stream')
anexo.set_payload(ler_anexo.read())
encoders.encode_base64(anexo)

# adiciona arquivo no cabeçalho do email
anexo.add_header('content-disposition', 'attachment; filename=scraping.txt')

# Fechando arquivo
ler_anexo.close

# Anexando o arquivo no corpo do email
msg.attach(anexo)

# envia o email no servidor SMTP
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()

print (f"successfully sent email to {msg['To']}:")