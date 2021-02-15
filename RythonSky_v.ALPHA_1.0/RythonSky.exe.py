from tabulate import tabulate
import json
import time
import sys
import os

def cls():
    if os.name is not 'nt':
        os.system('clear')
    else:
        os.system('cls')

version = '.ALPHA 1.0'

user = os.getlogin()

cls()

def error(e):
    print(f'{bcolors.SPACE}{bcolors.RED}[-] ERROR: {e}')

def title(title):
    os.system(f'title {title}')

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    CYAN = '\u001b[36m'
    SPACE = '      '

def banner():
    title('RythonSky')
    print(f"""{bcolors.GREEN}
                                           , 
                                          ;o\ 
                                          ;Ob`. 
                                         ;OOOOb`. 
                                        ;OOOOOY" ) 
                                       ;OOOO' ,%%) 
                                   \  /OOO ,%%%%,%\\ 
                                    |:  ,%%%%%%;%%/ 
                                   ||,%%%%%%%%%%/ 
                                   ;|%%%%%%%%%'/`-'"`. 
                                   /: %%%%%%%%'/ c$$$$.`. 
                      `.______     \\ \\%%%%%%%'/.$$YF"Y$: ) 
                     _________ "`.\\`\\o \\`%%' ,',$F,.   $F ) 
           ___,--""'dOOO;,:%%`-._ o_,O_   ,',"',d88)  '  ) 
        -"'. YOOOOOOO';%%%%%%%%%;`-O   )_     ,X888F   _/ 
            \\ YOOOO',%%%%%%%%%%Y    \\__;`),-.  `""F  ,' 
             \\ `" ,%%%%%%%%%%,' _,-   \\-' \\_ `------' 
              \\_ %%%%',%%%%%_,-' ,;    ( _,-\\ 
                `-.__`%%',-' .c$$'     |\\-_,-\\ 
                     `""; ,$$$',md8oY  : `\\_,') 
                       ( ,$$$F `88888  ;   `--' 
                        \\`$$(    `""' / 
                         \\`"$$c'   _,' 
                          `.____,-' 
        {bcolors.YELLOW}
            ____        __  __               _____ __        
           / __ \__  __/ /_/ /_  ____  ____ / ___// /____  __
          / /_/ / / / / __/ __ \/ __ \/ __ \\__ \/ //_/ / / /
         / _, _/ /_/ / /_/ / / / /_/ / / / /__/ / ,< / /_/ / 
        /_/ |_|\__, /\__/_/ /_/\____/_/ /_/____/_/|_|\__, /  
              /____/                                /____/    

            Author: {bcolors.RED}fulltime_Me{bcolors.YELLOW} 
    """)
    print(f'{bcolors.SPACE}+[+[+[ {bcolors.GREEN}RythonSky{bcolors.RED} v{version}{bcolors.YELLOW} +]+]+')
    print(f'{bcolors.SPACE}+[+[+[ {bcolors.GREEN}made with VS-code{bcolors.YELLOW} +]+]+')
    print(f'    #' + '-'*100 + '#\n\n')

class Commands:
    def __init__(self):
        print(f'{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ Initializing program ]+]+]+\n')
        time.sleep(2)

    def exit(self):
        print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ {bcolors.RED}Exiting the program {bcolors.YELLOW}]+]+]+')
        time.sleep(2)
        sys.exit(0)

    def help(self):
        help_list_f = open('help.json')
        help_list = json.load(help_list_f)

        form = tabulate(help_list['help'], tablefmt='fancy_grid')
        print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ HELP ]+]+]+')
        print(form + '\n')

    def cls(self):
        if os.name is not 'nt':
            os.system('clear')
            pass
        else:
            os.system('cls')
            pass
        banner()

    def hunter(self):
        os.system('tools\social-hunt.exe')
        banner()

    def embomb(self):
        os.system('tools\email-bomb.exe')
        banner()

    def locait(self):
        os.system('tools\location-track.exe')
        banner()

    def scanner(self):
        os.system('tools\port-scanner.exe')
        banner()

    def settings(self):
        print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ {bcolors.GREEN}Settings...{bcolors.YELLOW} ]+]+]+\n')
        os.system('settings.exe')

    def changelog(self):
        c_file = open('change_log.cl', 'r')
        change_log = c_file.readlines()
        c_file.close()

        print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ CHANGE LOG ]+]+]+\n')
        for log in change_log:
            log = log.replace("\n", "")
            print(f'{bcolors.SPACE}{bcolors.CYAN}[?] {bcolors.YELLOW}{log}')
        print('')

    def cmd(self):
        print('')
        os.system('cmd')
        print('')
        cls()

    def reboot(self):
        print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ {bcolors.RED}REBOOTING... {bcolors.YELLOW}]+]+]+\n')
        time.sleep(2)
        os.system('reboot')

 

def main():
    while True:
        command = input(f'{bcolors.SPACE}{bcolors.YELLOW}[~] {bcolors.CYAN}RythonSky{bcolors.YELLOW}@{user}>> {bcolors.RED}')

        if command == 'exit':
            commands.exit()
        elif command == 'help':
            commands.help()
        elif command == 'hunter':
            title('RythonSky --  Social-Hunter')
            commands.hunter()
            commands.cls()
        elif command == 'cls':
            commands.cls()
        elif command == 'embomb':
            title('RythonSky -- EmBomber')
            commands.embomb()
            commands.cls()
        elif command == 'locait':
            title('RythonSky -- LocTracker')
            commands.locait()
            commands.cls()
        elif command == 'scanner':
            title('RythonSky -- PortScann')
            commands.scanner()
            commands.cls()
        elif command == 'settings':
            commands.settings()

        elif command == 'changelog':
            commands.changelog()
        elif command == 'cmd':
            title('RythonSky -- CMD')
            commands.cmd()
            banner()
        elif command == 'reboot':
            commands.reboot()


        
        elif command == '':
            pass
        else:
            print('')
            error('command not defined! \n')


if __name__ == '__main__':
    banner()
    commands = Commands()
    main()
    input()