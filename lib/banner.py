from colorama import Fore as color
from colorama import Style as font
from requests import get as g
def home():
    v = g('https://raw.githubusercontent.com/BDadmehr0/AnonPN/main/lib/V').text
    ascii_banner = color.WHITE+f'''
   ___                  ___  _  __
  / _ | ___  ___  ___  / _ \/ |/ /  |{color.GREEN} AnonPN{font.BRIGHT} {v}{font.NORMAL}{color.WHITE}
 / __ |/ _ \/ _ \/ _ \/ ___/    /   |{color.WHITE} get last phone number fake anonymsms.com{color.WHITE}
/_/ |_/_//_/\___/_//_/_/  /_/|_/    |{color.CYAN} https://github.com/BDadmehr0/AnonPN\n'''
    
    return ascii_banner
