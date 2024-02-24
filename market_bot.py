from discord.ext import commands
import discord
import requests
import settings

logger = settings.logging.getLogger("market_bot_log")
    
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
        aliases=['ticks'],
        name = 'tickers',
        help = 'Reports Ticker Information Given Stream of Tickers'
    )
    async def tickers(ctx, *tickers):
        for ticker in tickers:
            print(ticker)
            url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={settings.SECRET_ALPHA_VINTAGE_KEY}'
            response = requests.get(url)
            data = response.json()
            if 'Global Quote' in data:
                stock_data = data['Global Quote']
                symbol = stock_data['01. symbol']
                open = float(stock_data['02. open'])
                high = float(stock_data['03. high'])
                low = float(stock_data['04. low'])
                price = stock_data['05. price']
                volume = stock_data['06. volume']
                latest_trade_day = stock_data['07. latest trading day']
                previous_close = stock_data['08. previous close']
                change = stock_data['09. change']
                percent_change = stock_data['10. change percent']
                await ctx.send(f'Stock: {symbol}, Price: {price}')
            else:
                await ctx.send(f'Could not find information for {ticker}')

    @bot.command()
    async def clear(ctx, amount="all"):
        """Clears the chat for an optional number of messages"""
        if amount.lower() == "all":
            await ctx.channel.purge(limit=None)
        else:
            try:
                amount = int(amount)
                await ctx.channel.purge(limit=amount)
            except ValueError:
                await ctx.send("Invalid amount. Please provide a number or 'all'.")    
    



    bot.run(settings.SECRET_BOT_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()