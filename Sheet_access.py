import os 
import get_stats
import random
import time
import statistics

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1PK31QXukbD6rdXK70Dbe6GAkpS6jAXB0kj_CD7KWQRA"

amount_of_accounts = 2



def full_data_scan(amount_of_accounts): 
    
    amount_of_accounts = amount_of_accounts + 2

    total_start_time = time.time()
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try: 
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

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
        
        

        for row in range (2,amount_of_accounts):
            start_time = time.time()

           
            id = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f"Roster!{id_column}{row}").execute()
            id = id.get("values", [])
            if id != []:
                id = id[0][0]

            if id != 0:
                
                
            
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
                
                sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Roster!C{row}:L{row}", valueInputOption="RAW", body={"values": [[alliance,server,power,merits,victories,defeats,killed,healed,dead,gathered]]}).execute()
                print(f"Updated stats for {id}", stats)
                # sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Roster!{power_column}{row}", valueInputOption="RAW", body={"values": [[power]]}).execute()
                # print(f"Updated power for {id}", power)
                # sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Roster!{kills_column}{row}", valueInputOption="RAW", body={"values": [[killed]]}).execute()
                # print(f"Updated killed for {id}", killed )
                # sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Roster!{healed_column}{row}", valueInputOption="RAW", body={"values": [[healed]]}).execute()
                # print(f"Updated healed for {id}, {healed}")   
                # sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Roster!{alliance_column}{row}", valueInputOption="RAW", body={"values": [[alliance]]}).execute()
                # print(f"Updated alliance for {id}")
                # # sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Roster!{server_column}{row}", valueInputOption="RAW", body={"values": [[server]]}).execute()
                # # print(f"Updated server for {id}")
                # sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Roster!{victories_column}{row}", valueInputOption="RAW", body={"values": [[victories]]}).execute()
                # print(f"Updated victories for {id}", victories)
                # sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Roster!{defeats_column}{row}", valueInputOption="RAW", body={"values": [[defeats]]}).execute()
                # print(f"Updated defeats for {id}", defeats)
                # sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Roster!{dead_column}{row}", valueInputOption="RAW", body={"values": [[dead]]}).execute()
                # print(f"Updated dead for {id}", dead)
                # sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Roster!{gathered_column}{row}", valueInputOption="RAW", body={"values": [[gathered]]}).execute()
                # print(f"Updated gathered for {id}", gathered)

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


    except HttpError as error:
        print(f"An error occured: {error}")
        

