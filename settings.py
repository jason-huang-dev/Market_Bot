import os
import logging
from logging.config import dictConfig
from dotenv import load_dotenv

load_dotenv()
SECRET_BOT_TOKEN = os.getenv("BOT_TOKEN")
SECRET_MARKET_CHANNEL_ID = os.getenv("MARKET_CHANNEL_ID")
SECRET_ALPHA_VINTAGE_KEY = os.getenv("ALPHA_VINTAGE_KEY")

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose":{
            "format": "%(levelname)-5s - %(asctime)s - %(module)-10s - %(message)s"
        },
        "standard":{
            "format": "%(levelname)-5s - %(name)-10s - %(message)s"
        }
    },
    "handlers":{
        "console":{
            "level":"DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "console2": {
            "level":"WARNING",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "file":{
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "Logs/infos.log",
            "mode": "w",
            "formatter": "verbose",
        }
    },
    "loggers":{
        "market_bot_log": {
            "handlers": ["console"], 
            "level": "INFO",
            "propagate": False
        },
        "discord":{
            'handlers': ['console2', "file"],
            "level":"INFO",
            "propagate": False
        }
    }
}
dictConfig(LOGGING_CONFIG)