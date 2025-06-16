# Sample code from the documentation
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_CHANNEL = int(os.getenv('DISCORD_CHANNEL'))

import discord

import time

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    channel = client.get_channel(DISCORD_CHANNEL)
    await channel.send('dit is een test')

client.run(DISCORD_TOKEN)
