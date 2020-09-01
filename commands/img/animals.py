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
  async def dog(self, ctx, *, message = ''):
    embed = discord.Embed(
      colour = 0xFF00FF
    )
    if message == '':
      url = 'https://dog.ceo/api/breeds/image/random'
    
    else:
      url = 'https://dog.ceo/api/breed/' + message + '/images/random'


    async with aiohttp.ClientSession() as session:
      html = await self.fetch(session, url)
      img = html.get('message')

    embed.set_image(url = img)

    this = await ctx.send(embed = embed)
    msg = await ctx.fetch_message(int(this.id))

    await msg.add_reaction('🐶')
    await msg.add_reaction('🐕')

    with open('json/dog.json', 'r') as f:
      dogs = json.load(f)

    dogs.clear()
    dogs[str(this.id)] = 0

    with open('json/dog.json', 'w') as f:
      json.dump(dogs, f, indent = 2)

    return


  @commands.command()
  async def borz(self, ctx):
    embed = discord.Embed(
      colour = 0xFF00FF
    )

    url = 'https://dog.ceo/api/breed/borzoi/images/random'

    async with aiohttp.ClientSession() as session:
      html = await self.fetch(session, url)
      img = html.get('message')

    embed.set_image(url = img)

    await ctx.send(embed = embed)


  @commands.command(aliases = ['kitty', 'kitten'])
  async def cat(self, ctx):
    embed = discord.Embed(
      colour = 0xFF00FF
    )

    headers = {"Authorization": "api_key=8589f552-4b09-4ffc-8561-cc6ef4e59018"}

    url = 'https://api.thecatapi.com/v1/images/search'
    async with aiohttp.ClientSession(headers = headers) as session:
      html = await self.fetch(session, url)
      img = (html[0]).get('url')

    embed.set_image(url = img)

    this = await ctx.send(embed = embed)
    msg = await ctx.fetch_message(int(this.id))

    await msg.add_reaction('🐱')

    with open('json/cat.json', 'r') as f:
      cats = json.load(f)

    cats.clear()
    cats[str(this.id)] = 0

    with open('json/cat.json', 'w') as f:
      json.dump(cats, f, indent = 2)

    return


  async def fetch(self, session, url):
    async with session.get(url) as response:
      return await response.json()



def setup(bot):
  bot.add_cog(animals(bot))