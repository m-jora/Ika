# alhelper.py
# helps with anilist commands
# i need  help

import discord
import sqlite3
import uuid, requests
import time, asyncio

from discord.ext import commands

QUERY = '''
  query ($id: Int, $page: Int, $search: String) {
  Page (page: $page, perPage: 10) {
    users (id: $id, search: $search) {
      name
      id
      about
    }
  }
}
'''


class alhelper(commands.Cog):
  
  def __init__(self, bot):
    self.client = bot
    self.url = 'https://graphql.anilist.co'


  '''verifies that passed accounts are valid on anilist
     returns True if valid account False otherwise'''
  async def isaccount(self, username):
    variables = {
      'search' : username,
      'page' : 1
    }

    response = requests.post(self.url, json = {'query' : QUERY, 'variables': variables}).json()
    user = response.get('data').get('Page').get('users')

    if len(user) < 1:
      return False

    return True


  '''used to validate a user owns a certain anilist account
  send an embed with instructions on how to verify'''
  async def validate(self, ctx, username):
    conn = sqlite3.connect('db/aniac.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT EXISTS (SELECT userid FROM al WHERE userid = ?)', (str(ctx.author.id),))
    data = cur.fetchall()

    if data == [(1,)]:
      cur.execute('SELECT username FROM al WHERE userid = ?', (str(ctx.author.id),))
      data = cur.fetchall()[0][0]
      conn.close()

      await ctx.send(f'You have already verified the account {data}.\nUse m:alremove if you wish to remove this account.')
      return

    embed = discord.Embed(
      title = '**Account Verification**',
      colour = 0x000CFF
    )

    new_key = uuid.uuid4()
    instructions = '''Within 4 minutes complete the following instructions.
                      • Navigate to [Anilist](https://anilist.co).
                      • Click on settings in the drop down menu in the upper right corner.
                      • Paste the given key into the about box then hit the save button. If the save button does not appear try getting rid of the blank line under it.'''
          
    embed.set_thumbnail(url = 'https://i.imgur.com/0CibkbN.gif')
    embed.add_field(name = 'Key', value = new_key, inline = False)
    embed.add_field(name = 'How to Use Key', value = instructions)

    try:
      channel = await ctx.author.create_dm()
      msg = await channel.send(embed = embed)
    except:
      await ctx.send('Please change Privacy settings to allow DM\'s from me')
      return [False, '']
    
    await ctx.send('I have DMed you the instructions for verifying your account')

    # done is list of values [bool, alid]
    done = await self.ping(new_key, username)

    title = '**Account Has Been Verified**' if done[0] else '**Failed to find the key in your description within time limit**'
    url = 'https://i.imgur.com/DkuetBb.gif' if done[0] else 'https://i.imgur.com/qSCvqai.gif'
    ret_val = [True, done[1]] if done[0] else [False, '']
    
    embed = discord.Embed(
      title = title,
      colour = 0x000CFF
    )

    embed.set_image(url = url)
    await msg.edit(embed = embed)

    await channel.send("After completeing these steps you are free to remove the key from your account.")
    return ret_val


  '''pings the anilist api to check to see if the key is in the given users description'''
  async def ping(self, new_key, username):
    t_end = time.time() + 60 * 4

    variables = {
      'search' : username,
      'page' : 1
    }

    while time.time() < t_end:
      response = requests.post(self.url, json = {'query': QUERY, 'variables': variables}).json()

      user = response.get('data').get('Page').get('users')[0]
      key = user.get('about')
      id = user.get('id')

      await asyncio.sleep(5)
      try:
        if str(new_key) in key:
          return [True, id]
      except TypeError:
        pass

    return [False, id]


def setup(bot):
  bot.add_cog(alhelper(bot))