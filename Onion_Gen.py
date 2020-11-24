import random
import string
import requests
import base64
import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import x25519
from colorama import Fore, Style
from datetime import date

def printMenu():
    name ="     )\n"
    name +="  ( /(                          (\n"
    name +="  )\())        (                )\ )      (                  (\n"
    name +=" ((_)\    (    )\   (    (     (()/(     ))\  (       `  )   )\ )\n"
    name +="   ((_)   )\ )((_)  )\   )\ )   /(_))_  /((_) )\ )    /(/(  (()/(\n"
    name +="  / _ \  _(_/( (_) ((_) _(_/(  (_)) __|(_))  _(_/(   ((_)_\  )(_))\n"
    name +=" | (_) || ' \))| |/ _ \| ' \))   | (_ |/ -_)| ' \))_ | '_ \)| || |\n"
    name +="  \___/ |_||_| |_|\___/|_||_|_____\___|\___||_||_|(_)| .__/  \_, |\n"
    name +="                            |_____|                  |_|     |__/ \n"
    print(Fore.RED + name)
    print(Style.RESET_ALL)
    print(' Select from the menu:\n\n  1) Generate onion link\n  2) Verify onion link\n  0) Exit the script\n')

def generate_tor_v3_keys():
    #Generates public, private keypair
    private_key = x25519.X25519PrivateKey.generate()
    private_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.Raw	,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption())
    public_key = private_key.public_key()
    public_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw)
    global public
    public = base64.b32encode(public_bytes).replace(b'=', b'') \
                       .decode("utf-8")
    private = base64.b32encode(private_bytes).replace(b'=', b'') \
                        .decode("utf-8")
    return public, private

def verifyOnionLink(linkToVerify):
    session = requests.session()
    session.proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'TE': 'Trailers',
    }
    try:
        print(Fore.YELLOW+" Trying to connect to "+linkToVerify)
        print(Style.RESET_ALL)
        r = session.get(linkToVerify, headers=headers, timeout=10)
        session.cookies.clear()
    except:
        session.cookies.clear()
        print(Fore.RED+"  Connection to "+linkToVerify+" failed!")
        print(Style.RESET_ALL)
        return False
    print(Fore.GREEN+"  Connection to "+linkToVerify+" succeded, this site is online\n")
    print(Style.RESET_ALL)
    return True

def generateOnionLink(numLink):
    link = ''
    tmp = ''
    isOnionLinkOnline = False
    for i in range(int(numLink)):
        while not isOnionLinkOnline:
            generate_tor_v3_keys()
            tmp = ''.join(hashlib.sha1(map(str, public)).encode('utf-8').digest()[:10]).lower()+".onion"
            isOnionLinkOnline = verifyOnionLink(tmp)
        link += tmp+"\n"
    print("Your online link:\n"+link)
    response = input("Do you want to save those in a file? (y/N) -> ")
    if response.lower() == 'y' or response.lower() == 'yes':
        today = date.today()
        fp = open("Generated onion link "+today.strftime("%b-%d-%Y")+".txt","a")
        fp.write(link)
        fp.close()

choice = '1'
while choice != '0':
    printMenu()
    choice = input('-> ')
    if choice == '1':
        numLink = input('How many link do you want to generate: ')
        generateOnionLink(numLink)
    if choice == '2':
        linkToVerify = input('Type or paste the link you want to test: ')
        verifyOnionLink(linkToVerify)
