import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from aternos import starter
import time

class ButtonView(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.button(label="start", style=discord.ButtonStyle.green)
    async def starter(self, int: discord.Interaction, item: discord.ui.Button):
        #starter()
        await int.response.defer()
        channel = client.get_channel(open("channel.txt", "r").read())
        await channel.send(f"Server Starting!", delete_after=10)


load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    id = open("channel.txt", "r").read()
    channel = client.get_channel(int(id))
    await channel.send(f"Bot is online!")


@client.event
async def on_message(message):
    id = open("channel.txt", "r").read()
    channel = client.get_channel(int(id))
    if message.author == client.user:
        return
    if (message.content.startswith('$starter') and (message.channel.id == int(id))) :
        await message.delete()
        await channel.send(view=ButtonView())
        await ButtonView().wait()
    if (message.content.startswith('$starter') and (message.channel.id != int(id))) :
        await message.delete()
        await message.channel.send("You can't use this command <#{channel}>")
    if message.content.startswith('$setchannel'):
        if message.author.guild_permissions.administrator:
            if(len(message.content.split(" ")) == 2):
                channel = message.content.split(" ")[1][2:-1]
                open("channel.txt", "w").write(channel)
                await message.channel.send(f"Channel set to <#{channel}>")
            else:
                open("channel.txt", "w").write(message.channel.id.__str__())
                channel = message.channel.id
                await message.channel.send(f"Channel set to <#{channel}>")


client.run(TOKEN)
