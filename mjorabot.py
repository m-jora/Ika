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
  print(f'{client.user.name} is connected to the following servers:')



  for guild in client.guilds:
    print(f'{guild.name} (id: {guild.id})')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content=='hello':
    await message.channel.send('Howdy')


client.run(TOKEN)