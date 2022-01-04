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
    mem = ctx.guild.get_member(705683895055679521)
    name = mem.display_name
    pfp = mem.avatar_url
  
    if message == '':
      embed = discord.Embed(
        title = '**COMMANDS**',
        url = 'https://hheselbarth.gitbook.io/mr-bot/',
        description = ' <> = required arguments, [] = optional.',
        colour = 0x000CFF
      )


      embed.set_footer(text = f'Replying to: {str(ctx.author)}')
      embed.set_thumbnail(url = 'https://i.imgur.com/mqrgVsu.gif')
      embed.set_author(name = name, icon_url = pfp)
      embed.add_field(name = '**ANIME/MANGA**', value = 'Type `m.help anime`', inline = False)
      embed.add_field(name = '**GENERAL**', value = 'Type `m.help general`', inline = False)
      embed.add_field(name = '**IMAGES**', value = 'Type `m.help images`', inline = False)
      embed.add_field(name = 'For any help with Ika join our support server', value = '[Join](https://discord.com/invite/xG7HEHu)')
      embed.add_field(name = 'If you like Ika please consider voting!', value = '[Vote](https://top.gg/bot/705683895055679521/vote)')
      await ctx.send(embed = embed)


    elif message == 'general' or message == 'General':
      embed = discord.Embed(
        title = '**GENERAL COMMANDS**',
        url = 'https://hheselbarth.gitbook.io/mr-bot/',
        description = ' <> = required arguments, [] = optional.',
        colour = 0x000CFF
      )

      embed.set_footer(text = f'Replying to: {str(ctx.author)}')
      embed.set_thumbnail(url = 'https://i.imgur.com/TXtizHw.png')
      embed.set_author(name = name, icon_url = pfp)
      embed.add_field(name = '**m.8ball <questions for 8ball>**', value = 'Ask the Magic 8Ball questions', inline = False)
      embed.add_field(name = '**m.botstatus**', value = 'Sends status and info on bot.', inline = False)
      embed.add_field(name = '**m.flip**', value = 'Flips a coin')
      embed.add_field(name = '**m.help**', value = 'Shows help options')
      embed.add_field(name = '**m.server**', value = 'Provids information on the current server', inline = False)
      embed.add_field(name = '**m.userinfo [user]**', value = 'Returns information on the given user', inline = False)
      await ctx.send(embed = embed)


    elif message == 'images' or message == 'Images':
      embed = discord.Embed(
        title = '**IMAGE COMMANDS**',
        url = 'https://hheselbarth.gitbook.io/mr-bot/',
        description = ' <> = required arguments, [] = optional.',
        colour = 0x000CFF
      )

      embed.set_footer(text = f'Replying to: {str(ctx.author)}')
      embed.set_thumbnail(url = 'https://i.imgur.com/TXtizHw.png')
      embed.set_author(name = name, icon_url = pfp)
      embed.add_field(name = '**m.avatar [user]**', value = 'Sends users avatar as embed', inline = False)
      embed.add_field(name = '**m.cat**', value = 'Sends random cat pictures', inline = False)
      embed.add_field(name = '**m.do <throw, ahh, wut, dance, idk>**', value = 'Tell Ika to do something', inline = False)
      embed.add_field(name = '**m.dog [breed]**', value = 'Sends random dog pictures', inline = False)
      embed.add_field(name = '**m.inspire**', value = name + ' sends an inspirational image', inline = False)
      await ctx.send(embed = embed)


    elif message == 'anime':
      embed = discord.Embed(
        title = '**ANIME/MANGA COMMANDS**',
        url = 'https://hheselbarth.gitbook.io/mr-bot/',
        description = ' <> = required arguments, [] = optional.',
        colour = 0x000CFF
      )

      embed.set_footer(text = f'Replying to: {str(ctx.author)}')
      embed.set_thumbnail(url = 'https://i.imgur.com/TXtizHw.png')
      embed.set_author(name = name, icon_url = pfp)
      embed.add_field(name = '**m.ani [mal or al] <anime title>**', value = 'Displays detailed information on the title given', inline = False)
      embed.add_field(name = '**m.anilist [anilist username]**', value = 'Displays account information for giver username', inline = False)
      embed.add_field(name = '**m.alremove**', value = 'Remove anilist username connection', inline = False)
      embed.add_field(name = '**m.alset <al username>**', value = 'Connect anilist username to your discord account', inline = False)
      embed.add_field(name = '**m.mal [mal username]**', value = 'Displays account information for given username', inline = False)
      embed.add_field(name = '**m.malset <mal username>**', value = 'Connect mal username to your discord account', inline = False)
      embed.add_field(name = '**m.malremove**', value = 'Remove mal username connection', inline = False)      
      embed.add_field(name = '**m.manga <manga title>**', value = 'Displays detailed information on the title given', inline = False)
      await ctx.send(embed = embed)


def setup(bot):
  bot.add_cog(hlp(bot))