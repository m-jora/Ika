#bot.py
import os
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user.name} connected')

'''@client.event
async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send(
    f'Howdy {member.name}, welcome to Yote INC.'
  )'''

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content=='hello':
    await message.channel.send('Howdy')

  if message.content==('yeet'):
    await message.channel.send('yee haw')

  if message.content == 'how are you':
    await message.channel.send('my life was a mistake')

  if message.content == 'joe mama':
    await message.channel.send('joE_mineR.png')

  

client.run(TOKEN)