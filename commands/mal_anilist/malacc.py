# accounts.py
# contains the account commands for mal and anilist

import discord
import sqlite3
import time

from jikanpy import AioJikan
from discord.ext import commands

class malacc(commands.Cog):

  def __init__(self, bot):
    self.client = bot


  @commands.command()
  async def mal(self, ctx, message = ''):
    aio_jikan = AioJikan()
    

    # if message does not contain username call db function to find user
    # if user does not exist in db message will equal '' and return
    if message == '':
      message = await self.malaccount(ctx, ctx.author.id)
      if message is '': return


    # gives the appears of the bot typing for commands that take a minute
    async with ctx.channel.typing():

      try:
        user = await aio_jikan.user(username = message)

      except:
        await ctx.send('`User not found`')
        return


      # literally just grabbing all my needed data from mal
      # big mess but items are self explanatory by key
      anime = user.get('anime_stats')
      data = {
        'url': user.get('url'),
        'username': user.get('username'),
        'img': ('https://i.imgur.com/9mnjji8.png' if (user.get('image_url') == None) else user.get('image_url')),
        'days': anime.get('days_watched'),
        'avg_score': anime.get('mean_score'),
        'watching': anime.get('watching'),
        'completed': anime.get('completed'),
        'hold': anime.get('on_hold'),
        'dropped': anime.get('dropped'),
        'plan': anime.get('plan_to_watch'),
        'total': anime.get('total_entries'),
        'num_ep': anime.get('episodes_watched')
      }


      embed = discord.Embed(
        title = '**' + data['username'] + '**',
        colour = 0x000CFF,
        url = data['url']
      )


      embed.set_thumbnail(url = data['img'])
      embed.add_field(name = 'Days watched', value = data['days'])
      embed.add_field(name = 'Episodes Watched', value = data['num_ep'])
      embed.add_field(name = 'Avg Score', value = data['avg_score'])
      embed.add_field(name = 'Total number of shows', value = data['total'])
      embed.add_field(name = 'Watching', value = data['watching'])
      embed.add_field(name = 'Completed', value = data['completed'])
      embed.add_field(name = 'Plan to Watch', value = data['plan'])
      embed.add_field(name = 'Dropped', value = data['dropped'])
      embed.add_field(name = 'On hold', value = data['hold'])

      await aio_jikan.close()
      await ctx.send(embed = embed)
      return


  async def malaccount(self, ctx, id):
    conn = sqlite3.connect('db/aniac.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT username FROM mal WHERE userid = ?', (str(id),))
    data = cur.fetchall()
    conn.close()

    if data != []:
      return data[0][0]

    await ctx.send('**Run m.malset <mal username>**')
    return ''


  @commands.command()
  async def malset(self, ctx, message = ''):
    if message == '':
      await ctx.send('Please include a username after the command')
      return

    conn = sqlite3.connect('db/aniac.sqlite')
    cur = conn.cursor()

    valid = await self.isaccount(message)
    if not valid:
      await ctx.send('**User does not exist**')
      return

    cur.execute('SELECT EXISTS (SELECT ? FROM mal)', (str(ctx.author.id),))
    data = cur.fetchall()

    if [(1,)] == data:
      cur.execute('UPDATE mal SET username = ? WHERE userid = ?', (message, str(ctx.author.id)))

    else:
      cur.execute('INSERT INTO mal (userid, username) VALUES (?,?)', (str(ctx.author.id), message))
      
    conn.commit()
    conn.close()

    await ctx.message.add_reaction('✅')


  @commands.command()
  async def malremove(self, ctx):
    conn = sqlite3.connect('db/aniac.sqlite')
    cur = conn.cursor()

    cur.execute('DELETE FROM mal WHERE userid = ?', (str(ctx.author.id),))
    conn.commit()
    conn.close()

    await ctx.message.add_reaction('✅')


  async def isaccount(self, username):
    aio_jikan = AioJikan()
    try:
      await aio_jikan.user(username = username)
      await aio_jikan.close()

    except:
      return False

    return True

def setup(bot):
  bot.add_cog(malacc(bot))