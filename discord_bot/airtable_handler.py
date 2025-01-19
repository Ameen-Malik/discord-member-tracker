from airtable import Airtable
import os
from dotenv import load_dotenv

load_dotenv()

class AirtableHandler:
    def __init__(self):
        self.api_key = os.getenv('AIRTABLE_API_KEY')
        self.base_id = os.getenv('AIRTABLE_BASE_ID')
        
        # Table for logging new joins
        self.joins_table = Airtable(
            self.base_id,
            'Member Joins',
            api_key=self.api_key
        )
        
        # Table containing verified member list
        self.verified_table = Airtable(
            self.base_id,
            'Verified Members',
            api_key=self.api_key
        )
        
    async def log_member(self, member_data):
        """Log new member join"""
        try:
            self.joins_table.insert(member_data)
            print(f"Logged new member: {member_data['username']}")
        except Exception as e:
            print(f"Error logging member: {e}")
            
    async def is_verified(self, user_id):
        """Check if user_id exists in verified members list"""
        try:
            formula = f"{{Discord ID}}='{user_id}'"
            records = self.verified_table.get_all(formula=formula)
            return len(records) > 0
        except Exception as e:
            print(f"Error checking verification: {e}")
            return False 