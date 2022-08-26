# event.py
# event handlers from main
import random
import json
import discord
import asyncio

from discord.ext import commands

class event(commands.Cog):

  def __init__(self, bot):
    self.client = bot

  
  @commands.Cog.listener()
  async def on_ready(self):
    anime = [
        'Steins;Gate','Mirai Nikki',
        'BEASTARS','Kiznaiver',
        'Fire Force','Anohana',
        'Your Name','MHA',
        'FMAB','AoT','NGNL',
        'Re:Zero','Ditf',
        'BNA','Charlotte',
        'Soul Eater','Danmachi'
      ]

    print(f'{self.client.user} connected')
    await self.client.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.watching, name = f'{random.choice(anime)} // m.help'))

  

  '''@commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandNotFound):
      print('CNF')
    else:
      print(error)
      await ctx.message.add_reaction('⚠️')'''



def setup(bot):
  bot.add_cog(event(bot))