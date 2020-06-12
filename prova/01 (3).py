from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import platform
import time
import random


arquivo = open('frases.txt', 'r')
linhas = arquivo.read()

for j in range(len(linhas)):
	frasesArray = linhas.split('.')
aux = []
print(frasesArray)

# para não pedir confirmação de uso de camera e microfone 
chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")


# Abrir o navegador com o driver correto
if platform.system() == 'Linux':
	browser = webdriver.Chrome(executable_path='./driver/chromedriver', options=chrome_options) # Linux
else:
	browser = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)   # Windows

# abre o link do AVA para a sala desejada
browser.get("https://us.bbcollab.com/guest/d3c0bb8b107d4c9092488ff4f6383be7")
#https://us.bbcollab.com/collab/ui/session/guest/26e8b2cea87140b79e4e1bfcc247f02a
control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_id("guest-name")
		nomeElem.send_keys("Jack Bot")
	except:
		print('[ERROR] Campo nome não encontrado. Outra tentativa acontecerá em %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - Nome digitado com sucesso.')
		control = 0


# clica no botão next


control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="launch-html-guest"]')
		nomeElem.click()
	except:
		print('[ERROR] Campo nome não encontrado. Outra tentativa acontecerá em %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - Botão encontrado.')
		control = 0



# fecha a configuração de audio e vídeo
time.sleep(2)

control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="techcheck-modal"]/button')
		nomeElem.click()

	except:
		print('[ERROR] botão não encontrado, tentando novamente em: %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - Botão encontrado.')
		control = 0



# fecha o tutorial do AVA
time.sleep(2)


control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="announcement-modal-page-wrap"]/button')
		nomeElem.click()

	except:
		print('[ERROR] botão não encontrado, tentando novamente em: %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - Botão encontrado.')
		control = 0



# clicar na aba
time.sleep(2)
control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="side-panel-open"]')
		nomeElem.click()

	except:
		print('[ERROR] bate papo não encontrado, tentando novamente em: %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - bate papo encontrado.')
		control = 0


#encontra o bate papo todos
time.sleep(2)
control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="chat-channel-scroll-content"]/ul/li/ul/li')
		nomeElem.click()

	except:
		print('[ERROR] bate papo todos não encontrado, tentando novamente em: %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - bate papo todos encontrado.')
		control = 0




#escolhe a mensagem aleatóriamente		
for i in range(len(frasesArray)):
    while (len(aux) < len(frasesArray)):
        valorsort = random.choice(frasesArray)
        while valorsort in aux:
            valorsort = random.choice(frasesArray)

        # clicar no campo escrever a mensagem e enviar
        while control > 0:
            try:
                time.sleep(10)
                nomeElem = browser.find_element_by_id("message-input")
                time.sleep(2)
                nomeElem.send_keys(valorsort)
                nomeElem.send_keys(Keys.ENTER)
            except:
                print('[ERROR] Não foi conseguido enviar a mensagem com sucesso %d' % (control))

                control += 1
            else:
                print(valorsort)
                aux += [valorsort]
                print('[OK] -Mensagem enviada com sucesso')
                control = 0
        control = 1
#print('Mensagem gravada')
#print(aux)

		
# Volta para escolher outro bate papo
time.sleep(1)

control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="panel-back-button"]/bb-svg-icon')
		nomeElem.click()

	except:
		print('[ERROR] botão não encontrado, tentando novamente em: %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - voltando para escolha de bate papo.')
		control = 0

#abre a escolha de alunos
time.sleep(1)
control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="panel-control-participants"]')
		nomeElem.click()

	except:
		print('[ERROR] campo não encontrado, tentando novamente em: %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - campo encontrado.')
		control = 0


#abrir opção do estudante

time.sleep(1)
control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="participant-list-item-10"]/div/div/div/div/div[1]/div[4]/div[4]/button')
		nomeElem.click()
		#//*[@id="participant-list-item-4"]/div/div/div/div/div[1]/div[4]/div[5]
		#//*[@id="participant-list-item-70"]/div/div/div/div/div[1]/div[4]/div[4]/button
		#//*[@id="participant-list-item-10"]/div/div/div/div/div[1]/div[4]/div[5]/button
		#//*[@id="participant-list-item-70"]/div/div/div/div/div[1]/div[4]/div[5] -- erro
		#//*[@id="participant-list-item-70"]/div/div/div/div/div[1]/div[4]/div[5]/button -- erro
		#//*[@id="participant-list-item-70"]/div/div/div/div/div[1]/div[4]/div[5]/button/bb-svg-icon -- erro
	except:
		print('[ERROR] botão opções não encontrado, tentando novamente em: %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - opções encontradas.')
		control = 0

#abrir conversa com aluno

time.sleep(1)
control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="participant-controls-dropdown-10"]/li/button/span/span')
		nomeElem.click()

	except:
		print('[ERROR] botão enviar mensagem, tentando novamente em: %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - enviar mensagem encontrado.')
		control = 0


#envia mensagem pro colega
time.sleep(1)
control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_id('message-input')
		time.sleep(2)
		nomeElem.send_keys('Oi gata.')
		nomeElem.send_keys(Keys.ENTER)
		time.sleep(1)
		nomeElem.send_keys('Ta funcionando')
		nomeElem.send_keys(Keys.ENTER)

	except:
		print('[ERROR] campo não encontrado, tentando novamente em: %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - campo encontrado.')
		control = 0


print("Bot executado com sucesso. :)")
