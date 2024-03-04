from GoogleNews import GoogleNews
from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
import nltk
import pandas as pd
import discord
from discord import app_commands

class News(app_commands.Group):  
    @app_commands.command(
        name = 'news',
        description="Reports News Information in the past predefined period or start-end period Given a Search Key"
    )
    @app_commands.describe(search_key = "topic that you want news for")
    @app_commands.rename(search_key = "search topic")
    async def news(self, interaction: discord.Interaction, search_key: str, period: str="", start: str="", end: str=""):
        message = ""
        #General set up of 403 unauthorized client
        nltk.download('punkt')
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        config = Config()
        config.browser_user_agent = user_agent

        #Gets/Setsup everything from Google News
        gNews = GoogleNews(period=period, start=start, end=end) # set up google news with given time frame
        gNews.search(search_key) # search for given key
        result  = gNews.results(sort=True) # get results and sorts it 
        articles = pd.DataFrame(result)
        articles.drop(columns=["img"])
        articles.head()

        #Iterates through n pages of the goolge new results
        for i in range(2,5):
            gNews.getpage(i)
            result=gNews.result()
            articles=pd.DataFrame(result)

        for i in articles.index:
            article = Article(articles['link'][i],config=config)
            article.download()
            article.parse()
            article.nlp()
            message += "Title: " + article.title + "\n"
            message += "\t\tLink: " + articles["link"] + "\n"
            message += "\t\tMedia: " + articles["media"][i] + "\t\tDate: " + articles["date"][i] + "\n"

        
        await interaction.response.send_message(f'Could not find information for {search_key}')
        await interaction.response.send_message(message)

async def setup(bot):
    bot.tree.add_command(News(name="news", description="General News Functions"))