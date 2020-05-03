# bot.py
# driver for the bot
# is the brains of this whole operation

import os
import sys
import random
import discord
import urllib.request

from discord.ext import commands

from dotenv import load_dotenv
sys.path.insert(1, 'commands/misc/') #includes my other files in the path
sys.path.insert(1, 'commands/mod/')
sys.path.insert(1, 'commands/roles/')


import mb #mr. bot.py files contains commands
import mod #mod.py files contains moderation commands
import hlp #help.py files containing custom help command


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #obtains bot token from .env file

#client = discord.Client()
bot = commands.Bot(command_prefix='~')
bot.remove_command('help')

@bot.event # messages when the bot is ready lists servers it is
async def on_ready():
  print(f'{bot.user} connected')
  print(f'{bot.user.name} is connected to the following servers:\n')

  for guild in bot.guilds:
    print(f'  {guild.name} (id: {guild.id})')
  
  await bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Becoming More Powerful'))

@bot.event # does not allow messages from bots
async def on_message(msg):
  if msg.author.bot:
    return
  await bot.process_commands(msg)



#add cogs to clean up driver
@bot.command()
async def pizza(ctx):
  await mb.pizza(ctx)

@bot.command()
async def ping(ctx):
  await ctx.send(f'`pong`')

@bot.command()
async def pong(ctx):
  await ctx.send('`ping`')

@bot.command()
async def banjo(ctx):
  await mb.banjo(ctx)

@bot.command(aliases = ['Hi', 'hello', 'Hello'])
async def hi(ctx):
  await mb.hello(ctx)

@bot.command(name = '8ball')
async def _8ball(ctx, *, question = ''):
  await mb._8ball(ctx, question)

@bot.command()
async def flip(ctx):
  await mb.flip(ctx)

@bot.command()
async def clear(ctx, amount = 2):
  await mod.clear(ctx, amount)

@bot.command()
async def kick(ctx, member : discord.member, *, reason = None):
  await mod.kick(ctx, member, reason)

@bot.command()
async def ban(ctx, member : discord.member, *, reason = None):
  await mod.ban(ctx, member, reason)

@bot.command()
async def unban(ctx, *, member):
  await mod.unban(ctx, member)

@bot.command(aliases = ['puppy', 'doggo', 'pup', 'pupper', 'hound', 'mutt'])
async def dog(ctx):
  await mb.dog(ctx)

@bot.command(aliases = ['kitty', 'kitten'])
async def cat(ctx):
  await mb.cat(ctx)

@bot.command()
async def say(ctx, *, message):
  await ctx.send(message)

@bot.command()
async def help(ctx, message = ''):
  await hlp.help(ctx, message)

@bot.command()
async def mathfun(ctx, message = ''):
  await mb.mathfun(ctx, message)

bot.run(TOKEN)


#random myanimelist anime link