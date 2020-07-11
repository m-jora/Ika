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

    mem = ctx.guild.get_member(705683895055679521)
    name = mem.display_name
    pfp = mem.avatar_url
  
    if message == '':
      embed = discord.Embed(
        title = '**COMMANDS**',
        url = 'https://hheselbarth.gitbook.io/mr-bot/',
        description = ' <> = required arguments, [] = optional.',
        colour = 0xFFC500
      )

      embed.set_footer(text = 'Replying to: ' + str(ctx.author))
      embed.set_thumbnail(url = 'https://i.imgur.com/mqrgVsu.gif')
      embed.set_author(name = name, icon_url = pfp)
      embed.add_field(name = '**MYANIMELIST**', value = 'Type `' + prefix + 'help mal`', inline = False)
      embed.add_field(name = '**GENERAL**', value = 'Type `' + prefix + 'help general`', inline = False)
      embed.add_field(name = '**IMAGES**', value = 'Type `' + prefix + 'help images`', inline = False)
      embed.add_field(name = 'For any help with Ika join our support server', value = '[Join](https://discord.com/invite/xG7HEHu)')
      embed.add_field(name = 'If you like Ika please consider voting!', value = '[Vote](https://top.gg/bot/705683895055679521/vote)')
      

      await ctx.send(embed = embed)
      return

    elif message == 'general' or message == 'General':
      embed = discord.Embed(
        title = '**GENERAL COMMANDS**',
        url = 'https://hheselbarth.gitbook.io/mr-bot/',
        description = ' <> = required arguments, [] = optional.',
        colour = 0xFFC500
      )

      embed.set_footer(text = 'Replying to: ' + str(ctx.author))
      embed.set_thumbnail(url = 'https://i.imgur.com/mqrgVsu.gif')
      embed.set_author(name = name, icon_url = pfp)
      embed.add_field(name = '**' + prefix + '8ball <questions for 8ball>**', value = 'Ask the Magic 8Ball questions', inline = False)
      embed.add_field(name = '**' + prefix + 'botstatus**', value = 'Sends status and info on bot.', inline = False)
      embed.add_field(name = '**' + prefix + 'choose <item1> <item2>**', value = name + ' chooses between two items given', inline = False)
      embed.add_field(name = '**' + prefix + 'flip**', value = 'Flips a coin')
      embed.add_field(name = '**' + prefix + 'help**', value = 'Shows help options')
      embed.add_field(name = '**' + prefix + 'say <message to repeat>**', value = name + ' repeats message given', inline = False)
      embed.add_field(name = '**' + prefix + 'userinfo [user]**', value = 'Returns information on the given user', inline = False)

      await ctx.send(embed = embed)
      return


    elif message == 'mal' or message == 'MAL':
      embed = discord.Embed(
        title = '**MAL COMMANDS**',
        url = 'https://hheselbarth.gitbook.io/mr-bot/',
        description = ' <> = required arguments, [] = optional.',
        colour = 0xFFC500
      )

      embed.set_footer(text = 'Replying to: ' + str(ctx.author))
      embed.set_thumbnail(url = 'https://i.imgur.com/mqrgVsu.gif')
      embed.set_author(name = name, icon_url = pfp)
      embed.add_field(name = '**'  + prefix + 'account <mal username>**', value = 'Displays account information for given username', inline = False)
      embed.add_field(name = '**' + prefix + 'ani <anime title>**', value = 'Displays detailed information on the title given', inline = False)
      embed.add_field(name = '**' + prefix + 'anisearch <anime title>**', value = 'Displays top 5 search results for given title on MAL', inline = False)
      embed.add_field(name = '**' + prefix + 'aniseason <year> <season>**', value = 'Gives information on anime from given season', inline = False)
      embed.add_field(name = '**' + prefix + 'manga <manga title>**', value = 'Displays detailed information on the title given', inline = False)
      embed.add_field(name = '**' + prefix + 'mangasearch <manga title>**', value = 'Displays top 5 search results for given title on MAL', inline = False)
      embed.add_field(name = '**' + prefix + 'schedule [m,t,w,r,f,s,su]**', value = 'Gives information on shows airing the given day or whole week if no day is given', inline = False)

      await ctx.send(embed = embed)
      return


    elif message == 'images' or message == 'Images':
      embed = discord.Embed(
        title = '**IMAGE COMMANDS**',
        url = 'https://hheselbarth.gitbook.io/mr-bot/',
        description = ' <> = required arguments, [] = optional.',
        colour = 0xFFC500
      )

      embed.set_footer(text = 'Replying to: ' + str(ctx.author))
      embed.set_thumbnail(url = 'https://i.imgur.com/mqrgVsu.gif')
      embed.set_author(name = name, icon_url = pfp)

      embed.add_field(name = '**' + prefix + 'avatar [user]**', value = 'Sends users avatar as embed', inline = False)
      embed.add_field(name = '**' + prefix + 'cat**', value = 'Sends random cat pictures', inline = False)
      embed.add_field(name = '**' + prefix + 'dog [breed]**', value = 'Sends random dog pictures', inline = False)
      embed.add_field(name = '**' + prefix + 'inspire**', value = name + ' sends an inspirational image', inline = False)
      embed.add_field(name = '**' + prefix + 'mathfun [1, 2, or 3]**', value = '***mathfun***', inline = False)
      

      await ctx.send(embed = embed)
      return

    else:
      return

def setup(bot):
  bot.add_cog(hlp(bot))



