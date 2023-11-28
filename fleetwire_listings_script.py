import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


# set up credentials
creds = service_account.Credentials.from_service_account_file(
    './google_sheets_api_keys.json',
    scopes=[os.getenv('SCOPES')])

# set up API client
service = build('sheets', 'v4', credentials=creds)

# specify the sheet and range you want to retrieve data from
sheet_id = os.getenv('SHEET_ID')
sheet_range = os.getenv('SHEET_RANGE')

# retrieve data from the sheet
result = service.spreadsheets().values().get(spreadsheetId=sheet_id, range=sheet_range).execute()
rows = result.get('values', [])

# print the data
for row in rows:
    print(row[0])
