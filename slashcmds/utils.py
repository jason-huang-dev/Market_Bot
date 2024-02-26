from discord import app_commands
import discord
    
class Utils(app_commands.Group):
    @app_commands.command(
        name = 'clear',
        description="Clears the chat for an optional number of messages (clear all if no number is passed through)"
    )
    @app_commands.describe(amount = "number of messages you want to purge from chat (no value means all)")
    @app_commands.rename(amount = "amount")
    async def clear(self, interaction: discord.Interaction, amount: str=None):
        if amount == None:
            await interaction.channel.purge(limit=None)
        else:
            try:
                amount = int(amount)
                await interaction.channel.purge(limit=amount)
            except ValueError:
                await interaction.response.send_message("Invalid amount. Please provide a number or 'all'.")    
        
async def setup(bot):
    bot.tree.add_command(Utils(name="utils", description="General Utilities"))
