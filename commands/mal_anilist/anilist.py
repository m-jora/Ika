# anilist.py
# contains anilist  account  commands

import nextcord
import requests
import sqlite3
import random

from nextcord.ext import commands

class alacc(commands.Cog):
  
  def __init__(self, bot):
    self.client = bot  #boot
    self.url = 'https://graphql.anilist.co' #requests url
    self.al = self.client.get_cog('alhelper') 


  '''use to pull user accounts from anilist.co
  makes calls to alaccount to pull account id's
  sends embed of the anilist image for the account'''
  @commands.command()
  async def anilist(self, ctx, message = ''):    
    db = False

    if message is '':
      message = await self.alaccount(ctx, ctx.author.id)
      db = (True if (message is not '') else False)
      
      if message is '':
        await ctx.send('Run m:alset <anilist username> to link anilist account')
        return

    if message[:2] == '<@' and message[-1] == '>':
      message = await self.alaccount(ctx, message[3:-1]); db = True
      if message is '':
        await ctx.send('User has not linked an anilist account'); db = False
        return

    query = '''
        query ($id: Int, $page: Int, $search: String) {
        Page (page: $page, perPage: 10) {
          users (id: $id, search: $search) {
            id
            name
            siteUrl
          }
        }
      }
    ''' 

    variables = {'id': message, 'page':1} if db else {'search': message, 'page':1}
    response = requests.post(self.url, json = {'query' : query, 'variables': variables}).json()
    user = response['data']['Page']['users']
    # user is list of possible users

    if len(user) < 1:
      await ctx.send('User does not exist')
      return

    embed = nextcord.Embed(
      title = f'**{user[0]["name"]}\'s Account**',
      url = f'https://anilist.co/user/{str(message)}',
      colour = 0x000CFF
    )

    # append random into the url to force discord to not pull image from cache
    embed.set_image(url = f'https://img.anili.st/user/{str(user[0]["id"])}?{str(random.randint(0, 9999999))}')
    await ctx.send(embed = embed)


  '''checks database for if account exists within
  if account is in database reutnr the anilist id
  otherwise return an empty string '' 
  does not call other functions just connects with db
  also sends an embed with command if user does not exist in db'''
  async def alaccount(self, ctx, id):
    conn = sqlite3.connect('db/aniac.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT EXISTS (SELECT alid FROM al WHERE userid = ?)', (str(id),))
    data = cur.fetchall()
  
    if [(1,)] == data:
      cur.execute('SELECT alid FROM al WHERE userid = ?', (str(id),))
      data = cur.fetchall()
      conn.close()
      return data[0][0]

    else:
      conn.close()
      return ''


  '''command used to setup account within the db
  makes calls to isaccount to validate account is real
  also calls validate to validate that user has that account
  will react with a check if validation otherwise reacts with x
  '''
  @commands.command()
  async def alset(self, ctx, message = ''):
    if message == '':
      await ctx.send('Please include a username after the command')
      return

    conn = sqlite3.connect('db/aniac.sqlite')
    cur = conn.cursor()

    valid = await self.al.isaccount(message)
    if valid is False:
      await ctx.send('User does not exist')
      return

    connect = await self.al.validate(ctx, message)

    if connect[0] is True:
      cur.execute('INSERT INTO al (userid, username, alid) VALUES (?,?,?)', (str(ctx.author.id), message, str(connect[1])))
      conn.commit()
      conn.close()
      await ctx.message.add_reaction('✅')

    elif connect[0] is False:
      conn.close()
      await ctx.message.add_reaction('❌')


  '''removes user from database by searching their discord id in table
  then reacts with check mark just to confirm you have been deleted'''
  @commands.command()
  async def alremove(self, ctx):
    conn = sqlite3.connect('db/aniac.sqlite')
    cur = conn.cursor()

    cur.execute('DELETE FROM al WHERE userid = ?', (str(ctx.author.id),))
    conn.commit()
    conn.close()

    await ctx.message.add_reaction('✅')


def setup(bot):
  bot.add_cog(alacc(bot))