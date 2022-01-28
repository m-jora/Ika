# img.py
# handles commands that send some sort of image

import random
import aiohttp
import nextcord
from nextcord.ext import commands

class img(commands.Cog):

  def __init__(self, bot):
    self.client = bot


  @commands.command()
  async def inspire(self, ctx):
    embed = nextcord.Embed(
      colour = 0xFF00FF
    )  

    url = 'https://inspirobot.me/api?generate=true'
    async with aiohttp.ClientSession() as session:
      html = await self.ftext(session, url)

    embed.set_image(url = html)
    await ctx.send(embed = embed)


  '''sends gifs of ika doing stuff'''
  @commands.command(aliases = ['do'])
  async def ikado(self, ctx, do = ''):
    switch = {
      'throw' : 'images/ikathrow.gif',
      'ahh' : 'images/ikawack.gif',
      'wut' : 'images/ikaconfuse.gif',
      'dance'  : 'images/ikadance.gif',
      'idk' : 'images/ikanyan.gif'
    }
    file = switch.get(do, 'not valid')

    if file is not 'not valid':
      await ctx.send(file = nextcord.File(file))


  @commands.command()
  async def kendallisabully(self, ctx):
    embed = nextcord.Embed(
      title = 'KENDALL IS A BULLY'
    )

    embed.add_field(name = "NO", value = 'PLEASE STOP BULLYING')
    embed.set_image(url = 'https://images-na.ssl-images-amazon.com/images/I/61PrwBJ9%2BzL._AC_SL1500_.jpg')

    this = await ctx.send(embed = embed)
    msg = await ctx.fetch_message(int(this.id))

    await msg.add_reaction('🇸')
    await msg.add_reaction('🇹')
    await msg.add_reaction('🇴')
    await msg.add_reaction('🅿️')
    await msg.add_reaction('🛑')
    return


  async def fetch(self, session, url):
    async with session.get(url) as response:
      return await response.json()

  async def ftext(self, session, url):
    async with session.get(url) as response:
      return await response.text()


def setup(bot):
  bot.add_cog(img(bot))