# bot.py
# driver for the bot
# is the brains of this whole operation

import os
import sys
import random, json
import discord
import aiohttp

from discord.ext import commands

from dotenv import load_dotenv
'''sys.path.insert(1, 'commands/misc/') #includes my other files in the path
sys.path.insert(1, 'commands/mod/')
sys.path.insert(1, 'commands/roles/')
sys.path.insert(1, 'commands/mal/')
sys.path.insert(1, 'commands/old/')'''


#import mb #mr. bot.py files contains commands
#import mod #mod.py files contains moderation commands
#import hlp #help.py files containing custom help command
#import anime #anime.py files containing jikan mal api

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #obtains bot token from .env file

def get_prefix(bot, msg):
  with open('json/prefix.json', 'r') as f:
    prefixes = json.load(f)

  return prefixes[str(msg.guild.id)]


#client = discord.Client()
bot = commands.Bot(command_prefix = get_prefix)
bot.remove_command('help')

'''
@bot.event # prints Command not Found to console if given command does not exist
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    print('CNF')
  else:
    print(error)'''


@bot.command()
async def load(ctx, extension):
  if ctx.author.id != 275065846836101120:
    await ctx.message.add_reaction('👎')
    return
  else:
    await ctx.message.add_reaction('👍')
    bot.load_extension(f'commands.{extension}')


@bot.command()
async def unload(ctx, extension):
  if ctx.author.id != 275065846836101120:
    await ctx.message.add_reaction('👎')
    return
  
  else:
    await ctx.message.add_reaction('👍')
    bot.unload_extension(f'commands.{extension}')


@bot.command()
async def reload(ctx, extension):
  if ctx.author.id != 275065846836101120:
    await ctx.message.add_reaction('👎')
    return
  
  else:
    await ctx.message.add_reaction('👍')
    bot.reload_extension(f'commands.{extension}')



#Load all cogs when bot starts
for filename in os.listdir('./commands/mal'):
  if filename.endswith('.py'):
    bot.load_extension(f'commands.mal.{filename[:-3]}')

for filename in os.listdir('./commands/misc'):
  if filename.endswith('.py'):
    bot.load_extension(f'commands.misc.{filename[:-3]}')

for filename in os.listdir('./commands/mod'):
  if filename.endswith('.py'):
    bot.load_extension(f'commands.mod.{filename[:-3]}')

for filename in os.listdir('./commands/start'):
  if filename.endswith('.py'):
    bot.load_extension(f'commands.start.{filename[:-3]}')


bot.run(TOKEN)
