import gspread
from google.oauth2 import service_account
from twilio.rest import Client
from config import TWILIO_TOKEN  # Add config.py whith token

# Cinfig Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = service_account.Credentials.from_service_account_file('credentials.json', scopes=scope)
gc = gspread.service_account(filename='credentials.json', scopes=scope)

spreadsheet = gc.open('YOUR_GOOLESHEET_NAME')

worksheet = spreadsheet.get_worksheet(0)

# Number form Google Sheet
phone_number = '+48' + worksheet.cell(1, 1).value

# Cinfig Twilio
twilio_sid = 'your_sid'
twilio_phone_number = 'your_number'

# Init Twilio
twilio_client = Client(twilio_sid, TWILIO_TOKEN) 

# Send SMS
twilio_client.messages.create(
    body='HI!',
    from_=twilio_phone_number,
    to=phone_number
)

print(f"SMS Send to {phone_number}")
