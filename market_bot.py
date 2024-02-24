from discord.ext import commands
import discord
import requests
import settings

logger = settings.logging.getLogger("market_bot_log")

class TickerList(commands.Converter):
    async def convert(self, ctx, stream):
        print(stream)
        for ticker in stream:
            print(ticker)
        return [ticker.upper() for ticker in stream if ticker.isalpha()]    
    
def run():
    intents = discord.Intents.all()
    intents.message_content = True
    prefix = '/'
    bot = commands.Bot(command_prefix=prefix, intents=intents)
    @bot.event
    async def on_ready():
        channel = bot.get_channel(settings.SECRET_MARKET_CHANNEL_ID)
        logger.info(f"\nMarket Bot is ready\nUser: {bot.user} (ID: {bot.user.id})")
        print("_"*50)
    
    @bot.command(
        alias = ['tick'],
        name = 'tickers',
        help = 'Reports Ticker Information Given Stream of Tickers'
    )
    async def tickers(ctx, *tickers: TickerList):
        for ticker in tickers:
            print(f"{ticker}\n")
            url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={settings.SECRET_ALPHA_VINTAGE_KEY}'
            response = requests.get(url)
            data = response.json()
            if 'Global Quote' in data:
                stock_data = data['Global Quote']
                symbol = stock_data['01. symbol']
                price = stock_data['05. price']
                await ctx.send(f'Stock: {symbol}, Price: {price}')
            else:
                await ctx.send(f'Could not find information for {ticker}')

    @bot.command()
    async def clear(ctx):
        """Clears the chat"""
        await ctx.channel.purge(limit=20)
    
    bot.run(settings.SECRET_BOT_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()