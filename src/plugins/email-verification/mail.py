import discord 
from discord.ext import commands





class EmailSetupCog(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot 
        
    
    @commands.hybrid_command(name="setup_email_verification")
    async def setup_email_verification(self, ctx : commands.Context) -> None:
        """Setup email verification for your server"""
        
        await ctx.send("Hello world")
        
        
        
async def setup(bot : commands.Bot) -> None:
    await bot.add_cog(EmailSetupCog(bot))
    print("Loaded email setup cog")
    
