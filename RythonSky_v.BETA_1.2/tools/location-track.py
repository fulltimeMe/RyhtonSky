from geopy.geocoders import Nominatim
import geocoder
import time
import sys
import os

def cls():
    if os.name is not 'nt':
         os.system('clear')
    else:
        os.system('cls')

version = '.BETA 1.2'

cls()

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    SPACE = '      '

def error(e):
    print(f'{bcolors.SPACE}{bcolors.RED}[-] ERROR: {e}')
    time.sleep(5)
    input(f'{bcolors.SPACE}.......')
    sys.exit(1)

def banner():
    print(f"""{bcolors.GREEN}
                              :
                              |
                              |
                             :|:
                             |||
                        _____|||_____
                       /=============\\
                   ---<~~~~~~~~~~~~~~~>---
                       \-------------/
                        \___________/
                          \||:::||/
                           ||:::||
                           ||:::||
                           ||:::||
                           ||ooo||
                           ||___||
                           ||:::||
                           ||:::||
                           ||:::||
                          /||:::||\\
                         / ||:::|| \\
                        /  ||:::||  \\
                       /   ||:::||   \\
                   ___/____||:::||____\____
                  /~~~~~~~~~~~~~~~~~~~~~~~~\\
                 /   |~~~~~~~~|  _____      \\
                 |   |________| |  |  |     |
              ___|______________|__|__|_____|___{bcolors.YELLOW}
          __             ______                __            
         / /  ____  ____/_  __/________ ______/ /_____  _____
        / /  / __ \/ ___// / / ___/ __ `/ ___/ //_/ _ \/ ___/
       / /__/ /_/ / /__ / / / /  / /_/ / /__/ ,< /  __/ /    
      /_____|____/\___//_/ /_/   \__,_/\___/_/|_|\___/_/

            Author: {bcolors.RED}fulltime_Me{bcolors.YELLOW}      
    """)
    print(f'{bcolors.SPACE}+[+[+[ {bcolors.GREEN}Location-tracker{bcolors.RED} v{version}{bcolors.YELLOW} +]+]+')
    print(f'{bcolors.SPACE}+[+[+[ {bcolors.GREEN}made with VS-code{bcolors.YELLOW} +]+]+')
    print(f"""
    \\\\\\__________________________________________________________________________///
    ///                                                                          \\\\\\ {bcolors.RESET}\n\n""")

class Tracker:
    def __init__(self):
        try:
            print(f'{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ Initializing program ]+]+]+')
            time.sleep(2)
            self.ip= str(input(f'{bcolors.SPACE}{bcolors.YELLOW}[~] Target: {bcolors.RED}'))

            self.geolocator = Nominatim(user_agent="geoapiExercises")

            self.g = geocoder.ip(self.ip)

            self.location = self.geolocator.reverse(self.g.latlng)
        except Exception as e:
            error(e)

    def locait(self):
        try:
            print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ Locaiting {bcolors.RED}{self.ip}{bcolors.YELLOW}... ]+]+]+')
            time.sleep(1)
            self.address = self.location.raw['address']

            city = self.address.get('city', '')
            country = self.address.get('country', '')
            cords = str(self.g.latlng)
            town = self.address.get('town', '')
            shop = self.address.get('shop', '')
            road = self.address.get('road', '')
            neighbourhood = self.address.get('neighbourhood', '')
            city_district = self.address.get('city_district', '')
            postcode = self.address.get('postcode', '')
            country_code = self.address.get('country_code', '')
                    
            informationList = [['city:', city], ['cords:', cords], ['town:', town], ['city_district:', city_district], ['neighbourhood:', neighbourhood], ['shop:', shop], ['road:', road], ['country:', country], ['postcode:', postcode], ['country_code:', country_code]]
            for item in informationList:
                if not item[1] == '':
                    print(f'\n{bcolors.SPACE}{bcolors.GREEN}[+]{bcolors.YELLOW} FOUND: {self.ip} {bcolors.RED}{item[0]} {item[1]}')
                else:
                    print_item = item[0].replace(':', '')
                    print(f'\n{bcolors.SPACE}{bcolors.RED}[-]{bcolors.YELLOW} NOT FOUND: {self.ip} {bcolors.RED}{print_item}')
                time.sleep(0.5)

            print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ Locaiting target {bcolors.RED}{self.ip}{bcolors.YELLOW} finished. ]+]+]+')
        except Exception as e:
            error(e)

if __name__ == '__main__':
    banner()
    tracker = Tracker()
    tracker.locait()
    input()