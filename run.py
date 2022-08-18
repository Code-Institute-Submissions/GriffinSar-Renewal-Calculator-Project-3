""" 
Import external libraries for the program
"""
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
import gspread 
from google.oauth2.service_account import Credentials
import pandas as pd


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Sales_Program')
stored_info = SHEET.worksheet('database')

def hist_data():
    """
    Allows user to view saved details
    """
    cust_name = input("Enter your customer name here:\n")

    if stored_info.find(cust_name, in_column=1):
         print(Fore.LIGHTCYAN_EX + Style.BRIGHT +
              "\nThe details you currently have saved are:\n")
         df = pd.DataFrame(stored_info.get_all_records())
         user_record = df.loc[df['Customer'] == cust_name].to_string(index=False)
         print(f"{Fore.LIGHTRED_EX }{Style.BRIGHT}\n{user_record}\n")
    else:
         print(Fore.LIGHTYELLOW_EX + "No Data Found to match this customer name")

    while True:
        print("What would you like to do now?")
        print("Type 'a' to check another customer.")
        print("Type 'b' to return to the main menu.")
        print("Type 'c' to exit the renewal calculator")

        selection = input("Enter your selection here:\n")
        selection = selection.lower()

        if selection == "a":
            hist_data()
        elif selection == "b":
            first_page()
        elif selection == "c":
            print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\
        \nThank you for using the calculator and goodbye.")
        break

    else:
        print(Fore.LIGHTYELLOW_EX +
        "\nYou do not currently have any details stored.")
        print(Fore.LIGHTYELLOW_EX + "Returning to the main menu...")
        first_page()


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
    print("It also calculates multi-year pricing.")
    print("You can save and retrieve customer pricing details as well\n")

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