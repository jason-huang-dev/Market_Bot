from discord.ext import commands
import discord
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
        for cog_file in settings.COGS_DIR.glob("*.py"):
            if cog_file.name != "__init__.py":
                await bot.load_extension(f"cogs.{cog_file.name[:-3]}")
        print("_"*50)    
        logger.info(f"\nMarket Bot is ready\nUser: {bot.user} (ID: {bot.user.id})")
        print("_"*50)    

    @bot.command()
    async def reload(ctx, cog : str):
        """Reloads a specified cog file <singular groupname>_cogs"""
        await bot.reload_extension(f"cogs.{cog.lower()}")
    @bot.command()
    async def load(ctx, cog : str):
        """Loads a specified cog file <singular groupname>_cogs"""
        await bot.load_extension(f"cogs.{cog.lower()}")
    @bot.command()
    async def unload(ctx, cog : str):
        """Unloads a specified cog file <singular groupname>_cogs"""
        await bot.unload_extension(f"cogs.{cog.lower()}")

    bot.run(settings.SECRET_BOT_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()