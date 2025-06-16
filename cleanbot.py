# Sample code from the documentation
import os
from dotenv import load_dotenv, dotenv_values
import discord
import datetime

def get_weeknumber():
    # '%V' returns the ISO 8601 week as a decimal number 
    # with Monday as the first day of the week. 
    week_number = int(datetime.datetime.now().strftime("%V"))
    return week_number

def determine_shower_toilet(week_number):
    if (week_number % 4 == 0):
        return "Allard"
    elif (week_number % 3 == 0):
        return "Wilhelm"
    elif (week_number % 2 == 0):
        return "Jesse"
    elif (week_number % 1 == 0):
        return "Daniel"
    else:
        return "error"

def determine_nasty_toilet(week_number):
    if (week_number % 4 == 0):
        return "Wilhelm"
    elif (week_number % 3 == 0):
        return "Jesse"
    elif (week_number % 2 == 0):
        return "Daniel"
    elif (week_number % 1 == 0):
        return "Allard"
    else:
        return "error"

def determine_bathroom_R(week_number):
    if (week_number % 2 == 0):
        return "Allard"
    elif (week_number % 1 == 0):
        return "Daniel"
    else:
        return "error"

def determine_bathroom_L(week_number):
    if (week_number % 2 == 0):
        return "Jesse"
    elif (week_number % 1 == 0):
        return "Wilhelm"
    else:
        return "error"

def determine_vacuum(week_number):
    if (week_number % 4 == 0):
        return "Daniel"
    elif (week_number % 3 == 0):
        return "Allard"
    elif (week_number % 2 == 0):
        return "Wilhelm"
    elif (week_number % 1 == 0):
        return "Jesse"
    else:
        return "error"

# load local environments to keep stuff secured
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_CHANNEL = int(os.getenv('DISCORD_CHANNEL'))

# set intents (sort of permissions)
intents = discord.Intents.default()
intents.message_content = True

#create client instance
client = discord.Client(intents=intents)


week_number = get_weeknumber()

cleaning_message = f'''
=======================================
**Schoonmaakrooster voor week {week_number}!**
Toilet 1: {determine_shower_toilet(week_number)}
Toilet 2: {determine_nasty_toilet(week_number)}
Douche R: {determine_bathroom_R(week_number)}
Douche L: {determine_bathroom_L(week_number)}
Stofzuigen: {determine_vacuum(week_number)}

*good luck everyone!*
=======================================
'''


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    channel = client.get_channel(DISCORD_CHANNEL)
    await channel.send(cleaning_message)
    exit()

client.run(DISCORD_TOKEN)
