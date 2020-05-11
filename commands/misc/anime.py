# anime.py
# allows for searching of mal returning animes
# maybe mangas soon?

import random
import discord
import asyncio, aiohttp
from jikanpy import Jikan
from emoji import UNICODE_EMOJI

jikan = Jikan()


async def ani(ctx, message):

  if message == '':
    await ctx.send('`You need to enter a show name`')
    return

  else:
    message = message.lower()

  if message in UNICODE_EMOJI:
    await ctx.send('`Emjois are not allowed`')
    return

  results = jikan.search('anime', message)
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
    data = await fetch(session, url)
 
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
  embed.add_field(name = 'Number of episodes', value = num_ep)
  embed.add_field(name = 'Score / Popularity / Rank', value = 'Score: ' + str(score) + ' / Popularity: ' + str(pop) + ' / Rank: ' + str(rank), inline = False)
  embed.add_field(name = 'Started Airing', value = start)
  embed.add_field(name = 'Finished Airing', value = end)
  embed.add_field(name = 'Synopsis', value = description, inline = False)
  embed.add_field(name = 'Genres', value = genre, inline = False)


  await ctx.send(embed = embed)


async def anisearch(ctx, message):
  if message == '':
    await ctx.send('`You need to enter a show name`')
    return

  else:
    message = str(message).lower()


  if message in UNICODE_EMOJI:
    await ctx.send('`Emjois are not allowed`')
    return 


  results = jikan.search('anime', message)
  info = results.get('results')
  ids = []

  if info == ids:
    await ctx.send('`No results found`')
    return

  
  for x in range(5):
    ids.append(info[x].get('mal_id'))
  
  desc =  ''

  for x in range(5):
    url = 'https://api.jikan.moe/v3/anime/' + str(ids[x])
    async with aiohttp.ClientSession() as session:
      data = await fetch(session, url)


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

  embed.set_footer(text = 'Use ~ani <title> to get more information')

  await ctx.send(embed = embed)


async def manga(ctx, message):
  if message == '':
    await ctx.send('`You need to enter a manga name`')
    return

  else:
    message = message.lower()

  if message in UNICODE_EMOJI:
    await ctx.send('`Emjois are not allowed`')
    return

  results = jikan.search('manga', message)
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
    data = await fetch(session, url)


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


  await ctx.send(embed = embed)


async def mangasearch(ctx, message):
  if message == '':
    await ctx.send('`You need to enter a manga name`')
    return

  else:
    message = str(message).lower()


  if message in UNICODE_EMOJI:
    await ctx.send('`Emjois are not allowed`')
    return 


  results = jikan.search('manga', message)
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
      data = await fetch(session, url)

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

  embed.set_footer(text = 'Use ~manga <title> to get more information')

  await ctx.send(embed = embed)


async def account(ctx, message):
  if message == '':
    await ctx.send('`Please provide an account name`')
    return

  try:
    user = jikan.user(username = message)

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

  await ctx.send(embed = embed)

async def aniseason(ctx, year, sesn):
  season = jikan.season(year = int(year), season = sesn)
  anime = season.get('anime')

  embed = discord.Embed(
    title = sesn + ' ' + year + ' season',
    colour = 0x000CFF
  )


  for x in range(5):
    title = anime[x].get('title')
    ep = anime[x].get('episodes')
    score = anime[x].get('score')

    embed.add_field(name = title, value = '#Eps: ' + str(ep) + ' / Score: ' + str(score), inline = False)


  await ctx.send(embed = embed)
  #'anime': is list of shows



async def fetch(session, url):
  async with session.get(url) as response:
    return await response.json()
