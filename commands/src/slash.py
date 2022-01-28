

import nextcord

from nextcord import Interaction
from nextcord.ext import commands
from nextcord.abc import GuildChannel

class Slash(commands.Cog):

  def __init__(self, bot):
    self.client = bot

  @nextcord.slash_command(guild_ids=[647960154079232041])
  async def pong(self, interaction : Interaction):
    await interaction.response.send_message("pong")



def setup(bot):
  bot.add_cog(Slash(bot))

