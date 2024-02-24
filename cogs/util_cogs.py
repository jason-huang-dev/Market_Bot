from discord.ext import commands
import discord
import requests
import settings
    
class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount: str="all"):
        """Clears the chat for an optional number of messages"""
        if amount.lower() == "all":
            await ctx.channel.purge(limit=None)
        else:
            try:
                amount = int(amount)
                await ctx.channel.purge(limit=amount)
            except ValueError:
                await ctx.send("Invalid amount. Please provide a number or 'all'.")    
        
async def setup(bot):
    await bot.add_cog(Utils(bot))
