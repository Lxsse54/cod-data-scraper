import os 
import get_stats
import random
import time
import statistics
import gspread
from datetime import datetime, timezone
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json




SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1rJSwd8K-Vc8p1Au66ZexeSw56EvnpWyct25T--l3iBE"

# Path to the service account JSON file
CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "token.json"

# amount_of_accounts = 2
# spreadsheet_name = "Script"
# credentials = None

# creds = Credentials.from_authorized_user_file("token.json", scopes=SCOPES)
# client = gspread.authorize(creds)
# sheets = client.open_by_key(SPREADSHEET_ID)

def get_credentials():
    creds = None
    
    # Load credentials if they exist
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as token:
            token_data = json.load(token)
            creds = Credentials.from_authorized_user_info(token_data, SCOPES)
    
    # If credentials are invalid or expired, refresh or request new ones
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
            
            # Save new credentials
            with open(TOKEN_FILE, "w") as token:
                json.dump({
                    "token": creds.token,
                    "refresh_token": creds.refresh_token,
                    "token_uri": creds.token_uri,
                    "client_id": creds.client_id,
                    "client_secret": creds.client_secret,
                    "scopes": creds.scopes
                }, token)
    
    return creds

def access_google_sheets():
    creds = get_credentials()
    client = gspread.authorize(creds)
    
    # Example: Open a Google Sheet and read data
    SPREADSHEET_ID = "your_spreadsheet_id"
    sheet = client.open_by_key(SPREADSHEET_ID).sheet1
    
    # Read values from Sheet1 (A1:D10)
    values = sheet.get("A1:D10")
    
    if not values:
        print("No data found.")
    else:
        for row in values:
            print(row)








  
creds = get_credentials()
client = gspread.authorize(creds)
sheets = client.open_by_key(SPREADSHEET_ID)
id_list = sheets.sheet1.col_values(1)
print(id_list)