# anime.py
# contains the ommands to search for anime in mal or anilist
import discord
import json
import requests
import asyncio, aiohttp

from emoji import UNICODE_EMOJI
from jikanpy import AioJikan
from discord.ext import commands

class anime(commands.Cog):

  def __init__(self, bot):
    self.client = bot
    self.url = 'https://graphql.anilist.co'

  @commands.command()
  async def ani(self, ctx, *, message):
    if message[:4] == 'mal ':
      message = message[4:]
      await self.malani(ctx, message)

    elif message[:3] == 'al ':
      message = message[3:]
      await self.alani(ctx, message)

    else:
      await self.alani(ctx, message)
  

  async def malani(self, ctx, message):
    aio_jikan = AioJikan()
    
    if message == '':
      await ctx.send('`You need to enter a show name`')
      return

    else:
      message = message.lower()

    if message in UNICODE_EMOJI:
      await ctx.send('`Emjois are not allowed`')
      return

    async with ctx.channel.typing():

      results = await aio_jikan.search('anime', message)
      info = results.get('results')

      check = []
      if info == check:
        await ctx.send('`No results found`')
        return

      info = info[0]
      show = info.get('mal_id')
      title = info.get('title').lower()
 
      url = 'https://api.jikan.moe/v3/anime/' + str(show)
      async with aiohttp.ClientSession() as session:
        data = await self.fetch(session, url)
 
      img = data.get('image_url')
      title = data.get('title')
      num_ep = data.get('episodes')
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
      aired = data.get('aired')
      start = aired.get('from')
      end = aired.get('to')

      if start == None:
        start = 'Not Yet Aired'
        num_ep = 'None'
        end = 'Not Yet Aired'
  
      elif start != None:
        start = start[:10]
 
      if num_ep == None and start != None:
        num_ep = 'Currently Airing'


      if end == None and start != None:
        end = 'On Going'

      elif end != 'Not Yet Aired':
        end = end[:10]

      link = data.get('url')
      author = data.get('title_english')
      if author == title:
        author = None
  
      #handles the synopsis for show
      description = data.get('synopsis')
      description = description[:255]
      description += '...'


      embed = discord.Embed(
        title = '**' + title +'**',
        description = author,
        colour = 0x000CFF,
        url = link
      )


      embed.set_thumbnail(url = img)
      embed.add_field(name = 'Status', value = status)
      embed.add_field(name = 'Number of episodes', value = num_ep)
      embed.add_field(name = 'Score / Popularity / Rank', value = 'Score: ' + str(score) + ' / Popularity: ' + str(pop) + ' / Rank: ' + str(rank), inline = False)
      embed.add_field(name = 'Started Airing', value = start)
      embed.add_field(name = 'Finished Airing', value = end)
      embed.add_field(name = 'Synopsis', value = description, inline = False)
      embed.add_field(name = 'Genres', value = genre, inline = False)
      embed.set_footer(text = 'Replying to: ' + str(ctx.author) + ' | ' + 'info from MAL')

      await aio_jikan.close()

      await ctx.send(embed = embed)


  async def alani(self, ctx, message):
    async with ctx.channel.typing():

      query = '''
        query ($id: Int, $page: Int, $perPage: Int, $search: String, $type: MediaType) {
          Page (page: $page, perPage: $perPage) {
            pageInfo {
              total
              currentPage
              lastPage
              hasNextPage
              perPage
            }
            media (id: $id, search: $search, type: $type) {
              id
              description(asHtml: false)
              title {
                  english
                  romaji
              }
              coverImage {
                large
              }
              bannerImage
              averageScore
              meanScore
              status
              episodes
              genres
              popularity
              rankings{
                rank
                allTime
              }
              startDate{
                year
                month
                day
              }
              endDate{
                year
                month
                day
              }
              externalLinks{
                url
                site
              }
          }
      }
  }
'''

      variables = {
        'search': message,
        'page': 1,
        'type': 'ANIME'
      }


      response = requests.post(self.url, json={'query': query, 'variables': variables})
      #print(response.json())
      response = response.json()

      stuff = response.get('data')
      page = stuff.get('Page')
      page = page.get('media')
      media = page[0]
      img = media.get('coverImage')
      img = img.get('large')

      description = media.get('description')
      description = description.replace('<br>\n', ' ')
      description = description.replace('<br> ', ' ')
      description = description[:255]
      description += '...'


      titles = media.get('title')
      title = titles.get('romaji')
      title_eng = titles.get('english')

      score = float(media.get('averageScore')) / 10.0

      status = media.get('status')
      if status == 'FINISHED':
        status = 'Finished Airing'

      num_ep = media.get('episodes')

      popularity = media.get('popularity')
      rank = media.get('rankings')
      
      try:
        rank = rank[1]
     
      except IndexError:
        if len(rank) < 1:
          rank = 'N/A'

        else:
          rank = rank[0]

      if rank is not 'N/A':
        rank = rank.get('rank')
      genres = media.get('genres')

      genre = ''
      for x in genres:
        if x == 'Hentai':
          await ctx.send('That is not allowed in this channel')
          return

        if x != genres[-1]:
          genre += x + ', '

        else:
          genre += x
      
      date = media.get('startDate')
      year = date.get('year')
      month = date.get('month')
      day = date.get('day')

      start = str(month) + '-' + str(day) + '-' + str(year)


      date = media.get('endDate')
      year = date.get('year')
      month = date.get('month')
      day = date.get('day')

      end = str(month) + '-' + str(day) + '-' + str(year)


      id = media.get('id')
      link = 'https://anilist.co/anime/' + str(id)




      embed = discord.Embed(
        title = '**' + title + '**',
        description = title_eng,
        colour = 0x000CFF,
        url = link
      )

      embed.set_thumbnail(url = img)
      embed.add_field(name = 'Status', value = status)
      embed.add_field(name = 'Number of episodes', value = num_ep)
      embed.add_field(name = 'Score / Popularity / Rank', value = 'Score: ' + str(score) + ' / Popularity: ' + str(popularity) + ' / Rank: ' + str(rank), inline = False)
      embed.add_field(name = 'Started Airing', value = start)
      embed.add_field(name = 'Finished Airing', value = end)
      embed.add_field(name = 'Synopsis', value = description, inline = False)
      embed.add_field(name = 'Genres', value = genre, inline = False)
      embed.set_footer(text = 'Replying to: ' + str(ctx.author) + ' | ' + 'info from Anilist')

      await ctx.send(embed = embed)
      return


  async def fetch(self, session, url):
    async with session.get(url) as response:
      return await response.json()

def setup(bot):
  bot.add_cog(anime(bot))

