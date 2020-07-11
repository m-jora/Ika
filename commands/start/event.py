# event.py
# event handlers from main
import random
import json
import discord

from discord.ext import commands

class event(commands.Cog):

  def __init__(self, bot):
    self.client = bot

  
  @commands.Cog.listener()
  async def on_ready(self):
    anime = [
      'Steins;Gate',
      'Your Name',
      'MHA',
      'FMAB',
      'SnK',
      'NGNL',
      'Re:Zero',
      'DITF',
      'BNA',
      'Future Diary',
      'Guilty Crown',
      'Chuunibyou',
      'A Silent Voice',
      'Charlotte',
      'Dragon Maid',
      'Soul Eater',
      'Fairy Tail',
      'One Punch Man',
      'Danmachi'
    ]

    show = random.choice(anime)

    print(f'{self.client.user} connected')
    print(f'{self.client.user.name} is connected to the following servers:\n')

    for guild in self.client.guilds:
      print(f'  {guild.name} (id: {guild.id})')
    print()
  
    await self.client.change_presence(status = discord.Status.online, activity = discord.Streaming(name = show, url = 'https://twitch.tv/mr.bot'))



  @commands.Cog.listener()
  async def on_message(self, msg: discord.Message):
    if msg.author.bot:
      return



  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    with open('json/prefix.json', 'r') as f:
      prefixes = json.load(f)

    prefixes[str(guild.id)] = 'm.'

    with open('json/prefix.json', 'w') as f:
      json.dump(prefixes, f, indent = 2)



  @commands.Cog.listener()
  async def on_guild_remove(self, guild):
    with open('json/prefix.json', 'r') as f:
      prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('json/prefix.json', 'w') as f:
      json.dump(prefixes, f, indent = 2)



  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandNotFound):
      print('CNF')
    else:
      print(error)
      await ctx.message.add_reaction('⚠️')



def setup(bot):
  bot.add_cog(event(bot))
