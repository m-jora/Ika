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

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #obtains bot token from .env file

def get_prefix(bot, msg):
  with open('json/prefix.json', 'r') as f:
    prefixes = json.load(f)

  return prefixes[str(msg.guild.id)]


bot = commands.Bot(command_prefix = get_prefix)
bot.remove_command('help')


@bot.command() # live load cogs
async def load(ctx, extension):
  if ctx.author.id != 275065846836101120:
    await ctx.message.add_reaction('👎')
    return
  else:
    await ctx.message.add_reaction('👍')
    bot.load_extension(f'commands.{extension}')


@bot.command() # live unload cogs
async def unload(ctx, extension):
  if ctx.author.id != 275065846836101120:
    await ctx.message.add_reaction('👎')
    return
  
  else:
    await ctx.message.add_reaction('👍')
    bot.unload_extension(f'commands.{extension}')


@bot.command()
async def reload(ctx, extension = ''):
  if ctx.author.id != 275065846836101120:
    await ctx.message.add_reaction('👎')
    return
  
  #reloads all cogs if no extension is spefically given
  elif extension == '':
    for filename in os.listdir('./commands/mal'):
      if filename.endswith('.py'):
        bot.reload_extension(f'commands.mal.{filename[:-3]}')

    for filename in os.listdir('./commands/misc'):
      if filename.endswith('.py'):
        bot.reload_extension(f'commands.misc.{filename[:-3]}')

    for filename in os.listdir('./commands/mod'):
      if filename.endswith('.py'):
        bot.reload_extension(f'commands.mod.{filename[:-3]}')

    for filename in os.listdir('./commands/start'):
      if filename.endswith('.py'):
        bot.reload_extension(f'commands.start.{filename[:-3]}')
    
    await ctx.message.add_reaction('👍')


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
