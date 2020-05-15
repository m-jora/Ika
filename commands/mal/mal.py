# mal.py
# contains the account, season and schedule commands for mal
import discord
import asyncio, aiohttp

from jikanpy import AioJikan
from discord.ext import commands

class mal(commands.Cog):

  def __init__(self, bot):
    self.client = bot


  @commands.command()
  async def account(self, ctx, message):
    loop = asyncio.get_event_loop()
    aio_jikan = AioJikan(loop = loop)
    
    if message == '':
      await ctx.send('`Please provide an account name`')
      return

    try:
      user = await aio_jikan.user(username = message)

    except:
      await ctx.send('`User not found`')
      return

    url = user.get('url')
    username = user.get('username')
    anime = user.get('anime_stats')

    if user.get('image_url') == None:
      img = 'https://i.imgur.com/9mnjji8.png'

    else:
      img = user.get('image_url')

    days = anime.get('days_watched')
    avg_score = anime.get('mean_score')
    watching = anime.get('watching')
    completed = anime.get('completed')
    hold = anime.get('on_hold')
    dropped = anime.get('dropped')
    plan = anime.get('plan_to_watch')
    total = anime.get('total_entries')
    num_ep = anime.get('episodes_watched')

    embed = discord.Embed(
      title = '**' + username + '**',
      colour = 0x000CFF,
      url = url
    )


    embed.set_thumbnail(url = img)
    embed.add_field(name = 'Days watched', value = days)
    embed.add_field(name = 'Episodes Watched', value = num_ep)
    embed.add_field(name = 'Avg Score', value = avg_score)
    embed.add_field(name = 'Total number of shows', value = total)
    embed.add_field(name = 'Watching', value = watching)
    embed.add_field(name = 'Completed', value = completed)
    embed.add_field(name = 'Plan to Watch', value = plan)
    embed.add_field(name = 'Dropped', value = dropped)
    embed.add_field(name = 'On hold', value = hold)

    await aio_jikan.close()

    await ctx.send(embed = embed)
    return



  @commands.command()
  async def aniseason(self, ctx, year, sesn):
    loop = asyncio.get_event_loop()
    aio_jikan = AioJikan(loop = loop)

    season = await aio_jikan.season(year = int(year), season = sesn)
    anime = season.get('anime')

    embed = discord.Embed(
      title = sesn.capitalize() + ' ' + year + ' Season',
      colour = 0x000CFF
    )

    for x in range(5):
      title = anime[x].get('title')
      ep = anime[x].get('episodes')
      score = anime[x].get('score')

      embed.add_field(name = title, value = 'Eps: ' + str(ep) + ' / Score: ' + str(score), inline = False)

    await aio_jikan.close()
    await ctx.send(embed = embed)
    #'anime': is list of shows



  @commands.command()
  async def schedule(self, ctx, day = ''):
    loop = asyncio.get_event_loop()
    aio_jikan = AioJikan(loop = loop)

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

        embed.add_field(name = date.capitalize(), value = title + '\nScore: ' + str(score), inline = False)
  

      await ctx.send(embed = embed)
      await aio_jikan.close()
      return

    elif day == 'days':
      desc = ''

      for x in shows:
        desc += x + ' : ' + shows[x] + '\n'
        print(desc)

      embed = discord.Embed(
        title = 'Days',
        colour = 0x000CFF,
        description = desc
      )
      await ctx.send(embed = embed)
      return

    elif day in shows:
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

          embed.add_field(name = title, value = 'Score: ' + str(score), inline = False)

      else:
        for x in range(len(hr)):
          sch = hr[x]
          title = sch.get('title')
          score = sch.get('score')

          embed.add_field(name = title, value = 'Score: ' + str(score), inline = False)

      await ctx.send(embed = embed)
      await aio_jikan.close()
      return

    else:
      await ctx.send('`input a valid day`')
      return



def setup(bot):
  bot.add_cog(mal(bot))