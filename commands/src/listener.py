# listener.py
# handles all different reaction listeners

import json
import nextcord
import aiohttp

from nextcord.ext import commands

class listener(commands.Cog):

  def __init__(self, bot):
    self.client = bot

  #reaction for removing embed
  @commands.Cog.listener()
  async def on_reaction_add(self, reaction, user):
    channel = reaction.message.channel

    #await channel.send(reaction.message.embeds)
    ###########################################
    ##### Need to add paging for searchs ######
    ###########################################

    if str(reaction.emoji) == '❌' and reaction.message.author.id == 712416120535253034:
      if len(reaction.message.reactions) < 3:
        return

      elif user.id != 712416120535253034 and str(reaction.message.reactions[0]) == '⬅️' and str(reaction.message.reactions[1]) == '❌' and str(reaction.message.reactions[2]) == '➡️':
        #await reaction.message.edit(delete_after = 0)
        await reaction.remove(user)
      else:
        return

    ###########################################
    ###### This ^ is for starting paging ######
    ###########################################

    elif (str(reaction.emoji) == '🐶' or str(reaction.emoji) == '🐕'):
      if user.id != 712416120535253034 and str(reaction.message.reactions[0]) == '🐶' and reaction.count > 1 and str(reaction.message.reactions[1] == '🐕'):
        with open('json/dog.json', 'r') as f:
          ids = json.load(f)

        id = ids[str(reaction.message.guild.id)]

        message = await channel.fetch_message(int(id))

        embed = nextcord.Embed(
          colour = 0xFF00FF
        )

        url = 'https://dog.ceo/api/breeds/image/random'

        async with aiohttp.ClientSession() as session:
          html = await self.fetch(session, url)
          img = html['message'] #.get('message')

        embed.set_image(url = img)

        await message.edit(embed = embed)
        await reaction.remove(user)


    elif str(reaction.emoji) == '🐱':
      if user.bot == False and str(reaction.message.reactions[0]) == '🐱':
        with open('json/cat.json', 'r') as f:
          ids = json.load(f)

        id = ids[str(reaction.message.guild.id)]

        message = await channel.fetch_message(int(id))

        embed = nextcord.Embed(
          colour = 0xFF00FF
        )

        headers = {"Authorization": "api_key=8589f552-4b09-4ffc-8561-cc6ef4e59018"}

        url = 'https://api.thecatapi.com/v1/images/search'

        async with aiohttp.ClientSession(headers = headers) as session:
          html = await self.fetch(session, url)
          img = (html[0]).get('url')

        embed.set_image(url = img)

        await message.edit(embed = embed)
        await reaction.remove(user)



  async def fetch(self, session, url):
    async with session.get(url) as response:
      return await response.json()


def setup(bot):
  bot.add_cog(listener(bot))