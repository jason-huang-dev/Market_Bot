import discord
from discord import app_commands
import requests
import settings
    
class Markets(app_commands.Group):    
    @app_commands.command(
        name = 'tickers',
        description="Reports Ticker Information Given Stream of Tickers"
    )
    @app_commands.describe(tickers_list = "list of space separated tickers that you want to look up")
    @app_commands.rename(tickers_list = "tickers")
    async def tickers(self, interaction: discord.Interaction, tickers_list: str):
        message = ""
        for ticker in tickers_list.split(" "):
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
                message += str(f'Stock: {symbol}, Price: {price}\n')
            else:
                await interaction.response.send_message(f'Could not find information for {ticker}')
        await interaction.response.send_message(message)

async def setup(bot):
    bot.tree.add_command(Markets(name="markets", description="General Market Functions"))