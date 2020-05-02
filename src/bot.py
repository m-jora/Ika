#bot.py

import os
import sys
import random

from discord.ext import commands

from dotenv import load_dotenv
sys.path.insert(1, 'commands/misc/')
sys.path.insert(1, 'commands/mod/')
sys.path.insert(1, 'commands/roles/')


import db


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client()
bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
  print(f'{bot.user} connected')
  print(f'{bot.user.name} is connected to the following servers:\n')

  for guild in bot.guilds:
    print(f'  {guild.name} (id: {guild.id})')


@bot.command(name='pizza')
async def words(ctx):
  await db.rad(ctx)

@bot.command(name='ping')
async def words(ctx):
  await db.ping(ctx)

@bot.command(name='pong')
async def words(ctx):
  await db.pong(ctx)

@bot.command(name = 'banjo')
async def words(ctx):
  await db.banjo(ctx)

@bot.command(name = 'evan', help = 'Pings Evan')
async def words(ctx):
  await db.evan(ctx)

@bot.command(name = 'hi')
async def words(ctx):
  await db.hello(ctx)

'''@bot.command(name = 'dog')
async def words(ctx):
  await db.dog(ctx)
'''
bot.run(TOKEN)


#random myanimelist anime link