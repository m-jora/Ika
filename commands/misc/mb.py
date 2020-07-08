# mb.py
# handles misc goofy commands that just kinda exist

import random
import json

from discord.ext import commands


class mb(commands.Cog):

  def __init__(self, bot):
    self.client = bot

  @commands.command()
  async def ping(self, ctx):
    with open('json/track.json', 'r') as f:
      tracking = json.load(f)
      
    if 'ping' in tracking:
      tracking['ping'] += 1

    else:
      tracking['ping'] = 1

    with open('json/track.json','w') as f:
      json.dump(tracking, f, indent = 2)
    await ctx.send('`pong`')

  @commands.command()
  async def pong(self, ctx):
    with open('json/track.json', 'r') as f:
      tracking = json.load(f)
      
    if 'pong' in tracking:
      tracking['pong'] += 1

    else:
      tracking['pong'] = 1

    with open('json/track.json','w') as f:
      json.dump(tracking, f, indent = 2)
    await ctx.send('`ping`')

  @commands.command()
  async def pizza(self, ctx):
    lit = ['Hi Kendall', 'Pizza', 'Howdy Partner', 'Hello Travis', '<@275065846836101120>', 'Hi Evan',]
    response = random.choice(lit)

    with open('json/track.json', 'r') as f:
      tracking = json.load(f)
      
    if 'pizza' in tracking:
      tracking['pizza'] += 1

    else:
      tracking['pizza'] = 1

    with open('json/track.json','w') as f:
      json.dump(tracking, f, indent = 2)

    await ctx.send(response)
    

  @commands.command(aliases = ['Hi', 'hello', 'Hello'])
  async def hi(self, ctx):
    greetings = ['Hi', 'Hello', 'Howdy', 'Salutations', 'Hey', 'uwu', 'Shalom',]
    greeting = random.choice(greetings)
    greet2 = ['\nHow are you?', '\nWhat\'s up?', '\nWhat anime are you watching?', '\nHas school killed you yet?',]
    greets2 = random.choice(greet2)

    with open('json/track.json', 'r') as f:
      tracking = json.load(f)
      
    if 'hi' in tracking:
      tracking['hi'] += 1

    else:
      tracking['hi'] = 1

    with open('json/track.json','w') as f:
      json.dump(tracking, f, indent = 2)


    await ctx.send(greeting + ' <@' + str(ctx.author.id) + '>' + greets2)



  @commands.command(name = '8ball')
  async def _8ball(self, ctx, *, question):
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

    with open('json/track.json', 'r') as f:
      tracking = json.load(f)
      
    if '8ball' in tracking:
      tracking['8ball'] += 1

    else:
      tracking['8ball'] = 1

    with open('json/track.json','w') as f:
      json.dump(tracking, f, indent = 2)


    if question == '':
      await ctx.send('Ask me a question by typing ~8ball <question>')

    else:
      await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')

  @commands.command()
  async def flip(self, ctx):
    sides = [
      'heads',
      'tails',
    ]

    with open('json/track.json', 'r') as f:
      tracking = json.load(f)
      
    if 'flip' in tracking:
      tracking['flip'] += 1

    else:
      tracking['flip'] = 1

    with open('json/track.json','w') as f:
      json.dump(tracking, f, indent = 2)

    await ctx.send(f'It\'s {random.choice(sides)}')


  @commands.command()
  async def say(self, ctx, *, message):
    with open('json/track.json', 'r') as f:
      tracking = json.load(f)
      
    if 'say' in tracking:
      tracking['say'] += 1

    else:
      tracking['say'] = 1

    with open('json/track.json','w') as f:
      json.dump(tracking, f, indent = 2)
    
    if message == '':
      return

    else:
      with open('json/say.json', 'r') as f:
        users = json.load(f)

      if str(ctx.author.id) in users:
        list = users[str(ctx.author.id)]
        list.append(message)
        users[str(ctx.author.id)] = list

      else:
        list = [message]
        users[str(ctx.author.id)] = list

      with open('json/say.json', 'w') as f:
        json.dump(users, f, indent = 2) 

      print(ctx.author, 'said', message)
      await ctx.send(message)


  @commands.command()
  async def choose(self, ctx, msg1 = '', msg2 = ''):
    with open('json/track.json', 'r') as f:
      tracking = json.load(f)
      
    if 'choose' in tracking:
      tracking['choose'] += 1

    else:
      tracking['choose'] = 1

    with open('json/track.json','w') as f:
      json.dump(tracking, f, indent = 2)
    
    if msg1 == '' or msg2 == '':
      await ctx.send('Please provide at least 2 arguments')
      return
    
    msgs = [msg1, msg2]
    send = random.choice(msgs)

    await ctx.send (send)


def setup(bot):
  bot.add_cog(mb(bot))