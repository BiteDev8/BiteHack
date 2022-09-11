from colorama import Fore, Back, Style, init
import time
import random
import pyfiglet
T = "BiteHack"
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)
init()
a = "AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn1234567890."

cookie= ''.join(random.choice(a)for i in range(111))

def gen_ip():
    h = "123456789"
    first = ''.join((random.choice(h)for i in range(2)))
    second = ''.join((random.choice(h)for i in range(2)))
    third = ''.join((random.choice(h)for i in range(2)))
    four = ''.join((random.choice(h)for i in range(2)))

    ipres = first + "." + second + "." + third +"." + four

    return ipres

ip = gen_ip()

def gen_cc():
    h = "1234567890"
    first = ''.join((random.choice(h)for i in range(4)))
    second = ''.join((random.choice(h)for i in range(4)))
    third = ''.join((random.choice(h)for i in range(4)))
    four = ''.join((random.choice(h)for i in range(4)))

    ccres = first + "." + second + "." + third +"." + four

    return ccres

cc = gen_cc()

def gen_token():
    a = "AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn1234567890"
    first = ''.join((random.choice(a)for i in range(24)))
    second = ''.join((random.choice(a)for i in range(6)))
    third = ''.join((random.choice(a)for i in range(27)))

    result = first + "." + second + "." + third

    return result

token = gen_token()

print(Fore.GREEN+"tag discord a hack:")
x = str(input())

print("hack en cours...")
time.sleep(3)
print("tokens hack...")
time.sleep(5)
print("initialisation...")
time.sleep(2)

print("")
print("Token :",token)
print("ip :",ip)
print("cookie roblox :",cookie )
print("credit cart :",cc ," date :08/24  cap :652" )

input()
