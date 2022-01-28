# anime.py
# contains the ommands to search for anime in mal or anilist
import nextcord
import requests
import re
import aiohttp

from jikanpy import AioJikan
from nextcord.ext import commands

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

    async with ctx.channel.typing():

      results = await aio_jikan.search('anime', message)
      info = results['results']

      if info == []:
        await ctx.send('No results found')
        return

      show = info[0]['mal_id']
 
      url = 'https://api.jikan.moe/v3/anime/' + str(show)
      async with aiohttp.ClientSession() as session:
        data = await self.fetch(session, url)

      info = {
        'title': data['title'],
        'show': show,
        'img': data['image_url'],
        'num_ep': data['episodes'],
        'status': data['status'],
        'score': data['score'],
        'rank': data['rank'],
        'pop': data['popularity'],
        'from': data['aired']['prop']['from'],
        'to': data['aired']['prop']['to'],
        'link': data['url'],
        'author': data['title_english'] if data['title_english'] is not None else '',
        'description': data['synopsis'] if data['synopsis'] is not None else 'No Synopsis Found',
        'genres': data['genres']
      }

      info['start'] = f'{info["from"]["month"]}-{info["from"]["day"]}-{info["from"]["year"]}'
      info['end'] = f'{info["to"]["month"]}-{info["to"]["day"]}-{info["to"]["year"]}'

      info['start'] = 'Not Yet Aired' if 'None' in info['start'] else info['start']
      info['end'] = '-' if info['start'] is 'Not Yet Aired' and 'None' in info['end'] else (
        'Currently Airing' if 'Not Yet Aired' != info['start'] and 'None' in info['end'] else info['end'])

      genre = ''
      for x in info['genres']:
        if x != info['genres'][len(info['genres']) - 1]:
          genre += f'{x["name"]}, '

        else:
          genre += x['name']

      if 'Hentai' in genre and not ctx.channel.is_nsfw():
        await ctx.send('Hentai is not allowed in this channel')
        return


      embed = nextcord.Embed(
        title = f'**{info["title"]}**',
        description = info['author'],
        colour = 0x000CFF,
        url = info['link']
      )


      embed.set_thumbnail(url = info['img'])
      embed.add_field(name = 'Status', value = info['status'])
      embed.add_field(name = 'Number of episodes', value = info['num_ep'])
      embed.add_field(name = 'Score / Popularity / Rank', value = f'Score: {str(info["score"])} / Popularity: {str(info["pop"])} / Rank: {str(info["rank"])}', inline = False)
      embed.add_field(name = 'Started Airing', value = info['start'])
      embed.add_field(name = 'Finished Airing', value = info['end'])
      embed.add_field(name = 'Synopsis', value = f'{info["description"][:252]}...', inline = False)
      embed.add_field(name = 'Genres', value = genre, inline = False)
      embed.set_footer(text = f'Replying to: {str(ctx.author)} | info from MAL')

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


      response = requests.post(self.url, json={'query': query, 'variables': variables}).json()

      media = response['data']['Page']['media'][0]

      ################################################
      ########## SCORE NEEDS ERROR CATCHING ##########
      ################################################

      info = {
        'img': media['coverImage']['large'],
        'description': await self.cleanhtml(media['description']),
        'title': media['title']['romaji'],
        'title_eng': media['title']['english'],
        'score': float(media['averageScore']) / 10.0 if media['averageScore'] != None else '-',
        'num_ep': media['episodes'] if media['episodes'] != None else '-',
        'popularity': media['popularity'],
        'rank': media['rankings'][0]['rank'] if (len(media['rankings']) > 0 and len(media['rankings'][0])) >=1 else 'N/A'
      }

      ###############################################
      ##### NOT_YET_RELEASED FINISHED RELEASING #####
      ###############################################

      if media['status'] == 'FINISHED':
        info['status'] = 'Finished Airing'

      elif media['status'] == 'NOT_YET_RELEASED':
        info['status'] = 'Not Yet Released'

      elif media['status'] == 'RELEASING':
        info['status'] = 'Currently Airing'


      info['start'] = f'{media["startDate"]["month"]}-{media["startDate"]["day"]}-{media["startDate"]["year"]}'
      info['end'] = f'{media["endDate"]["month"]}-{media["endDate"]["day"]}-{media["endDate"]["year"]}'

      info['start'] = 'Not Yet Aired' if 'None' in info['start'] else info['start']
      info['end'] = '-' if info['start'] is 'Not Yet Aired' else (
        'Currently Airing' if 'Not Yet Aired' != info['start'] and 'None' in info['end'] else info['end'])
     

      genre = ''
      for x in media['genres']:
        if x != media['genres'][-1]:
          genre += x + ', '

        else:
          genre += x

      if 'Hentai' in genre and not ctx.channel.is_nsfw():
        await ctx.send('Hentai is not allowed in this channel')
        return

      link = f'https://anilist.co/anime/{media["id"]}'


      embed = nextcord.Embed(
        title = f'**{info["title"]}**',
        description = info['title_eng'],
        colour = 0x000CFF,
        url = link
      )

      embed.set_thumbnail(url = info['img'])
      embed.add_field(name = 'Status', value = info['status'])
      embed.add_field(name = 'Number of episodes', value = info['num_ep'])
      embed.add_field(name = 'Score / Popularity / Rank', value = f'Score: {info["score"]} / Popularity: {str(info["popularity"])} / Rank: {str(info["rank"])}', inline = False)
      embed.add_field(name = 'Started Airing', value = info['start'])
      embed.add_field(name = 'Finished Airing', value = info['end'])
      embed.add_field(name = 'Synopsis', value = info['description'], inline = False)
      embed.add_field(name = 'Genres', value = genre, inline = False)
      embed.set_footer(text = f'Replying to: {str(ctx.author)} | info from Anilist')

      await ctx.send(embed = embed)
      return


  async def fetch(self, session, url):
    async with session.get(url) as response:
      return await response.json()

  async def cleanhtml(self, text):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', text)
    return cleantext



def setup(bot):
  bot.add_cog(anime(bot))

