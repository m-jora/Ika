# mb.py
'''contains misc commands'''

import random
import discord
import asyncio, aiohttp


async def pizza(ctx):
  lit = ['Hi Kendall', 'Pizza', 'Howdy Partner', 'Hello Travis', '<@275065846836101120>', 'Hi Evan',]
  response = random.choice(lit)
  await ctx.send(response)

async def banjo(ctx):
  await ctx.send('''

                .----.
           [-\|.  .\|-]
           [-\|.\\/.\|-]
             \|\|\|\|/
              \|\|\|\|
              \|\|\|\|
              \|\|\|\|
              \|\|\|\|
              \|\|\|\|
              \|\|\|\|
             /\|\|\|\|
           [-\|\|\|\|\|
             \|\|\|\|\|
             \|\|\|\|\|
             \|\|\|\|\|
             \|\|\|\|\|
           _.\|\|\|\|\|._
        .-\'  |||||  `-.
      .\'     |||||     `.
    .\'       |||||       `.
   /         |||||         \
  /          |||||          \
  |          |||||          |
  |          _____          |
  |-.       \'-----\'         |
  \  `.      |||||          /
   \   \    .-----.        /
    `.  \   |     |      .\'
      \'.|   \'.    |    .\'
        \'--._|____|_.-\'''')

async def hello(ctx):
  greetings = ['Hi', 'Hello', 'Howdy', 'Salutations', 'Hey', 'uwu', 'Shalom',]
  greeting = random.choice(greetings)
  greet2 = ['\nHow are you?', '\nWhat\'s up?', '\nWhat anime are you watching?', '\nHas school killed you yet?',]
  greets2 = random.choice(greet2)

  await ctx.send(greeting + ' <@' + str(ctx.author.id) + '>' + greets2)

async def _8ball(ctx, question):
  responses = [
    'As I see it, yes',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again',
    'Don\'t count on it',
    'It is certain',
    'It is decidedly so',
    'Most likely',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Outlook good',
    'Reply hazy, try again',
    'Signs point to yes',
    'Very doubtful',
    'Without a doubt',
    'Yes',
    'Yes - definitely',
    'You may rely on it',
    'Please shake again',
    'Who said I had the answers',
    'Ask someone else',
    'Why would you ask me that?',
  ]

  if question == '':
    await ctx.send('Ask me a question by typing ~8ball <question>')

  else:
    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')

async def flip(ctx):
  sides = [
    'heads',
    'tails',
  ]

  await ctx.send(f'It\'s {random.choice(sides)}')

async def dog(ctx):
  embed = discord.Embed(
    title = None,
    description = None,
    colour = 0xFF00FF
  )
  urls = [
    'http://random.dog/woof',
    'https://dog.ceo/api/breeds/image/random',
  ]

  url = random.choice(urls)

  if url == urls[0]:
    async with aiohttp.ClientSession() as session:
      html = await ftext(session, url)
      pic = 'http://random.dog/' + html

    embed.set_image(url = pic)

    await ctx.send(embed = embed)
    return

  else:
    async with aiohttp.ClientSession() as session:
      html = await fetch(session, url)
      img = html.get('message')

    embed.set_image(url = img)

    await ctx.send(embed = embed)
    return

async def cat(ctx):
  embed = discord.Embed(
    colour = 0xFF00FF
  )

  url = 'http://aws.random.cat/meow'
  async with aiohttp.ClientSession() as session:
    html = await fetch(session, url)
    img = html.get('file')

  embed.set_image(url = img)

  await ctx.send(embed = embed)

async def mathfun(ctx, message):
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
    return

async def say(ctx, message):
  if message == '':
    return

  else:
    print(ctx.author, 'said', message)
    await ctx.send(message)

async def meme(ctx):
  embed = discord.Embed(
    colour = 0xFFFF00
  )

  url = 'https://meme-api.herokuapp.com/gimme'
  async with aiohttp.ClientSession() as session:
    html = await fetch(session, url)
    link = html.get('url')

  embed.set_image(url = link)

  await ctx.send(embed = embed)

async def inspire(ctx):
  embed = discord.Embed(
    colour = 0x8000FF
  )  

  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
  }

  url = 'https://inspirobot.me/api?generate=true'
  req = urllib.request.Request(url = url, headers = headers)
  response = urllib.request.urlopen(req).read()

  img = response.decode('utf-8')

  embed.set_image(url = img)

  await ctx.send(embed = embed)




async def fetch(session, url):
  async with session.get(url) as response:
    return await response.json()

async def ftext(session, url):
  async with session.get(url) as response:
    return await response.text()