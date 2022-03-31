# manga.py
# contains the commands to search for manga and list manga
import discord
import json
import asyncio, aiohttp

from jikanpy import AioJikan
from discord.ext import commands

class manga(commands.Cog):
  
  def __init__(self, bot):
    self.client = bot

  @commands.command()
  async def manga(self, ctx, *, message):
    aio_jikan = AioJikan()
    
    if message == '':
      await ctx.send('`You need to enter a manga name`')
      return

    async with ctx.channel.typing():

      results = await aio_jikan.search('manga', message)
      info = results['results']

      if info == []:
        await ctx.send('No results found')
        return

      show = info[0]['mal_id']
  
      url = 'https://api.jikan.moe/v3/manga/' + str(show)
      async with aiohttp.ClientSession() as session:
        data = await self.fetch(session, url)

      info = {
        'title': data['title'],
        'show': show,
        'img': data['image_url'],
        'chapters': (data['chapters'] if (data['chapters'] is not None) else 'Currently Publishing'),
        'status': data['status'],
        'score': data['score'],
        'rank': data['rank'],
        'pop': data['popularity'],
        'genres': 'update later',
        'from': data['published']['prop']['from'],
        'to': data['published']['prop']['to'],
        'link': data['url'],
        'author': data['title_english'] if data['title_english'] is not None else '',
        'description': data['synopsis'] if data['synopsis'] is not None else 'No Synopsis Found',
        'genres': data['genres']
      }

      info['start'] = f'{info["from"]["month"]}-{info["from"]["day"]}-{info["from"]["year"]}'
      info['end'] = f'{info["to"]["month"]}-{info["to"]["day"]}-{info["to"]["year"]}'
      
      info['start'] = 'Not Yet Published' if 'None' in info['start'] else info['start']
      info['end'] = '-' if info['start'] is 'Not Yet Published' and 'None' in info['end'] else (
        'Currently Publishing' if 'Not Yet Published' != info['start'] and 'None' in info['end'] else info['end'])

      genre = ''
      for x in info['genres']:
        if x != info['genres'][len(info['genres']) - 1]:
          genre += f'{x["name"]}, '

        else:
          genre += x['name']

      if 'Hentai' in genre and not ctx.channel.is_nsfw():
        await ctx.send('Hentai is not allowed in this channel')
        return

      embed = discord.Embed(
        title = f'**{info["title"]}**',
        description = info['author'],
        colour = 0x000CFF,
        url = info['link']
      )

      embed.set_thumbnail(url = info['img'])
      embed.add_field(name = 'Status', value = info['status'])
      embed.add_field(name = 'Number of Chapters', value = str(info['chapters']))
      embed.add_field(name = 'Score / Popularity / Rank', value = f'Score: {str(info["score"])} / Popularity: {str(info["pop"])} / Rank: {str(info["rank"])}', inline = False)
      embed.add_field(name = 'Started Publishing', value = info['start'])
      embed.add_field(name = 'Finished Publishing', value = info['end'])
      embed.add_field(name = 'Synopsis', value = f'{info["description"][:252]}...', inline = False)
      embed.add_field(name = 'Genres', value = genre, inline = False)

      await aio_jikan.close()
      await ctx.send(embed = embed)


  async def fetch(self, session, url):
    async with session.get(url) as response:
      return await response.json()

def setup(bot):
  bot.add_cog(manga(bot))