# animals.py
# handles the animal commands that send random images

import discord
import json
import asyncio, aiohttp

from discord.ext import commands

class animals(commands.Cog):

  def __init__(self, bot):
    self.client = bot


  @commands.command(aliases = ['puppy', 'doggo', 'pup', 'pupper', 'hound', 'mutt'])
  async def dog(self, ctx):
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

    this = await ctx.send(embed = embed)

    with open('json/dog.json', 'r') as f:
      dogs = json.load(f)

    dogs.clear()
    dogs[str(this.id)] = 0

    with open('json/dog.json', 'w') as f:
      json.dump(dogs, f, indent = 2)

    return


  @commands.command()
  async def redog(self, ctx):
    with open('json/dog.json', 'r')as f:
      ids = json.load(f)

    id = list(ids.keys())[0]
  
    message = await ctx.fetch_message(int(id))
    if message.author.id != 705683895055679521:
      await ctx.message.add_reaction('👎')
      return

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


  @commands.command(aliases = ['kitty', 'kitten'])
  async def cat(self, ctx):
    embed = discord.Embed(
      colour = 0xFF00FF
    )

    url = 'http://aws.random.cat/meow'
    async with aiohttp.ClientSession() as session:
      html = await self.fetch(session, url)
      img = html.get('file')

    embed.set_image(url = img)

    await ctx.send(embed = embed)


  async def fetch(self, session, url):
    async with session.get(url) as response:
      return await response.json()



def setup(bot):
  bot.add_cog(animals(bot))