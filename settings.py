from pathlib import Path
import os
import logging
from logging.config import dictConfig
from dotenv import load_dotenv
import discord

BASE_DIR = Path(__file__).parent
load_dotenv(override=True)
SECRET_BOT_TOKEN = os.getenv("BOT_TOKEN")
SECRET_MARKET_CHANNEL_ID = os.getenv("MARKET_CHANNEL_ID")
SECRET_ALPHA_VINTAGE_KEY = os.getenv("ALPHA_VINTAGE_KEY")
SECRET_GUILD_ID = discord.Object(id=int(os.getenv("GUILD_ID")))

# Make this a directory, not a file path
LOG_DIR = BASE_DIR / "Logs"
LOG_FILE = LOG_DIR / "infos.log"

SLASH_CMDS_DIR = BASE_DIR / "slashcmds"

# Check if running on Render (you can set an env var on Render)
ON_RENDER = os.getenv("RENDER", None) is not None

# Create Logs directory only if not on Render
if not ON_RENDER:
    LOG_DIR.mkdir(parents=True, exist_ok=True)

# Base handlers always have console
handlers = {
    "console": {
        "level": "DEBUG",
        "class": "logging.StreamHandler",
        "formatter": "standard",
    },
    "console2": {
        "level": "WARNING",
        "class": "logging.StreamHandler",
        "formatter": "standard",
    },
}

# Add file handler only if not on Render and log directory exists
if not ON_RENDER and LOG_DIR.exists():
    handlers["file"] = {
        "level": "INFO",
        "class": "logging.FileHandler",
        "filename": str(LOG_FILE),
        "mode": "w",
        "formatter": "verbose",
    }

# Assign handlers per logger, omit 'file' on Render
loggers = {
    "market_bot_log": {
        "handlers": ["console"],
        "level": "INFO",
        "propagate": False,
    },
    "discord": {
        "handlers": ["console2"] + (["file"] if "file" in handlers else []),
        "level": "INFO",
        "propagate": False,
    },
}

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)-5s - %(asctime)s - %(module)-10s - %(message)s",
        },
        "standard": {
            "format": "%(levelname)-5s - %(name)-10s - %(message)s",
        },
    },
    "handlers": handlers,
    "loggers": loggers,
}

dictConfig(LOGGING_CONFIG)
