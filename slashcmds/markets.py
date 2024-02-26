import discord
from discord import app_commands
import requests
import settings
    
class Markets(app_commands.Group):    
    @app_commands.command(
        name = 'tickers',
        description="Reports Ticker Information Given Stream of Tickers"
    )
    async def tickers(self, interaction: discord.Interaction):
        for ticker in interaction.data:
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
                await interaction.response.send_message(f'Stock: {symbol}, Price: {price}')
            else:
                await interaction.response.send_message(f'Could not find information for {ticker}')

async def setup(bot):
    bot.tree.add_command(Markets(name="markets", description="General Market Functions"))