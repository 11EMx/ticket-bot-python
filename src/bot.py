import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

# تحميل المتغيرات من البيئة (محليًا فقط، في Railway يستخدم Variables)
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

async def load_extensions():
    # تحميل كوج التذاكر
    await bot.load_extension("src.commands.ticket")

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

    # مزامنة Slash Commands
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} application commands.")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")

def run_bot():
    token = os.getenv("MTQ4ODIyNDk0MTgyNzQyNDM4Nw.GM6Zs3.0dsYtHqi9qpAj4dB9cYBVKxJ36a7ihJs61Kii0")
    if not token:
        raise ValueError("DISCORD_TOKEN is not set in environment variables.")

    async def main():
        await load_extensions()
        await bot.start(token)

    asyncio.run(main())
