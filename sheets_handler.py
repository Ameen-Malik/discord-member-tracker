from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

class GoogleSheetsHandler:
    def __init__(self):
        # Set up Google Sheets credentials
        self.creds = Credentials.from_service_account_file(
            'service-account.json',
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        
        self.spreadsheet_id = os.getenv('SHEETS_SPREADSHEET_ID')
        self.service = build('sheets', 'v4', credentials=self.creds)
        
    async def log_member(self, member_data):
        """Log new member join"""
        try:
            values = [[
                member_data['user_id'],
                member_data['username'],
                member_data['discriminator'],
                member_data['joined_at'],
                member_data['created_at'],
                str(member_data['is_bot'])
            ]]
            
            body = {
                'values': values
            }
            
            self.service.spreadsheets().values().append(
                spreadsheetId=self.spreadsheet_id,
                range='Member Joins!A:F',
                valueInputOption='RAW',
                body=body
            ).execute()
            
            print(f"Logged new member: {member_data['username']}")
            
        except Exception as e:
            print(f"Error logging member: {e}")
            
    async def is_verified(self, user_id):
        """Check if user_id exists in verified members list"""
        try:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range='Verified Members!A:A'
            ).execute()
            
            values = result.get('values', [])
            return [user_id] in values
            
        except Exception as e:
            print(f"Error checking verification: {e}")
            return False 