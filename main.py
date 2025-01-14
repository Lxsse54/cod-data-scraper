from Sheet_access import *
from ID_scan import *




def choice():
    print("1. Full Data Scan based on ID's")
    print("2. ID Scan for a kingdom")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        # how many accounts would you like to scan?
        amount_of_accounts = int(input("How many accounts would you like to scan? "))
        full_data_scan(amount_of_accounts)
    elif choice == "2":
        server = int(input("Enter the server you would like to scan: "))
        amount_of_accounts = int(input("How many accounts would you like to scan? Scroll down to the first account that is over 15m, and input the number of that accounts ranking in the server "))
        id_scan(amount_of_accounts, server)
    elif choice == "3":
        exit()
    else:
        print("Invalid choice")
        choice()
    

choice()