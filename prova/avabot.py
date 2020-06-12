from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import platform
import time
import random

#abre arquivo de mensagem
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
	
#abre o ava
browser.get("https://univel.br/ava")

#informa o usuário
control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="formAva"]/form/div[1]/input')
		nomeElem.send_keys("Ejlima")
	except:
		print('[ERROR] Campo nome não encontrado. Outra tentativa acontecerá em %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - Nome digitado com sucesso.')
		control = 0

#informa a senha
time.sleep(1)
control = 1
while control > 0:
	try:	
		nomeElem = browser.find_element_by_xpath('//*[@id="formAva"]/form/div[2]/input')
		nomeElem.send_keys('26998971')
	except:
		print('[ERROR] Campo senha não encontrada. Outra tentativa acontecerá em %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - senha digitada com sucesso.')
		control = 0

#clica no botão para logar
time.sleep(1)
control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="formAva"]/form/div[4]/input')
		nomeElem.click()
	except:
		print('[ERROR] Botao não encontrado. Outra tentativa acontecerá em %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - botao encontrado com sucesso.')
		control = 0

#abre a materia
time.sleep(1)
control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="snap-pm-courses-current-cards"]/div[4]/div/h3/a')
		nomeElem.click()
	except:
		print('[ERROR] materia não encontrada. Outra tentativa acontecerá em %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - materia encontrada com sucesso.')
	control = 0

#abre a aula
time.sleep(2)
control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="module-72084"]/div/div/div[2]/h3/a/p')
		nomeElem.click()
	except:
		print('[ERROR] aula não encontrada. Outra tentativa acontecerá em %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - aula encontrada com sucesso.')
		control = 0

#participar da sessão
time.sleep(4)
control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="maininfo"]/div/a')
		nomeElem.click()
	except:
		print('[ERROR] Sessão não encontrada. Outra tentativa acontecerá em %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - Entrando na sessão.')
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

#abre a escolha de bate papos
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


#abrir opções do bate papo

time.sleep(1)
control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="participant-options-menu-toggle"]')
		nomeElem.click()
		#
		#//*[@id="participant-list-item-70"]/div/div/div/div/div[1]/div[4]/div[4]/button mensagem direta
		
	except:
		print('[ERROR] botão opções não encontrado, tentando novamente em: %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - opções encontradas.')
		control = 0

#Abre o campo e pesquisa o aluno
control = 1
while control > 0:
	try:
		aluno = input("Digite o nome do aluno:")
		nomeElem = browser.find_element_by_xpath('//*[@id="participant-options-menu"]/ul/li[1]')
		nomeElem.click()
		time.sleep(2)
		nomeElem = browser.find_element_by_xpath('//*[@id="search-dropdown"]/input')
		nomeElem.send_keys(aluno)
		#//*[@id="participant-options-menu"] erro
		#//*[@id="participant-options-menu"]/ul/li[1]/button erro
		#//*[@id="participant-options-menu"]/ul/li[1]/button/span erro
		#//*[@id="medium--search"]/g erro
		#//*[@id="medium--search"] erro
		#//*[@id="participant-options-menu"]/ul/li[1]/button/bb-svg-icon/svg/use erro
		#//*[@id="participant-options-menu"]/ul/li[1]/button/bb-svg-icon/svg 	 erro
		#//*[@id="participant-options-menu"]/ul/li[1]/button/bb-svg-icon  	erro
		
	except:
		print('[ERROR] Aluno não encontrado. Outra tentativa acontecerá em %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - Aluno encontrado com sucesso.')
		control = 0
	

#abrir opções do aluno

time.sleep(1)
control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//div[@class="participant-icons__wrap participant-controls-static"]/button')
		nomeElem.click()
		#participant-controls live ng-scope ng-isolate-scope erro
		#participant-controls-toggle has-tooltip participant-button icon-button erro
		#ng-scope ng-isolate-scope erro
		#svg-icon small default erro
		#//div[@class="participant-icons__wrap participant-controls-static"]/button
	except:
		print('[ERROR] botão opções não encontrado, tentando novamente em: %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - Opções encontradas.')
		control = 0


#Abre a conversa com o Aluno
time.sleep(1)
control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//button[@class="button menu-list__control focus-item"]')
		nomeElem.click()
		#
		#//*[@id="participant-controls-dropdown-23"]/li/button
		#
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
		pvmensagem = input("Digite uma mensagem:")
		nomeElem = browser.find_element_by_id('message-input')
		time.sleep(2)
		nomeElem.send_keys(pvmensagem)
		nomeElem.send_keys(Keys.ENTER)
		time.sleep(1)
		nomeElem.send_keys('Funcionou mano')
		nomeElem.send_keys(Keys.ENTER)

	except:
		print('[ERROR] campo não encontrado, tentando novamente em: %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - campo encontrado.')
		control = 0


print("Bot executado com sucesso. :)")
