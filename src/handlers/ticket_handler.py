import discord
from discord import Interaction, PermissionOverwrite, ButtonStyle
from discord.ui import Button, View

async def send_ticket_panel(interaction: Interaction):
    class OpenTicket(View):
        def __init__(self):
            super().__init__(timeout=None)

        @discord.ui.button(label="🎫 فتح تذكرة", style=ButtonStyle.primary)
        async def open(self, interaction2: Interaction, button: Button):
            await create_ticket(interaction2)

    await interaction.response.send_message(
        "اضغط على الزر لفتح تذكرة جديدة:",
        view=OpenTicket()
    )

async def create_ticket(interaction: Interaction):
    guild = interaction.guild

    overwrites = {
        guild.default_role: PermissionOverwrite(view_channel=False),
        interaction.user: PermissionOverwrite(view_channel=True, send_messages=True)
    }

    channel = await guild.create_text_channel(
        name=f"ticket-{interaction.user.name}",
        overwrites=overwrites
    )

    class CloseTicket(View):
        def __init__(self):
            super().__init__(timeout=None)

        @discord.ui.button(label="🔒 إغلاق التذكرة", style=ButtonStyle.danger)
        async def close(self, interaction2: Interaction, button: Button):
            await interaction2.channel.send("سيتم إغلاق التذكرة خلال 5 ثوانٍ...")
            await interaction2.channel.delete(delay=5)

    await channel.send(
        f"مرحبًا {interaction.user.mention}، سيتم خدمتك قريبًا.",
        view=CloseTicket()
    )

    await interaction.response.send_message(
        f"تم فتح تذكرتك: {channel.mention}",
        ephemeral=True
    )
