# hlp.py
# cotains custom help command

import json
import discord

from discord.ext import commands

class hlp(commands.Cog):

  def __init__(self, bot):
    self.client = bot


  @commands.command()
  async def help(self, ctx, message = ''):
    with open('json/prefix.json', 'r') as f:
      prefixes = json.load(f)

    prefix = prefixes[str(ctx.guild.id)]
  
    if message == '':
      embed = discord.Embed(
        title = '**COMMANDS**',
        url = 'https://hheselbarth.gitbook.io/mr-bot/',
        description = ' <> = required arguments, [] = optional.',
        colour = 0xFFC500
      )

      embed.set_footer(text = 'great day gamers')
      embed.set_thumbnail(url = 'https://i.imgur.com/TXtizHw.png')
      embed.set_author(name = 'Mr. bot', icon_url = 'https://i.imgur.com/NXWb7Ik.png')
      embed.add_field(name = '**MYANIMELIST**', value = 'Type `' + prefix + 'help mal`', inline = False)
      embed.add_field(name = '**GENERAL**', value = 'Type `' + prefix + 'help general`', inline = False)
      #embed.add_field(name = '**MOD**', value = 'Type `~help mod`', inline = False)
 
      await ctx.send(embed = embed)
      return

    elif message == 'general' or message == 'General':
      embed = discord.Embed(
        title = '**GENERAL COMMANDS**',
        url = 'https://hheselbarth.gitbook.io/mr-bot/',
        description = ' <> = required arguments, [] = optional.',
        colour = 0xFFC500
      )

      embed.set_footer(text = 'good day gamers')
      embed.set_thumbnail(url = 'https://i.imgur.com/TXtizHw.png')
      embed.set_author(name = 'Mr. bot', icon_url = 'https://i.imgur.com/NXWb7Ik.png')
      embed.add_field(name = '**' + prefix + '8ball <questions for 8ball>**', value = 'Ask the Magic 8Ball questions', inline = False)
      embed.add_field(name = '**' + prefix + 'Avatar [user]**', value = 'Sends users avatar as embed', inline = False)
      embed.add_field(name = '**' + prefix + 'Botstatus [user]**', value = 'Sends status and info on bot.', inline = False)
      embed.add_field(name = '**' + prefix + 'cat**', value = 'Sends random cat pictures', inline = False)
      embed.add_field(name = '**' + prefix + 'choose <item1> <item2>**', value = 'Mr. bot chooses between two items given', inline = False)
      embed.add_field(name = '**' + prefix + 'dog [breed]**', value = 'Sends random dog pictures', inline = False)
      embed.add_field(name = '**' + prefix + 'flip**', value = 'Flips a coin', inline = False)
      embed.add_field(name = '**' + prefix + 'help**', value = 'Shows help options', inline = False)
      embed.add_field(name = '**' + prefix + 'hi**', value = 'Mr. bot says hello', inline = False)
      embed.add_field(name = '**' + prefix + 'inspire**', value = 'Mr. bot sends an inspirational image', inline = False)
      embed.add_field(name = '**' + prefix + 'mathfun [1, 2, or 3]**', value = '***mathfun***', inline = False)
      embed.add_field(name = '**' + prefix + 'ping**', value = 'pong', inline = False)
      embed.add_field(name = '**' + prefix + 'pizza**', value = 'It does something idk', inline = False)
      embed.add_field(name = '**' + prefix + 'pong**', value = 'ping', inline = False)
      embed.add_field(name = '**' + prefix + 'recat**', value = 'Gives you a new cat if you didn\'t like the old one.', inline = False)
      embed.add_field(name = '**' + prefix + 'redog [breed]**', value = 'Gives you a new dog if you didn\'t like the old one.', inline = False)
      embed.add_field(name = '**' + prefix + 'say <message to repeat>**', value = 'Mr. bot repeats message given', inline = False)
      embed.add_field(name = '**' + prefix + 'userinfo [user]**', value = 'Returns information on the given user', inline = False)

      if ctx.guild.id == 459928054014148608 or ctx.guild.id == 654930414657339403 or ctx.guild.id == 686001936155410453:
        embed.add_field(name = '**' + prefix + 'yeet**', value = 'sends random memes', inline = False)


      await ctx.send(embed = embed)
      return


    elif message == 'mal' or message == 'MAL':
      embed = discord.Embed(
        title = '**MAL COMMANDS**',
        url = 'https://hheselbarth.gitbook.io/mr-bot/',
        description = ' <> = required arguments, [] = optional.',
        colour = 0xFFC500
      )

      embed.set_footer(text = 'all weebs welcome here')
      embed.set_thumbnail(url = 'https://i.imgur.com/TXtizHw.png')
      embed.add_field(name = '**'  + prefix + 'account <mal username>**', value = 'Displays account information for given username', inline = False)
      embed.add_field(name = '**' + prefix + 'ani <anime title>**', value = 'Displays detailed information on the title given', inline = False)
      embed.add_field(name = '**' + prefix + 'anisearch <anime title>**', value = 'Displays top 5 search results for given title on MAL', inline = False)
      embed.add_field(name = '**' + prefix + 'aniseason <year> <season>**', value = 'Gives information on anime from given season', inline = False)
      embed.add_field(name = '**' + prefix + 'manga <manga title>**', value = 'Displays detailed information on the title given', inline = False)
      embed.add_field(name = '**' + prefix + 'mangasearch <manga title>**', value = 'Displays top 5 search results for given title on MAL', inline = False)
      embed.add_field(name = '**' + prefix + 'schedule [m,t,w,r,f,s,su]**', value = 'Gives information on shows airing the given day or whole week if no day is given', inline = False)

      await ctx.send(embed = embed)
      return

    else:
      return

    '''elif message == 'mod' or message == 'Mod':
      embed = discord.Embed(
        title = '**MOD COMMANDS**',
        description = 'Mr. bot mod',
        colour = 0xFFC500
      )

      embed.set_footer(text = 'ok day gamers')
      embed.set_thumbnail(url = 'https://i.imgur.com/TXtizHw.png')
      embed.set_author(name = 'Mr. bot', icon_url = 'https://i.imgur.com/NXWb7Ik.png')
      embed.add_field(name = '**~ban <user id>**', value = 'Bans user passed if calling user has permission', inline = False)
      embed.add_field(name = '**~clear [num messages]**', value = 'deletes number of messages given', inline = False)
      embed.add_field(name = '**~kick <user id>**', value = 'Kicks user passed if calling user has permission', inline = False)
      embed.add_field(name = '**~unban <user id>**', value = 'Unbans user passed if calling user has permission', inline = False)

      await ctx.send(embed = embed)
      return'''

def setup(bot):
  bot.add_cog(hlp(bot))



