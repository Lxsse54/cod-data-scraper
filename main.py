from Sheet_access import *
from ID_scan import *




def choice():
    print("1. Full Data Scan based on ID's")
    print("2. ID Scan for a kingdom")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        resizeWindow()
        shutdown = False
        # in how many minutes would you like to start scanning?
        delay = int(input("in how many minutes would you like to start scanning?"))
        shutdown_q = input("Would you like to shutdown the computer after the scan? (y/n)")
        if shutdown_q == "y":
            shutdown = True
            
        if shutdown == True and delay == 0:
            print("The scan will start immediately, and the computer will shutdown afterwards")
        elif shutdown == True and delay > 0:
            print(f"The scan will start in {delay} minutes, and the computer will shutdown afterwards")
        elif shutdown == False and delay > 0:
            print(f"The scan will start in {delay} minutes, and the computer will NOT shutdown afterwards")
        elif shutdown == False and delay == 0:
            print("The scan will start immediately, and the computer will NOT shutdown afterwards")
        
        full_data_scan(delay)
    elif choice == "2":
        server = int(input("Enter the server you would like to scan: "))
        amount_of_accounts = int(input("How many accounts would you like to scan? Scroll down to the first account that is over 15m, and input the number of that accounts ranking in the server "))
        id_scan(amount_of_accounts, server)
    elif choice == "3":
        exit()
    else:
        print("Invalid choice")
        choice()
        
    if shutdown == True:
        os.system('shutdown -s')
    

choice()
