import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from airtable_handler import AirtableHandler
# or from sheets_handler import GoogleSheetsHandler

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('DISCORD_GUILD_ID'))
VERIFIED_ROLE_ID = int(os.getenv('VERIFIED_ROLE_ID'))

class MemberTrackingBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True  # Enable member tracking
        super().__init__(command_prefix='!', intents=intents)
        
        # Initialize database handler
        self.db_handler = AirtableHandler()  # or GoogleSheetsHandler()
        
    async def setup_hook(self):
        print(f'Logged in as {self.user}')
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Handle new member joins"""
        if member.guild.id != GUILD_ID:
            return
            
        # Log the new member
        await self.log_new_member(member)
        
        # Check if member is in verified list
        if await self.verify_member(member):
            await self.assign_verified_role(member)
        
    async def log_new_member(self, member):
        """Log member details to Airtable/Sheets"""
        member_data = {
            'user_id': str(member.id),
            'username': member.name,
            'discriminator': member.discriminator,
            'joined_at': member.joined_at.isoformat(),
            'created_at': member.created_at.isoformat(),
            'is_bot': member.bot
        }
        
        await self.db_handler.log_member(member_data)
        
    async def verify_member(self, member):
        """Check if member is in verified list"""
        return await self.db_handler.is_verified(str(member.id))
        
    async def assign_verified_role(self, member):
        """Assign verified role to member"""
        verified_role = member.guild.get_role(VERIFIED_ROLE_ID)
        if verified_role:
            await member.add_roles(verified_role)
            print(f"Assigned verified role to {member.name}")

bot = MemberTrackingBot()

@bot.command()
@commands.has_permissions(administrator=True)
async def sync_verified(ctx):
    """Sync verified roles with master list"""
    guild = ctx.guild
    verified_role = guild.get_role(VERIFIED_ROLE_ID)
    
    if not verified_role:
        await ctx.send("Verified role not found!")
        return
        
    members = guild.members
    for member in members:
        if await bot.verify_member(member):
            if verified_role not in member.roles:
                await member.add_roles(verified_role)
                await ctx.send(f"Added verified role to {member.name}")
        else:
            if verified_role in member.roles:
                await member.remove_roles(verified_role)
                await ctx.send(f"Removed verified role from {member.name}")
                
    await ctx.send("Verification sync complete!")

if __name__ == "__main__":
    bot.run(TOKEN) 