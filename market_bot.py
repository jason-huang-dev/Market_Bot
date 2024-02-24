from discord.ext import commands
import discord
from dataclasses import dataclass
from ..constants import  *

intents = discord.Intents.default()
intents.message_content = True
prefix = '/'

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
client = discord.Client()

@bot.event
async def on_ready():
    channel = bot.get_channel(MARKET_CHANNEL_ID)
    await   print(f'Logged in as {bot.user.name}')
    
@bot.command()
async def add(ctx, *arr):
    result = 0
    for num in arr:
        result += num
    await ctx.send(f"Result = {result}")

bot.run(BOT_TOKEN)