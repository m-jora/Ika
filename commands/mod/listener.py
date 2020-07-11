# listener.py
# handles all different reaction listeners

import json
import discord
import asyncio, aiohttp

from discord.ext import commands

class listener(commands.Cog):

  def __init__(self, bot):
    self.client = bot

  #reaction for removing embed
  @commands.Cog.listener()
  async def on_reaction_add(self, reaction, user):
    channel = reaction.message.channel

    if (str(reaction.emoji) == '🐶' or str(reaction.emoji) == '🐕') and reaction.message.author.id == 705683895055679521:
      if user.id != 705683895055679521 and str(reaction.message.reactions[0]) == '🐶' and reaction.count > 1 and str(reaction.message.reactions[1] == '🐕'):
        with open('json/dog.json', 'r') as f:
          ids = json.load(f)

        id = list(ids.keys())[0]

        message = await channel.fetch_message(int(id))

        embed = discord.Embed(
          title = None,
          description = None,
          colour = 0xFF00FF
        )

        url = 'https://dog.ceo/api/breeds/image/random'

        async with aiohttp.ClientSession() as session:
          html = await self.fetch(session, url)
          img = html.get('message')

        embed.set_image(url = img)

        await message.edit(embed = embed)

        await reaction.remove(user)


    elif str(reaction.emoji) == '🐱' and reaction.message.author.id == 705683895055679521:
      if user.id != 705683895055679521 and str(reaction.message.reactions[0]) == '🐱':
        with open('json/cat.json', 'r') as f:
          ids = json.load(f)

        id = list(ids.keys())[0]

        message = await channel.fetch_message(int(id))

        embed = discord.Embed(
          title = None,
          description = None,
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