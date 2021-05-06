from colorama import init, Fore, Back, Style
import requests 

init()

def main():

    i = 0

    print(''' 
                 ██▀███   █    ██  ███▄    █  ███▄    █ ▓█████  ██▀███  ▒███████▒
                ▓██ ▒ ██▒ ██  ▓██▒ ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒ ▒ ▒ ▄▀░
                ▓██ ░▄█ ▒▓██  ▒██░▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒░ ▒ ▄▀▒░ 
                ▒██▀▀█▄  ▓▓█  ░██░▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄    ▄▀▒   ░
                ░██▓ ▒██▒▒▒█████▓ ▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒▒███████▒
                ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░░▒▒ ▓░▒░▒
                  ░▒ ░ ▒░░░▒░ ░ ░ ░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░░░▒ ▒ ░ ▒
            404 ░░   ░  ░░░ ░ ░    ░   ░ ░    ░   ░ ░    ░     ░░   ░ ░ ░ ░ ░ ░
                ░        ░              ░          ░    ░  ░   ░       ░ ░    
                                                        ░        
    ''')

    print('             [+]         Github: https://github.com/waitForTheQ           [+]\n\n\n')

    ALLOWED = 0
    FILE = open('output.txt', 'w')
    RESET = FILE.write('')

    USER_URL = input('URL: ')
    USER_PATH = input("Path of the wordlist : ")
    USER_OUTPUT = input("Output ? (Y/N)").lower()

    if not USER_PATH: 
        PATH_WORDLIST = open('SecLists/Discovery/Web-Content/big.txt', 'r')
    else:
        PATH_WORDLIST = open(USER_PATH,'r')

    if USER_OUTPUT == 'y':
        ALLOWED = 1
    elif USER_OUTPUT == 'n':
        pass

        
    for i in PATH_WORDLIST: 

        FINAL_URL = USER_URL + f'{i}'
        REQUEST = requests.get(FINAL_URL.strip())

        if REQUEST.status_code == 200: 
            print(f'{i}/' + '-> '+FINAL_URL+Fore.GREEN+' | CODE: 200 |\n'+Style.RESET_ALL) 
            if ALLOWED == 1:
                FILE.write(f'{i}/' + '-> | CODE: 200 |')
              

        if REQUEST.status_code == 403: 
            print(f'{i}/' + '-> '+FINAL_URL+Fore.RED+" | CODE : 403 |\n"+Style.RESET_ALL)
            if ALLOWED == 1:
                FILE.write(f'{i}/' + '-> | CODE 403 | ')

        if REQUEST.status_code == 404:
            print(f'{i}/' + '-> '+FINAL_URL+Fore.RED+" | CODE : 404 |\n"+Style.RESET_ALL)
            
main() 
