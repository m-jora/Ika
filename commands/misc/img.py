# img.py
# handles commands that send some sort of image

import random
import aiohttp
import discord
from discord.ext import commands

class img(commands.Cog):

  def __init__(self, bot):
    self.client = bot

  @commands.command()
  async def mathfun(self, ctx, message = ''):
    if message == '':
      location = [
        'images/3.png',
        'images/2.png',
        'images/1.png',
      ]

      pic = random.choice(location)

      await ctx.send(file = discord.File(pic))
      return

    elif message == '1' or message == 1 or message == 'one' or message == 'One' or message == 'eins':
      await ctx.send(file = discord.File('images/1.png'))
      return

    elif message == '2' or message == 2 or message == 'two' or message == 'Two' or message == 'zwei':
      await ctx.send(file = discord.File('images/2.png'))
      return

    elif message == '3' or message == 3 or message == 'three' or message == 'Three' or message == 'drei':
      await ctx.send(file = discord.File('images/3.png'))
      return

    else:
      await ctx.message.add_reaction('👎')
      return


  @commands.command()
  async def inspire(self, ctx):
    embed = discord.Embed(
      colour = 0x8000FF
    )  

    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }

    url = 'https://inspirobot.me/api?generate=true'

    async with aiohttp.ClientSession() as session:
      html = await self.ftext(session, url)

    embed.set_image(url = html)

    await ctx.send(embed = embed)


  @commands.command(name = 'random')
  async def ran(self, ctx):
    imgs = [
      'images/fp.png',
      'images/fp1.png',
      'images/fp2.png',
      'images/fp3.png',
      'images/fp4.png',
      'images/fp5.png',
      'images/fp6.png',
      'images/fp7.png',
      'images/help.png',
      'images/pogg.png',
      'images/reverse.png'
    ]

    pic = random.choice(imgs)
    await ctx.send(file = discord.File(pic))
    return


  async def fetch(self, session, url):
    async with session.get(url) as response:
      return await response.json()


  async def ftext(self, session, url):
    async with session.get(url) as response:
      return await response.text()


def setup(bot):
  bot.add_cog(img(bot))