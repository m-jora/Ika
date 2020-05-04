# anime.py
# allows for searching of mal returning animes
# maybe mangas soon?

import random
import discord
import urllib, json
from jikanpy import Jikan
from emoji import UNICODE_EMOJI

jikan = Jikan()


async def mal(ctx, message):

  if message == '':
    await ctx.send('`You need to enter a show name`')
    return

  else:
    message = message.lower()


  results = jikan.search('anime', message)
  info = results.get('results')
  info = info[0]
  show = info.get('mal_id')
  title = info.get('title').lower()
  #title1 = ''

  '''for x in range(len(title)):
    if title[x].isalnum() or title[x] == ' ':
      title1 += title[x]
     
    else:
      title1 += ' '''

  

  
  url = 'https://api.jikan.moe/v3/anime/' + str(show)
  response = urllib.request.urlopen(url)
  data = json.loads(response.read())

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
      await ctx.send('That is not allowed in this channel')
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
  description = description[:252]
  description += '...'


  embed = discord.Embed(
    title = '**' + title +'**',
    description = author,
    colour = 0x000CFF,
    url = link
  )


  embed.set_thumbnail(url = img)
  #embed.set_footer(text = 'stuff')
  embed.add_field(name = 'Status', value = status)
  embed.add_field(name = 'Number of episodes', value = num_ep)
  embed.add_field(name = 'Score / Popularity / Rank', value = 'Score: ' + str(score) + ' / Popularity: ' + str(pop) + ' / Rank: ' + str(rank), inline = False)
  embed.add_field(name = 'Started Airing', value = start)
  embed.add_field(name = 'Finished Airing', value = end)
  embed.add_field(name = 'Synopsis', value = description, inline = False)
  embed.add_field(name = 'Genres', value = genre, inline = False)


  await ctx.send(embed = embed)






async def malsearch(ctx, message):
  if message == '':
    await ctx.send('`You need to enter a show name`')
    return

  else:
    message = message.lower()


  if message in UNICODE_EMOJI:
    await ctx.send('Emjois are not allowed')
    return 


  results = jikan.search('anime', message)
  info = results.get('results')
  ids = []
  for x in range(5):
    ids.append(info[x].get('mal_id'))
  
  desc =  ''

  for x in range(5):
    url = 'https://api.jikan.moe/v3/anime/' + str(ids[x])
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    if x == 4:
      if data.get('title_english') == None:
        desc += '**·** **' + data.get('title') + '**'

      elif data.get('title_english').lower() != data.get('title').lower():
        desc += '**·** **' + data.get('title') + '**\n' + '---' + data.get('title_english')

    else:
      if data.get('title_english') == None:
        desc += '**·** **' + data.get('title') + '**\n'

      elif data.get('title_english').lower() != data.get('title').lower():
        desc += '**·** **' + data.get('title') + '**\n' + '---' + data.get('title_english') + '\n'

  
  embed = discord.Embed(
    title = '**RESULTS**',
    description = desc,
    colour = 0x000CFF,
  )

  embed.set_footer(text = 'Use ~mal <title> to get more information')

  await ctx.send(embed = embed)

  