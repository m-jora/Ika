# me.py
# commands that were designed only for me or only work for me currently

import discord
import random
import json

from discord.ext import commands

class me(commands.Cog):

  def __init__(self, bot):
    self.client = bot

  @commands.command()
  async def status(self, ctx, game, status, *, msg = ''):
    if ctx.author.id != 275065846836101120:
      await ctx.message.add_reaction('👎')
      return

    else:
      if game == 'stream':
        if status == 'online':
          await ctx.message.add_reaction('👍')
          await self.client.change_presence(status = discord.Status.online, activity = discord.Streaming(name = msg, url = 'https://twitch.tv/mr.bot'))
          return
        elif status == 'dnd':
          await ctx.message.add_reaction('👍')
          await self.client.change_presence(status = discord.Status.dnd, activity = discord.Streaming(name = msg, url = 'https://twitch.tv/mr.bot'))
          return
        elif status == 'idle':
          await ctx.message.add_reaction('👍')
          await self.client.change_presence(status = discord.Status.idle, activity = discord.Streaming(name = msg, url = 'https://twitch.tv/mr.bot'))
          return

      elif game == 'game':
        if status == 'online':
          await ctx.message.add_reaction('👍')
          await self.client.change_presence(status = discord.Status.online, activity = discord.Game(msg))
          return
        elif status == 'dnd':
          await ctx.message.add_reaction('👍')
          await self.client.change_presence(status = discord.Status.dnd, activity = discord.Game(msg))
          return
        elif status == 'idle':
          await ctx.message.add_reaction('👍')
          await self.client.change_presence(status = discord.Status.idle, activity = discord.Game(msg))
          return


  @commands.command()
  async def restatus(self, ctx):
    if ctx.author.id != 275065846836101120 and ctx.author.id != 125492204234997761:
      await ctx.message.add_reaction('👎')
      return
  
    else:
      anime = [
        'Spirited Away',
        'Steins;Gate',
        'Your Name',
        'My Hero Academia',
        'Howl\'s Moving Castle',
        'Fullmetal Alchemist: Brotherhood',
        'Attack on Titan',
        'No Game No Life',
        'Assassination Classroom',
        'Re:Zero',
        'Darling in the Franxx',
        'Bunny Girl Senpai',
        'Black Lagoon',
        'Future Diary',
        'Guilty Crown',
        'Zetsuen no Tempest',
        'Chuunibyou',
        'Your Lie in April',
        'A Silent Voice',
        'Charlotte',
        'Dragon Maid',
        'Kimetsu no Yaiba',
        'Rising of the Shield Hero',
        'Quintessential Quintuplets',
        'The girl who leapt through time',
        'Soul Eater',
        'Fairy Tail',
        'One Punch Man',
        'Danmachi'
      ]

      show = random.choice(anime)
      await ctx.message.add_reaction('👍')
      await self.client.change_presence(status = discord.Status.online, activity = discord.Streaming(name = show, url = 'https://twitch.tv/mr.bot'))


  @commands.command()
  async def prefix(self, ctx, prefix):
    if ctx.author.id != 275065846836101120:
      await ctx.message.add_reaction('👎')
      return

    else:
      with open('json/prefix.json', 'r') as f:
        prefixes = json.load(f)

      prefixes[str(ctx.guild.id)] = prefix

      with open('json/prefix.json', 'w') as f:
        json.dump(prefixes, f, indent = 2)
    
      await ctx.message.add_reaction('👍')


  @commands.command()
  async def delete(self, ctx, id):
    if ctx.author.id != 275065846836101120:
      await ctx.message.add_reaction('👎')
      return
  
    else:
      message = await ctx.fetch_message(id)

      if message.author.id != 705683895055679521:
        await ctx.message.add_reaction('👎')
        return

      else:
        await ctx.message.add_reaction('👍')
        await message.edit(delete_after = 0)


  @commands.command()
  async def getsay(self, ctx, user, index):
    if ctx.author.id != 275065846836101120:
      await ctx.message.add_reaction('👎')
      return
  
    else:
      with open('json/say.json', 'r') as f:
        said = json.load(f)

      user = user[3:]
      length = len(user)
      user = user[:length - 1]

      messages = said[str(user)]
      message = messages[int(index)]

      await ctx.send('<@' + str(user) + '>' + ' said ' + message)
  

  @commands.command()
  async def saylen(self, ctx, user):
    if ctx.author.id != 275065846836101120:
      await ctx.message.add_reaction('👎')
      return
 
    else:
      with open('json/say.json', 'r') as f:
        said = json.load(f)

      user = user[3:] #slice username to make sure its only the digits
      length = len(user)
      user = user[:length - 1]

      messages = said[str(user)]

      await ctx.send(len(messages))




def setup(bot):
  bot.add_cog(me(bot))