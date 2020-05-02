#bot.py

import os
import discord

from dotenv import load_dotenv

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

  if 'happy birthday' in message.content.lower():
    await message.channel.send('Happy Birthday! 🎈🎈')

  if 'dang it jesse' in message.content.lower():
    await message.channel.send('DANG IT JESSE!')

  if 'hello' in message.content:
    await message.channel.send('Howdy')

  if 'hi mr. bot' in message.content.lower():
    await message.channel.send('How are you?')

  


client.run(TOKEN)