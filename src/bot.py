# bot.py
# driver for the bot
# is the brains of this whole operation

import os
import sys
import random
import discord

from discord.ext import commands

from dotenv import load_dotenv
sys.path.insert(1, 'commands/misc/') #includes my other files in the path
sys.path.insert(1, 'commands/mod/')
sys.path.insert(1, 'commands/roles/')


import mb #mr. bot.py files contains commands
import mod #mod.py files contains moderation commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #obtains bot token from .env file

#client = discord.Client()
bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
  print(f'{bot.user} connected')
  print(f'{bot.user.name} is connected to the following servers:\n')

  for guild in bot.guilds:
    print(f'  {guild.name} (id: {guild.id})')
  
  await bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Becoming More Powerful'))

#add cogs to clean up driver
@bot.command(help = 'it does something idk')
async def pizza(ctx):
  await mb.pizza(ctx)

@bot.command(help = 'pong')
async def ping(ctx):
  await ctx.send(f'`pong`')

@bot.command(help = 'ping')
async def pong(ctx):
  await ctx.send('`ping`')

@bot.command(help = 'the worlds worst banjo ascii art')
async def banjo(ctx):
  await mb.banjo(ctx)

@bot.command(help = 'Pings Evan')
async def evan(ctx):
  await ctx.send('<@219202507354669057>')

@bot.command(help = 'Mr. bot says greets you')
async def hi(ctx):
  await mb.hello(ctx)

@bot.command(aliases = ['8ball', 'eightball'], help = 'Ask the magic 8ball questions')
async def _8ball(ctx, *, question = ''):
  await mb._8ball(ctx, question)

@bot.command(help = 'flip a coin')
async def flip(ctx):
  await mb.flip(ctx)

@bot.command(help = 'clears number of messages give')
async def clear(ctx, amount = 2):
  await mod.clear(ctx, amount)

@bot.command(help = 'kicks member from server if Mr. bot has the permissions')
async def kick(ctx, member : discord.member, *, reason = None):
  await mod.kick(ctx, member, reason)

@bot.command(help = 'bans member from server if Mr. bot has the permissions')
async def ban(ctx, member : discord.member, *, reason = None):
  await mod.ban(ctx, member, reason)

@bot.command(help = 'unbans member from server if Mr. bot has the permissions')
async def unban(ctx, *, member):
  await mod.unban(ctx, member)


'''@bot.command()
async def load(ctx, extension)
bot.load_extension()
'''



bot.run(TOKEN)


#random myanimelist anime link