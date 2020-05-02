#bot.py

import os
import sys
#import discord
import random

from discord.ext import commands

from dotenv import load_dotenv
sys.path.insert(1, 'commands/misc/')
sys.path.insert(1, 'commands/mod/')
sys.path.insert(1, 'commands/roles/')

import messages


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client()
bot = commands.Bot(command_prefix='db.')

@bot.event
async def on_ready():
  print(f'{bot.user} connected')
  print(f'{bot.user.name} is connected to the following servers:\n')

  for guild in bot.guilds:
    print(f'  {guild.name} (id: {guild.id})')


@bot.command(name='pizza')
async def words(ctx):
  lit = ['Hi Kendall', 'Pizza', 'Howdy Partner',]
  response = random.choice(lit)
  await ctx.send(response)


'''@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  await messages.on_message(message)
'''

bot.run(TOKEN)