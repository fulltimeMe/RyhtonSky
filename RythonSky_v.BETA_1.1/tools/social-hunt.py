import requests
import time
import sys
import os

def cls():
    if os.name is not 'nt':
         os.system('clear')
    else:
        os.system('cls')
version = '.BETA 1.1'

cls()

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

def banner():
    print(f"""{bcolors.GREEN}
                                      .-----------------TTTT_-----_______
                                /''''''''''(______O] ----------____  \______/]_
             __...---'\"\"\"\_ --''   Q                               ___________@
         |'''                   ._   _______________=---------\"\"\"\"\"\"\"
         |                ..--''|   l L |_l   |
         |          ..--''      .  /-___j '   '
         |    ..--''           /  ,       '   '
         |--''                /           `    \\
                              L__'         \    -
                                            -    '-.
                                             '.    /
                                               '-./
    {bcolors.YELLOW}
           _____            _       ____  __            __           
          / ___/____  _____(_)___ _/ / / / /_  ______  / /____  _____
          \__ \/ __ \/ ___/ / __ `/ / /_/ / / / / __ \/ __/ _ \/ ___/
         ___/ / /_/ / /__/ / /_/ / / __  / /_/ / / / / /_/  __/ /    
        /____/\____/\___/_/\__,_/_/_/ /_/\__,_/_/ /_/\__/\___/_/     
                                                             
             Author: {bcolors.RED}fulltime_Me{bcolors.YELLOW}   
    """)
    print(f'{bcolors.SPACE}+[+[+[ {bcolors.GREEN}Social-Hunter{bcolors.RED} v{version}{bcolors.YELLOW} +]+]+')
    print(f'{bcolors.SPACE}+[+[+[ {bcolors.GREEN}made with VS-code{bcolors.YELLOW} +]+]+')
    print(f"""
    \\\\\\__________________________________________________________________________///
    ///                                                                          \\\\\\ {bcolors.RESET}\n\n""")

class Social_Hunter:
    def __init__(self):
        try:
            print(f'{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ Initializing program ]+]+]+')
            time.sleep(2)
            self.target = str(input(f'{bcolors.SPACE}{bcolors.YELLOW}[~] Target: {bcolors.RED}'))

            # INSTAGRAM
            instagram = f'https://www.instagram.com/{self.target}/'

            # FACEBOOK
            facebook = f'https://www.facebook.com/{self.target}/'

            # TWITTER
            twitter = f'https://www.twitter.com/{self.target}/'

            # TIKTOK
            tiktok = f'https://www.tiktok.com/@{self.target}'

            # YOUTUBE
            youtube = f'https://www.youtube.com/{self.target}/'

            # BLOGGER
            blogger = f'https://{self.target}.blogspot.com'

            # GOOGLE+
            google_plus = f'https://plus.google.com/s/{self.target}/top'

            # REDDIT
            reddit = f'https://www.reddit.com/user/{self.target}/'

            # WORDPRESS
            wordpress = f'https://{self.target}.wordpress.com'

            # PINTEREST
            pinterest = f'https://www.pinterest.com/{self.target}/'

            # GITHUB
            github = f'https://www.github.com/{self.target}/'

            # TUMBLR
            tumblr = f'https://{self.target}.tumblr.com'

            # FLICKR
            flickr = f'https://www.flickr.com/people/{self.target}/'

            # STEAM
            steam = f'https://steamcommunity.com/id/{self.target}/'

            # VIMEO
            vimeo = f'https://vimeo.com/{self.target}/'

            # SOUNDCLOUD
            soundcloud = f'https://soundcloud.com/{self.target}/'

            # DISQUS
            disqus = f'https://disqus.com/by/{self.target}/'

            # MEDIUM
            medium = f'https://medium.com/@{self.target}/'

            # DEVIANTART
            deviantart = f'https://{self.target}.deviantart.com'

            # VK
            vk = f'https://vk.com/{self.target}/'

            # ABOUT.ME
            aboutme = f'https://about.me/{self.target}/'

            # IMGUR
            imgur = f'https://imgur.com/user/{self.target}/'

            # FLIPBOARD
            flipboard = f'https://flipboard.com/@{self.target}/'

            # SLIDESHARE
            slideshare = f'https://slideshare.net/{self.target}/'

            # FOTOLOG
            fotolog = f'https://fotolog.com/{self.target}/'

            # SPOTIFY
            spotify = f'https://open.spotify.com/user/{self.target}/'

            # MIXCLOUD
            mixcloud = f'https://www.mixcloud.com/{self.target}/'

            # SCRIBD
            scribd = f'https://www.scribd.com/{self.target}/'

            # BADOO
            badoo = f'https://www.badoo.com/en/{self.target}/'

            # PATREON
            patreon = f'https://www.patreon.com/{self.target}/'

            # BITBUCKET
            bitbucket = f'https://bitbucket.org/{self.target}/'

            # DAILYMOTION
            dailymotion = f'https://www.dailymotion.com/{self.target}/'

            # ETSY
            etsy = f'https://www.etsy.com/shop/{self.target}/'

            # CASHME
            cashme = f'https://cash.me/{self.target}/'

            # BEHANCE
            behance = f'https://www.behance.net/{self.target}/'

            # GOODREADS
            goodreads = f'https://www.goodreads.com/{self.target}/'

            # INSTRUCTABLES
            instructables = f'https://www.instructables.com/member/{self.target}/'

            # KEYBASE
            keybase = f'https://keybase.io/{self.target}'

            # KONGREGATE
            kongregate = f'https://kongregate.com/accounts/{self.target}'

            # LIVEJOURNAL
            livejournal = f'https://{self.target}.livejournal.com'

            # ANGELLIST
            angellist = f'https://angel.co/{self.target}'

            # LAST.FM
            last_fm = f'https://last.fm/user/{self.target}'

            # DRIBBBLE
            dribbble = f'https://dribbble.com/{self.target}'

            # CODECADEMY
            codecademy = f'https://www.codecademy.com/{self.target}'

            # GRAVATAR
            gravatar = f'https://en.gravatar.com/{self.target}'

            # PASTEBIN
            pastebin = f'https://pastebin.com/u/{self.target}'

            # FOURSQUARE
            foursquare = f'https://foursquare.com/{self.target}'

            # ROBLOX
            roblox = f'https://www.roblox.com/user.aspx?username={self.target}'

            # GUMROAD
            gumroad = f'https://www.gumroad.com/{self.target}'

            # NEWSGROUND
            newsground = f'https://{self.target}.newgrounds.com'

            # WATTPAD
            wattpad = f'https://www.wattpad.com/user/{self.target}'

            # CANVA
            canva = f'https://www.canva.com/{self.target}'

            # CREATIVEMARKET
            creative_market = f'https://creativemarket.com/{self.target}'

            # TRAKT
            trakt = f'https://www.trakt.tv/users/{self.target}'

            # 500PX
            five_hundred_px = f'https://500px.com/{self.target}'

            # BUZZFEED
            buzzfeed = f'https://buzzfeed.com/{self.target}'

            # TRIPADVISOR
            tripadvisor = f'https://tripadvisor.com/members/{self.target}'

            # HUBPAGES
            hubpages = f'https://{self.target}.hubpages.com'

            # CONTENTLY
            contently = f'https://{self.target}.contently.com'

            # HOUZZ
            houzz = f'https://houzz.com/user/{self.target}'

            #BLIP.FM
            blipfm = f'https://blip.fm/{self.target}'

            # WIKIPEDIA
            wikipedia = f'https://www.wikipedia.org/wiki/User:{self.target}'

            # HACKERNEWS
            hackernews = f'https://news.ycombinator.com/user?id={self.target}'

            # REVERBNATION
            reverb_nation = f'https://www.reverbnation.com/{self.target}'

            # DESIGNSPIRATION
            designspiration = f'https://www.designspiration.net/{self.target}'

            # BANDCAMP
            bandcamp = f'https://www.bandcamp.com/{self.target}'

            # COLOURLOVERS
            colourlovers = f'https://www.colourlovers.com/love/{self.target}'

            # IFTTT
            ifttt = f'https://www.ifttt.com/p/{self.target}'

            # EBAY
            ebay = f'https://www.ebay.com/usr/{self.target}'

            # SLACK
            slack = f'https://{self.target}.slack.com'

            # OKCUPID
            okcupid = f'https://www.okcupid.com/profile/{self.target}'

            # TRIP
            trip = f'https://www.trip.skyscanner.com/user/{self.target}'

            # ELLO
            ello = f'https://ello.co/{self.target}'

            # BASECAMP
            basecamp = f'https://{self.target}.basecamphq.com/login'

            self.WEBSITES = [instagram, facebook, twitter, youtube, tiktok, blogger, google_plus, reddit,
            wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus, 
            medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
            mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
            goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
            dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
            wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
            contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
            bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, basecamp]
        except Exception as e:
            error(e)

    def search(self):
        try:
            print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ Hunting down {bcolors.RED}{self.target}{bcolors.YELLOW}... ]+]+]+')
            time.sleep(0.5)
            print(f'{bcolors.SPACE}.......')
            time.sleep(0.5)
            print(f'{bcolors.SPACE}.......')
            time.sleep(0.5)

            print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ Social-Hunter{bcolors.RED} v{version}{bcolors.YELLOW} ist working ]+]+]+')
            time.sleep(0.5)
            print(f'{bcolors.SPACE}.......')
            time.sleep(0.5)
            print(f'{bcolors.SPACE}.......')
            time.sleep(1)

            count = 0

            print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ {bcolors.RED}{self.target}{bcolors.YELLOW} MATCHES FOUND ]+]+]+')

            for url in self.WEBSITES:
                r = requests.get(url)
                if r.status_code == 200:
                    count += 1
                    print(f"\n{bcolors.SPACE}{bcolors.GREEN}[+]{bcolors.YELLOW} MATCH {bcolors.RED}{self.target}{bcolors.YELLOW} matching: {bcolors.RED}{url}{bcolors.YELLOW} - {bcolors.GREEN}{r.status_code}{bcolors.YELLOW} - OK")
                    if self.target in r.text:
                        print(f'{bcolors.SPACE}{bcolors.SPACE}{bcolors.YELLOW}MATCH: {bcolors.RED}{url}{bcolors.YELLOW} POSITIVE: {bcolors.RED}{self.target}{bcolors.YELLOW} in text.')
                    else:
                        print(f'{bcolors.SPACE}{bcolors.SPACE}{bcolors.YELLOW}MATCH: {bcolors.RED}{url}{bcolors.YELLOW} POSITIVE: {bcolors.RED}could be a FALSE POSITIVE.{bcolors.YELLOW}')
                else:
                    print(f"\n{bcolors.SPACE}{bcolors.RED}[-]{bcolors.YELLOW} NO MATCH {bcolors.RED}{self.target}{bcolors.YELLOW} not matching: {bcolors.RED}{url}{bcolors.YELLOW} - {bcolors.RED}{r.status_code}{bcolors.YELLOW} - NOT OK")
                        
            total = len(self.WEBSITES)

            print(f'\n{bcolors.SPACE}{bcolors.YELLOW}+[+[+[ FINISHED: A total of {bcolors.RED}{count}{bcolors.YELLOW} MATCHES out of {bcolors.RED}{total}{bcolors.YELLOW} WEBSITES. ]+]+]+')
        except Exception as e:
            error(e)

if __name__ == '__main__':
    banner()
    hunter = Social_Hunter()
    hunter.search()
    input()