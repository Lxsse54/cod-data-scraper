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

# print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1rJSwd8K-Vc8p1Au66ZexeSw56EvnpWyct25T--l3iBE"

amount_of_accounts = 5
spreadsheet_name = "Script"

id_column = "A"



creds = Credentials.from_authorized_user_file("token.json", scopes=SCOPES)
client = gspread.authorize(creds)
sheets = client.open_by_key(SPREADSHEET_ID)


ID_list = sheets.worksheet("ID_list")
#sheets.duplicate_sheet(ID_list.id, new_sheet_name=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))



stats = {
    "Alliance": "AllianceName",
    "Server": "ServerName",
    "Power": "123456",
    "Merits": "100",
    "Victories": "50",
    "Defeats": "10",
    "Killed": "200",
    "Healed": "150",
    "Dead": "30",
    "Gathered": "5000"
}

print(stats)

row = 2
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

values = list(stats.values())
    
print(f"{alliance_column}{row}:{gathered_column}{row}")
sheets.sheet1.update(range_name= f"{alliance_column}{row}:{gathered_column}{row}", values = [values])







#  try:
#         if not credentials or not credentials.valid:
#             if credentials and credentials.expired and credentials.refresh_token:
#                     credentials.refresh(Request())
#             else:
#                     flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
#                     credentials = flow.run_local_server(port=0)
#             with open("token.json", "w") as token:
#                     token.write(credentials.to_json())
#     except:
#         print("auth error")

#     try: 
#             service = build("sheets", "v4", credentials=credentials)
#             sheets = service.spreadsheets()
#     except HttpError as error:
#             print(f"An error occured: {error}")
