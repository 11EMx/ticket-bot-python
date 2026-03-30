import discord
from discord import app_commands
from discord.ext import commands

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ticket", description="فتح تذكرة جديدة")
    async def ticket(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "تم فتح تذكرة (مثال بسيط)!", 
            ephemeral=True
        )

async def setup(bot: commands.Bot):
    await bot.add_cog(Ticket(bot))
