# SMSFromSheets
# Integrating with Google Sheets and Twilio SMS in Python

This project demonstrates the integration of Google Sheets and Twilio to send SMS messages based on data from a Google Sheets spreadsheet.

## Requirements

- Python 3.x
- Python packages: gspread, google-auth, twilio

## Configuration

1. Clone the repository to your computer:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo

2. Install the necessary Python packages:

```bash
pip install gspread google-auth twilio

3. Create a credentials.json file containing the credentials for accessing the Google Sheets API. The file should contain a JSON service account key.

4. Create a config.py file and place your Twilio Token in it:

```bash
# config.py

TWILIO_TOKEN = 'Twilio_Token'  # Place your actual token here

5.In the main.py file, you will find the main application code. Before running it, make sure you have properly configured your API keys and Twilio tokens.

## Running the Application

To run the application, follow these steps:

```bash
python main.py

The application will retrieve data from Google Sheets and send an SMS to the specified phone number.




