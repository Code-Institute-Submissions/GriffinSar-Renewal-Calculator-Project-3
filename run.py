""" 
Import external libraries for the program
"""
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
import gspread 
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Sales_Program')

def first_page():
    """
    Intro Page where the user can select the mode they want to use.
    """
    print(Fore.GREEN + Style.BRIGHT + "Welcome to your Renewal Calculator!\n") 
    print(Fore.MAGENTA + Style.BRIGHT + """\
     _________
    | ________ |
    ||12345678||
    |----------|
    |[M|#|C][-]|
    |[7|8|9][+]|
    |[4|5|6][x]|
    |[1|2|3][%]|
    |[.|O|:][=]|
     __________ \n""")

    print("This program lets you to enter last years")
    print("renewal cost and get this years uplifted price.")
    print("Along with multi-year pricing.\n")
    print("You can also save and retrieve customer pricing details")

    while True:
        print(Fore.CYAN + Style.BRIGHT + "Enter 1 if you want to start a new\
        \ncalculation.")
        print(Fore.CYAN + Style.BRIGHT + "Enter 2 if you want to access\
        \nhistorical data for a customer")

        mode = input("Please enter your selection here:\n")
        if mode == "1":
            new_customer()
            break
        elif mode == "2":
            hist_data()
            break
        else:
            print(Fore.LIGHTYELLOW_EX + "Invalid input, please try again.\n")   


first_page()