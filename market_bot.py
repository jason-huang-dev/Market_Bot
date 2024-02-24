from discord.ext import commands
import discord
import requests
from ..constants import  *

intents = discord.Intents.default()
intents.message_content = True
prefix = '/'

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@bot.event
async def on_ready():
    channel = bot.get_channel(MARKET_CHANNEL_ID)
    await   print(f'Logged in as {bot.user.name}')
    
@bot.command()
async def tickers(ctx, *tickers):
     for ticker in tickers:
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={ALPHA_VINTAGE_KEY}'
        response = requests.get(url)
        data = response.json()
        if 'Global Quote' in data:
            stock_data = data['Global Quote']
            symbol = stock_data['01. symbol']
            price = stock_data['05. price']
            await ctx.send(f'Stock: {symbol}, Price: {price}')
        else:
            await ctx.send(f'Could not find information for {ticker}')

bot.run(BOT_TOKEN)