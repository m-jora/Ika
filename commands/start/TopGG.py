# top.py
# handles updating server count on top.gg

import dbl
import discord

from discord.ext import commands

class TopGG(commands.Cog):

  def __init__(self, bot):
    self.client = bot
    self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjcwNTY4Mzg5NTA1NTY3OTUyMSIsImJvdCI6dHJ1ZSwiaWF0IjoxNTkwNjUwODI4fQ.VcWawdFMrb3VRwb5rb-n_pqgc_UrGZUnAfelE4kyGoE'
    self.dblpy = dbl.DBLClient(self.bot, self.token, autopost = True) 
    # automatically updates server info on tog.gg website

    async def on_guild_post():
      print("Server count posted successfully")


def setup(bot):
  bot.add_cog(TopGG(bot))


