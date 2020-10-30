# accounts.py
# contains the account commands for mal and anilist

import discord
import sqlite3
import time
import asyncio, aiohttp

from jikanpy import AioJikan
from discord.ext import commands

class malacc(commands.Cog):

  def __init__(self, bot):
    self.client = bot


  @commands.command()
  async def mal(self, ctx, message = ''):
    aio_jikan = AioJikan()
    
    if message == '':
      message = await self.malaccount(ctx, ctx.author.id)

    if message == '':
      return

    async with ctx.channel.typing():

      try:
        user = await aio_jikan.user(username = message)

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

      print(user)

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

      await aio_jikan.close()

      await ctx.send(embed = embed)
      return


  async def malaccount(self, ctx, id):
    conn = sqlite3.connect('/home/hheselbarth/Ikabeta/db/aniac.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT EXISTS (SELECT username FROM mal WHERE userid = ?)', (str(id),))
    data = cur.fetchall()


    if [(1,)] == data:
      cur.execute('SELECT username FROM mal WHERE userid = ?', (str(id),))
      data = cur.fetchall()
      cur.close()
      conn.close()
      return data[0][0]

    else:
      embed = discord.Embed(
        title = '**Run m:malset <mal username>**',
        colour = 0x000CFF
      )
      await ctx.send(embed = embed)
      cur.close()
      conn.close()
      return ''


  @commands.command()
  async def malset(self, ctx, message = ''):
    if message == '':
      await ctx.send('Please include a username after the command')
      return

    conn = sqlite3.connect('/home/hheselbarth/Ikabeta/db/aniac.sqlite')
    cur = conn.cursor()

    valid = await self.isaccount(message)
    if valid is False:
      embed = discord.Embed(
        title = '**User does not exist**',
        colour = 0x000CFF
      )

      await ctx.send(embed = embed)
      return

    cur.execute('SELECT EXISTS (SELECT ? FROM mal)', (str(ctx.author.id),))
    data = cur.fetchall()

    if [(1,)] == data:
      cur.execute('''UPDATE mal SET username = ? WHERE userid = ?''', (message, str(ctx.author.id)))

    else:
      cur.execute('INSERT INTO mal (userid, username) VALUES (?,?)', (str(ctx.author.id), message))
      
    conn.commit()
    cur.close()
    conn.close()

    await ctx.message.add_reaction('✅')


  @commands.command()
  async def malremove(self, ctx):
    conn = sqlite3.connect('/home/hheselbarth/Ikabeta/db/aniac.sqlite')
    cur = conn.cursor()

    cur.execute('DELETE FROM mal WHERE userid = ?', (str(ctx.author.id),))
    conn.commit()
    cur.close()
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