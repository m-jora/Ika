# manga.py
# contains the commands to search for manga and list manga
import discord
import json
import asyncio, aiohttp

from emoji import UNICODE_EMOJI
from jikanpy import AioJikan
from discord.ext import commands

class manga(commands.Cog):
  

  def __init__(self, bot):
    self.client = bot

  
  @commands.command()
  async def manga(self, ctx, *, message):
    loop = asyncio.get_event_loop()
    aio_jikan = AioJikan(loop = loop)
    
    if message == '':
      await ctx.send('`You need to enter a manga name`')
      return

    else:
      message = message.lower()

    if message in UNICODE_EMOJI:
      await ctx.send('`Emjois are not allowed`')
      return

    results = await aio_jikan.search('manga', message)
    info = results.get('results')

    check = []
    if info == check:
      await ctx.send('`No results found`')
      return

    info = info[0]
    show = info.get('mal_id')
    title = info.get('title').lower()
  
  
    url = 'https://api.jikan.moe/v3/manga/' + str(show)
    async with aiohttp.ClientSession() as session:
      data = await self.fetch(session, url)


    img = data.get('image_url')
    title = data.get('title')
  
    chapters = data.get('chapters')
    if chapters == None:
      chapters = 'Currently Publishing'

    status = data.get('status')
    score = data.get('score')
    rank = data.get('rank')
    pop = data.get('popularity')
    genres = data.get('genres')
  

    genre = ''
    for x in genres:
      if x.get('name') == 'Hentai':
        await ctx.send('`That is not allowed in this channel`')
        return

      if x != genres[len(genres) - 1]:
        genre += x.get('name') + ', '

      else:
        genre += x.get('name')
  
    #handles dates of the show airing
    aired = data.get('published')
    start = aired.get('from')
    end = aired.get('to')

    if start == None:
      start = 'Not Yet Published'
      end = 'Not Yet Published'
  
    elif start != None:
      start = start[:10]
 

    if end == None and start != None:
      end = 'On Going'

    elif end != 'Not Yet Published':
      end = end[:10]


    link = data.get('url')
    author = data.get('title_english')
    if author == title:
      author = None
  
    #handles the synopsis for show
    description = data.get('synopsis')
    description = description[:252]
    description += '...'


    embed = discord.Embed(
      title = '**' + title +'**',
      description = author,
      colour = 0x000CFF,
      url = link
    )


    embed.set_thumbnail(url = img)
    embed.add_field(name = 'Status', value = status)
    embed.add_field(name = 'Number of Chapters', value = str(chapters))
    embed.add_field(name = 'Score / Popularity / Rank', value = 'Score: ' + str(score) + ' / Popularity: ' + str(pop) + ' / Rank: ' + str(rank), inline = False)
    embed.add_field(name = 'Started Publishing', value = start)
    embed.add_field(name = 'Finished Publishing', value = end)
    embed.add_field(name = 'Synopsis', value = description, inline = False)
    embed.add_field(name = 'Genres', value = genre, inline = False)

    await aio_jikan.close()

    await ctx.send(embed = embed)



  @commands.command()
  async def mangasearch(self, ctx, *, message):
    with open('json/prefix.json', 'r') as f:
      prefixes = json.load(f)

    prefix = prefixes[str(ctx.guild.id)]

    loop = asyncio.get_event_loop()
    aio_jikan = AioJikan(loop = loop)
    
    if message == '':
      await ctx.send('`You need to enter a manga name`')
      return

    else:
      message = str(message).lower()


    if message in UNICODE_EMOJI:
      await ctx.send('`Emjois are not allowed`')
      return 


    results = await aio_jikan.search('manga', message)
    info = results.get('results')
    ids = []

    if info == ids:
      await ctx.send('`No results found`')
      return

  
    for x in range(5):
      ids.append(info[x].get('mal_id'))
  
    desc =  ''

    for x in range(5):
      url = 'https://api.jikan.moe/v3/manga/' + str(ids[x])
      async with aiohttp.ClientSession() as session:
        data = await self.fetch(session, url)

      if x == 4:
        if data.get('title_english') == None:
          desc += '**·** **' + data.get('title') + '**'

        elif data.get('title_english').lower() != data.get('title').lower():
          desc += '**·** **' + data.get('title') + '**\n' + '--' + data.get('title_english')

        elif data.get('title_english').lower() == data.get('title').lower():
          desc += '**·** **' + data.get('title') + '**'

      else:
        if data.get('title_english') == None:
          desc += '**·** **' + data.get('title') + '**\n'

        elif data.get('title_english').lower() != data.get('title').lower():
          desc += '**·** **' + data.get('title') + '**\n' + '--' + data.get('title_english') + '\n'

        elif data.get('title_english').lower() == data.get('title').lower():
          desc += '**·** **' + data.get('title') + '**\n'

  
    embed = discord.Embed(
      title = '**RESULTS**',
      description = desc,
      colour = 0x000CFF,
    )

    embed.set_footer(text = 'Use ' + prefix + 'manga <title> to get more information')

    await aio_jikan.close()

    await ctx.send(embed = embed)



  async def fetch(self, session, url):
    async with session.get(url) as response:
      return await response.json()


def setup(bot):
  bot.add_cog(manga(bot))