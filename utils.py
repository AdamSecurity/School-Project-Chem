from colorama import Fore
from datetime import date

blue   = Fore.BLUE
white  = Fore.WHITE 
green  = Fore.GREEN 
yellow = Fore.YELLOW 
red    = Fore.RED

def success(msg):
    print(f"[{green}+{white}] {msg}")

def wait(msg):
    print(f"[{blue}*{white}] {msg}")

def exiting():
    print(f"[{yellow}~{white}] GoodBye ...:)")

def error():
    print(f"[{red}!{white}] You Have Some Error")

def banner():
    banner = f'''
{date.today()}    Chemistry App   Made by: Abdullah Almobark

0) show menu

1) Balancing the chemical formula
2) Get information about elements
3) Get the molar mass of compound 
4) Get percentage by mass

69) Exit
'''
    print(banner)
banner()

def option():
    opt = '''
1) grams
2) moles
3) molecules
'''
    print(opt)