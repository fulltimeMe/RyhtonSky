import socket
import time
import sys
import os

def cls():
    if os.name is not 'nt':
        os.system('clear')
    else:
        os.system('cls')

version = '.BETA 1.1'

def error(e):
    print(f'{bcolors.SPACE}{bcolors.RED}[-] ERROR: {e}')
    time.sleep(5)
    input(f'{bcolors.SPACE}.......')
    sys.exit(1)

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    SPACE = '      '

cls()

def banner():
    print(f'''{bcolors.GREEN}
                               ____
                          /___.`--.____ .--. ____.--(
                                 .'_.- (    ) -._'.
                               .'.'    |'..'|    '.'.
                        .-.  .' /'--.__|____|__.--'\ '.  .-.
                       (O).)-| |  \    |    |    /  | |-(.(O)
                        `-'  '-'-._'-./      \.-'_.-'-'  `-'
                           _ | |   '-.________.-'   | | _
                        .' _ | |     |   __   |     | | _ '.
                       / .' ''.|     | /    \ |     |.'' '. \\
                       | |( )| '.    ||      ||    .' |( )| |
                       \ '._.'   '.  | \    / |  .'   '._.' /
                        '.__ ______'.|__'--'__|.'______ __.'
                       .'_.-|         |------|         |-._'.
                    //\\\\  |         |--::--|         |  //\\\\
                   //  \\\\ |         |--::--|         | //  \\\\
                  //    \\\\|        /|--::--|\        |//    \\\\
                 / ""'._.-'/|_______/ |--::--| \_______|\`-._.\\
                / __..--'          /__|--::--|__\      `--..__ \\
               / /                 '-.|--::--|.-'             \ \\
              / /                     |--::--|                 \ \\
             / /                      |--::--|                  \ \\
         _.-'  `-._                   _..||.._                _.-` '-._
        '--..__..--'                 '-.____.-'              '--..__..-'
    {bcolors.YELLOW}
               ____                __  _____                          
              / __ \ ____   _____ / /_/ ___/ _____ ____ _ ____   ____ 
             / /_/ // __ \ / ___// __/\__ \ / ___// __ `// __ \ / __ \\
            / ____// /_/ // /   / /_ ___/ // /__ / /_/ // / / // / / /
           /_/     \____//_/    \__//____/ \___/ \__,_//_/ /_//_/ /_/

                Author: {bcolors.RED}fulltime_Me{bcolors.YELLOW} 
    ''')
    print(f'{bcolors.SPACE}+[+[+[ {bcolors.GREEN}Port-Scann{bcolors.RED} v{version}{bcolors.YELLOW} +]+]+')
    print(f'{bcolors.SPACE}+[+[+[ {bcolors.GREEN}made with VS-code{bcolors.YELLOW} +]+]+')
    print(f"""
    \\\\\\__________________________________________________________________________///
    ///                                                                          \\\\\\ {bcolors.RESET}\n\n""")

class Scanner:
    def __init__(self):
        try:
            self.port = 1000
            print(f'{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ Initializing program ]+]+]+\n')
            time.sleep(2)

            self.target = input(f'{bcolors.SPACE}{bcolors.YELLOW}[~] Target: {bcolors.RED}')
            self.start = int(input(f'{bcolors.SPACE}{bcolors.YELLOW}[~] Starting Port: {bcolors.GREEN}'))
            self.end = int(input(f'{bcolors.SPACE}{bcolors.YELLOW}[~] Ending Port: {bcolors.GREEN}'))+1
        except Exception as e:
            error(e)

    def scann(self):
        print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ Scaning {bcolors.RED}{self.target}{bcolors.YELLOW}... ]+]+]+\n')
        time.sleep(1)

        for port in range(self.start, self.end):
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = self.s.connect_ex((self.target, port))
            self.open_p = []
            if result == 0:
                print(f'\n{bcolors.SPACE}{bcolors.GREEN}[+]{bcolors.YELLOW} PORT {bcolors.RED}{port}{bcolors.YELLOW} from {bcolors.RED}{self.target}{bcolors.YELLOW} is:  {bcolors.GREEN}OPENED{bcolors.YELLOW}')
                self.open_p.append(port)
            else:
                print(f'\n{bcolors.SPACE}{bcolors.RED}[-]{bcolors.YELLOW} PORT {bcolors.RED}{port}{bcolors.YELLOW} from {bcolors.RED}{self.target}{bcolors.YELLOW} is:  {bcolors.RED}NOT OPENED{bcolors.YELLOW}')
            self.s.close()
           
    def printing(self):
        print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ Scaning {bcolors.RED}{self.target}{bcolors.YELLOW} finished ]+]+]+\n')



if __name__ == '__main__':
    banner()
    scanner = Scanner()
    scanner.scann()
    scanner.printing()
    input()