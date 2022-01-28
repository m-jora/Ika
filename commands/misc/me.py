# me.py
# commands that were designed only for me or only work for me currently

import nextcord
import random

from nextcord import Interaction
from nextcord.ext import commands

class me(commands.Cog):

  def __init__(self, bot):
    self.client = bot


  @nextcord.slash_command(guild_ids=[647960154079232041], force_global=True)
  async def restatus(self, interaction : Interaction):
    if interaction.user.id == 275065846836101120:
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

      await interaction.response.send_message('👍')
      await self.client.change_presence(status = nextcord.Status.online, activity = nextcord.Activity(type = nextcord.ActivityType.watching, name = f'{random.choice(anime)} // m:help'))
            

  @commands.command()
  async def eval(self, ctx, *, msg,):
    if ctx.author.id == 275065846836101120:
      await ctx.send(eval(msg))


def setup(bot):
  bot.add_cog(me(bot))