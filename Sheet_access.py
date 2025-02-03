import os 
import get_stats
import random
import time
import statistics
import gspread
from datetime import datetime, timezone

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1rJSwd8K-Vc8p1Au66ZexeSw56EvnpWyct25T--l3iBE"

amount_of_accounts = 2
spreadsheet_name = "Script"
credentials = None

creds = Credentials.from_authorized_user_file("token.json", scopes=SCOPES)
client = gspread.authorize(creds)
sheets = client.open_by_key(SPREADSHEET_ID)




def full_data_scan(delay): 
        
    
    delay = delay * 60
    time.sleep(delay)
    total_start_time = time.time()

    ID_list = sheets.worksheet("ID_list")
    sheets.duplicate_sheet(ID_list.id, new_sheet_name=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))

    id_list = sheets.sheet1.col_values(1)
    #remove the first entry
    id_list.pop(0)
    
    
    id_column = "A"
    name_column = "B"
    alliance_column = "C"
    server_column = "D"
    power_column = "E"
    merits_column = "F"
    victories_column = "G"
    defeats_column = "H"
    kills_column = "I"
    healed_column = "J"
    dead_column = "K"
    gathered_column = "L"

    runtimes_list = []

    
    for id in id_list:
        row = id_list.index(id) + 2


        if id != 0:
                    
                    
                    start_time = time.time()
                    stats = get_stats.main(id)
                    alliance = stats["alliance"]
                    merits = stats["merits"]
                    power = stats["power"]
                    healed = stats["healed"]
                    killed = stats["killed"]
                    victories = stats["victories"]
                    defeats = stats["defeats"]
                    dead = stats["dead"]
                    gathered = stats["gathered"]
                    server = stats["server"]
                    
                    
                    
                    print(stats)
                    
                    # get all values from stats without the id
                    stats.pop("id")
                    values = list(stats.values())
                    print (values)
                    sheets.sheet1.update(range_name= f"{alliance_column}{row}:{gathered_column}{row}", values = [values])
                    print(f"Updated stats for {id}", stats)
                    
                    

                    
                    
                    end_time = time.time()
                    execution_time = end_time - start_time
                    runtimes_list.append(execution_time)
                    print ("Time for this account: " , execution_time, "seconds")

    average_runtime = statistics.mean(runtimes_list) 
    print("average runtime per account: ", average_runtime)
    total_end_time = time.time()
    total_execution_time = total_end_time - total_start_time
    amount_of_accounts_done = runtimes_list.__len__()
    print("Total runtime : ", total_execution_time, ". Accounts done: ", amount_of_accounts_done)
            # os.system('shutdown -s')
        

    
        
