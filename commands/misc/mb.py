# mb.py
'''contains misc commands'''

import random


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

#async def dog(ctx):

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

