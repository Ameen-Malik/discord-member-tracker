# Discord Member Tracker

A Discord bot that automatically tracks server members and manages verification against Airtable or Google Sheets. The bot logs all new member joins and can automatically verify members against a master list, assigning roles accordingly.

## Features

- 🔄 Automatic member join logging to Airtable/Google Sheets
- ✅ Member verification against a master list
- 👥 Automatic role assignment for verified members
- 🔐 Admin commands for verification management
- 📊 Detailed member data tracking including:
  - User ID
  - Username
  - Join date
  - Account creation date
  - Bot status

## Technology Stack

- Python 3.7+
- discord.py
- Airtable API / Google Sheets API
- python-dotenv

## Prerequisites

Before running the bot, you'll need:

- Python 3.7 or higher installed
- A Discord Bot Token ([Create one here](https://discord.com/developers/applications))
- Either:
  - Airtable API Key and Base ID
  - OR Google Sheets API credentials (service-account.json)
- A Discord server with administrator permissions

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/discord-member-tracker.git
cd discord-member-tracker
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up your environment variables by creating a `.env` file:
```env
# Discord Configuration
DISCORD_TOKEN=your_bot_token
DISCORD_GUILD_ID=your_guild_id
VERIFIED_ROLE_ID=your_role_id

# Choose either Airtable OR Google Sheets configuration

# Airtable Configuration
AIRTABLE_API_KEY=your_airtable_api_key
AIRTABLE_BASE_ID=your_base_id

# OR Google Sheets Configuration
SHEETS_SPREADSHEET_ID=your_spreadsheet_id
```

## Database Setup

### Airtable Setup
1. Create a new Airtable base
2. Create two tables:
   - `Member Joins` - For logging new members
   - `Verified Members` - Master list of verified Discord IDs
3. In the `Verified Members` table, create a field called "Discord ID"

### Google Sheets Setup
1. Create a new Google Spreadsheet
2. Create two sheets:
   - `Member Joins` - For logging new members
   - `Verified Members` - Master list of verified Discord IDs
3. Place Discord IDs in column A of the `Verified Members` sheet
4. Set up service account and download `service-account.json`

## Usage

1. Start the bot:
```bash
python discord_bot/bot.py
```

2. Available Commands:
   - `!sync_verified` - Admin only command to sync verification roles with the master list

## Bot Behavior

- Automatically logs all new members joining the server
- Checks new members against the verified list
- Automatically assigns/removes verified roles based on the master list
- Provides detailed console logging for tracking operations
- Handles errors gracefully with try-catch blocks

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## Error Handling

The bot includes error handling for:
- Database connection issues
- Discord API errors
- Invalid permissions
- Missing environment variables

## Security Notes

- Keep your `.env` file secure and never commit it to version control
- Regularly rotate your API keys
- Use minimum required permissions for your Discord bot
- Keep your `service-account.json` secure if using Google Sheets

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, please:
1. Check the existing issues
2. Create a new issue with a detailed description
3. Include any relevant error messages or screenshots

## Acknowledgments

- Discord.py documentation
- Airtable API documentation
- Google Sheets API documentation
