from discord import app_commands, Interaction
from discord.ext import commands
from src.handlers.ticket_handler import send_ticket_panel

def setup(bot: commands.Bot):

    @bot.tree.command(name="ticket", description="إظهار لوحة فتح التذاكر")
    async def ticket(interaction: Interaction):
        await send_ticket_panel(interaction)

    @bot.event
    async def on_ready():
        guild = bot.get_guild(int(bot.guilds[0].id))
        await bot.tree.sync(guild=guild)
        print("Slash commands synced.")
