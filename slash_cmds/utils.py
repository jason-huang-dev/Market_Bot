from discord import app_commands
import discord
    
class Utils(app_commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def clear(self, interaction: discord.Interaction, amount: str="all"):
        """Clears the chat for an optional number of messages"""
        if amount.lower() == "all":
            await interaction.channel.purge(limit=None)
        else:
            try:
                amount = int(amount)
                await interaction.channel.purge(limit=amount)
            except ValueError:
                await interaction.response.send_message("Invalid amount. Please provide a number or 'all'.")    
        
async def setup(bot):
    await bot.tree.add_command(Utils(name="utils"))
