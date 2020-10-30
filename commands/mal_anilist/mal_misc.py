# mal.py
# contains the account, season and schedule commands for mal
import discord

from jikanpy import AioJikan
from discord.ext import commands

class mal(commands.Cog):

  def __init__(self, bot):
    self.client = bot


  @commands.command()
  async def aniseason(self, ctx, year, sesn):
    aio_jikan = AioJikan()

    async with ctx.channel.typing():
      anime = (await aio_jikan.season(year = int(year), season = sesn)).get('anime')

      embed = discord.Embed(
        title = f'{sesn.capitalize()}  {year} Season',
        colour = 0x000CFF
      )

      #'anime': is list of shows
      for x in range(5):
        title = anime[x].get('title')
        ep = anime[x].get('episodes')
        score = anime[x].get('score')

        embed.add_field(name = title, value = f'Eps: {ep} / Score: {score}', inline = False)

      await aio_jikan.close()
      await ctx.send(embed = embed)


  @commands.command()
  async def schedule(self, ctx, day = ''):
    aio_jikan = AioJikan()

    shows = {
      'm':'monday',
      't':'tuesday',
      'w':'wednesday',
      'r':'thursday',
      'f':'friday',
      's':'saturday',
      'su':'sunday'
    }

    if day == '':
      async with ctx.channel.typing():
        scheduled = await aio_jikan.schedule()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

        embed = discord.Embed(
          title = 'Airing',
          colour = 0x000CFF
        )

        for x in range(7):
          hr = scheduled.get(days[x])
          date = days[x]
          sch = hr[0]
          title = sch.get('title')
          score = sch.get('score')

          embed.add_field(name = date.capitalize(), value = f'{title}\nScore: {str(score)}', inline = False)
  

        await ctx.send(embed = embed)
        await aio_jikan.close()
        return

    elif day == 'days':
      async with ctx.channel.typing():
        desc = ''

        for x in shows:
          desc += f'{x} : {shows[x]}\n'

        embed = discord.Embed(
          title = 'Days',
          colour = 0x000CFF,
          description = desc
        )
        await ctx.send(embed = embed)
        return

    elif day in shows:
      async with ctx.channel.typing():
        scheduled = await aio_jikan.schedule(shows[day])
    
        embed = discord.Embed(
          title = shows[day].capitalize(),
          colour = 0x000CFF
        )

        hr = scheduled.get(shows[day])

        if len(hr) > 7:
          for x in range(7):
            sch = hr[x]
            title = sch.get('title')
            score = sch.get('score')

            embed.add_field(name = title, value = f'Score: {str(score)}', inline = False)

        else:
          for x in range(len(hr)):
            sch = hr[x]
            title = sch.get('title')
            score = sch.get('score')

            embed.add_field(name = title, value = f'Score: {str(score)}', inline = False)

        await ctx.send(embed = embed)
        await aio_jikan.close()
        return

    else:
      await ctx.send('Please input a valid day')
      return


def setup(bot):
  bot.add_cog(mal(bot))