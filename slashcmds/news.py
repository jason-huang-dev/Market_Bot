from GoogleNews import GoogleNews
from GoogleNews import GoogleNews
from newspaper import Article, ArticleException
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
    @app_commands.rename(search_key = "search_topic")
    @app_commands.describe(period = "peroid to date of search (<number><d,y,w,m>), d:day, y:year, m:month, w:week")
    @app_commands.rename(period = "period")
    @app_commands.describe(start = "start date to search mm/dd/yyyy")
    @app_commands.rename(start = "start_date")
    @app_commands.describe(end = "end date to search mm/dd/yyyy")
    @app_commands.rename(end = "end_date")
    async def news(self, interaction: discord.Interaction, search_key: str, period: str="", start: str="", end: str=""):
        message = ""
        #General set up of 403 unauthorized client
        nltk.download('punkt')
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36'
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
            try:
                article = Article(articles['link'][i], config=config)
                article.download()
                article.parse()
                article.nlp()
                message += "Title: " + article.title + "\n"
                message += "\t\tLink: " + articles["link"] + "\n"
                message += "\t\tMedia: " + articles["media"][i] + "\t\tDate: " + articles["date"][i] + "\n"
                message += "\t\tSummary:\n" + article.summary + "\n"
            except ArticleException as e:
                # Handle the exception (e.g., log the error or skip the article)
                print(f"Failed to process article: {e}")            
        await interaction.response.send_message(message)

async def setup(bot):
    bot.tree.add_command(News(name="news", description="General News Functions"))