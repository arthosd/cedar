"""
This script is used to gather all the data from all the needed sources.
For now we only have crawlers data.

Process :
--------
    1- Run the crawlers to gather all articles from the web
    2- Adding all the RAW data in MongoDB
"""
from app.Bots.scheduler import start_process

from app.Bots.bots.MatterBot import MatterBot
from app.Bots.bots.GlobalForestBot import GlobalForestBot

start_process([
    GlobalForestBot,
    MatterBot
])