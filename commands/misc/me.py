# me.py
# commands that were designed only for me or only work for me currently

import discord
import random

from discord.ext import commands

class me(commands.Cog):

  def __init__(self, bot):
    self.client = bot


  @commands.command()
  async def restatus(self, ctx):
    if ctx.author.id == 275065846836101120:
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

      await ctx.message.add_reaction('👍')
      await self.client.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.watching, name = f'{random.choice(anime)} // m:help'))
            

  @commands.command()
  async def eval(self, ctx, *, msg,):
    if ctx.author.id == 275065846836101120:
      await ctx.send(eval(msg))


def setup(bot):
  bot.add_cog(me(bot))