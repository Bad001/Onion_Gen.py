from colorama import Fore, Style
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
    print(' Select from the menu:\n\n  1) Generate onion links\n  2) Verify onion links\n  0) Exit the script\n')

choice = '1'
while choice != '0':
    printMenu()
    choice = input('-> ')
    if choice == '1':
        print('choice 1')
    if choice == '2':
        print('choice 2')
