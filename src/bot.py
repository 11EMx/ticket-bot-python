import os
from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv

load_dotenv()

def run_bot():
    intents = Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    # تحميل أوامر التذاكر
    from src.commands.ticket import setup as ticket_setup
    ticket_setup(bot)

    bot.run(os.getenv("DISCORD_TOKEN"))
