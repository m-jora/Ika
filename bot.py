# bot.py
# driver for the bot
# is the brains of this whole operation

import os
import sys
import random, json
import discord
import aiohttp
import threading

from discord.ext import commands

from dotenv import load_dotenv

intents = discord.Intents(guilds = True, emojis = True, members = True, messages = True, reactions = True, typing = True)

load_dotenv()
TOKEN = os.getenv('BETA_TOKEN') #obtains bot token from .env file

bot = commands.Bot(command_prefix = ('m:', 'M:', '<@!712416120535253034> ', '<@!712416120535253034>'), intents = intents)
bot.remove_command('help')

# loads cogs
@bot.command()
async def load(ctx, extension):
  if ctx.author.id != 275065846836101120:
    await ctx.message.add_reaction('👎')
    return
  else:
    await ctx.message.add_reaction('👍')
    bot.load_extension(f'commands.{extension}')

# unloads cogs
@bot.command()
async def unload(ctx, extension):
  if ctx.author.id != 275065846836101120:
    await ctx.message.add_reaction('👎')
    return
  
  else:
    await ctx.message.add_reaction('👍')
    bot.unload_extension(f'commands.{extension}')

# reloads the cogs 
# ack
@bot.command()
async def reload(ctx, extension = ''):
  if ctx.author.id != 275065846836101120:
    await ctx.message.add_reaction('👎')
    return
  
  elif extension == '':
    for filename in os.listdir('./commands/general'):
      if filename.endswith('.py'):
        bot.reload_extension(f'commands.general.{filename[:-3]}')

    for filename in os.listdir('./commands/img'):
      if filename.endswith('.py'):
        bot.reload_extension(f'commands.img.{filename[:-3]}')

    for filename in os.listdir('./commands/mal_anilist'):
      if filename.endswith('.py'):
        bot.reload_extension(f'commands.mal_anilist.{filename[:-3]}')

    for filename in os.listdir('./commands/misc'):
      if filename.endswith('.py'):
        bot.reload_extension(f'commands.misc.{filename[:-3]}')

    for filename in os.listdir('./commands/src'):
      if filename.endswith('.py'):
        bot.reload_extension(f'commands.src.{filename[:-3]}')

    await ctx.message.add_reaction('👍')


  else:
    await ctx.message.add_reaction('👍')
    bot.reload_extension(f'commands.{extension}')






#Load all cogs when bot starts
for filename in os.listdir('./commands/general'):
  if filename.endswith('.py'):
    bot.load_extension(f'commands.general.{filename[:-3]}')

for filename in os.listdir('./commands/img'):
  if filename.endswith('.py'):
    bot.load_extension(f'commands.img.{filename[:-3]}')

for filename in os.listdir('./commands/mal_anilist'):
  if filename.endswith('.py'):
    bot.load_extension(f'commands.mal_anilist.{filename[:-3]}')

for filename in os.listdir('./commands/misc'):
  if filename.endswith('.py'):
    bot.load_extension(f'commands.misc.{filename[:-3]}')

for filename in os.listdir('./commands/src'):
  if filename.endswith('.py'):
    bot.load_extension(f'commands.src.{filename[:-3]}')


bot.run(TOKEN)
