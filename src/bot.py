#bot.py

import os
import sys
import discord

from dotenv import load_dotenv
sys.path.insert(1, 'commands/misc/')
sys.path.insert(1, 'commands/mod/')
sys.path.insert(1, 'commands/roles/')

import messages


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} connected')
  print(f'{client.user.name} is connected to the following servers:\n')

  for guild in client.guilds:
    print(f'  {guild.name} (id: {guild.id})')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  await messages.on_message(message)


client.run(TOKEN)