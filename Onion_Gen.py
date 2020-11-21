import random
import string
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

def randomString():
    letters_and_digits = string.ascii_lowercase + string.digits
    myString = ''.join((random.choice(letters_and_digits) for i in range(16)))
    return myString

def verifyOnionLink(linkToVerify):
    #to do
    return True

def generateOnionLink(numLink):
    link = ''
    tmp = ''
    isOnionLinkOnline = False
    for i in range(int(numLink)):
        while not isOnionLinkOnline:
            tmp = "http://"+randomString()+".onion/"
            isOnionLinkOnline = verifyOnionLink(tmp)
        link += tmp+"\n"
    print("Your online link:\n"+link)
    response = input("Do you want to save those in a file? (y/N) -> ")
    if response == 'y' or response == 'Y':
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
