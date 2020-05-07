# hlp.py
# contains the custom help commands

import discord

async def help(ctx, message):
  if message == '':
    embed = discord.Embed(
      title = '**COMMANDS**',
      description = ' <> = required arguments, [] = optional.',
      colour = 0xFFC500
    )

    embed.set_footer(text = 'great day gamers')
    embed.set_thumbnail(url = 'https://i.imgur.com/TXtizHw.png')
    embed.set_author(name = 'Mr. bot', icon_url = 'https://i.imgur.com/NXWb7Ik.png')
    embed.add_field(name = '**MYANIMELIST**', value = 'Type `~help mal`', inline = False)
    embed.add_field(name = '**GENERAL**', value = 'Type `~help general`', inline = False)
    embed.add_field(name = '**MOD**', value = 'Type `~help mod`', inline = False)
  
    await ctx.send(embed = embed)
    return

  elif message == 'general' or message == 'General':
    embed = discord.Embed(
      title = '**GENERAL COMMANDS**',
      description = 'Mr. bot general',
      colour = 0xFFC500
    )

    embed.set_footer(text = 'good day gamers')
    embed.set_thumbnail(url = 'https://i.imgur.com/TXtizHw.png')
    embed.set_author(name = 'Mr. bot', icon_url = 'https://i.imgur.com/NXWb7Ik.png')
    embed.add_field(name = '**~8ball <questions for 8ball>**', value = 'Ask the Magic 8Ball questions', inline = False)
    embed.add_field(name = '**~banjo**', value = 'Prints worlds worst ascii art', inline = False)
    embed.add_field(name = '**~cat**', value = 'Sends random cat pictures', inline = False)
    embed.add_field(name = '**~dog**', value = 'Sends random dog pictures', inline = False)
    embed.add_field(name = '**~flip**', value = 'Flips a coin', inline = False)
    embed.add_field(name = '**~help**', value = 'Shows help options', inline = False)
    embed.add_field(name = '**~hi**', value = 'Mr. bot says hello', inline = False)
    embed.add_field(name = '**~inspire**', value = 'Mr. bot sends an inspirational image', inline = False)
    if ctx.guild.id == 647960154079232041:
      embed.add_field(name = '**~mathfun [1, 2, or 3]**', value = '***mathfun***', inline = False)
    embed.add_field(name = '**~ping**', value = 'pong', inline = False)
    embed.add_field(name = '**~pizza**', value = 'It does something idk', inline = False)
    embed.add_field(name = '**~pong**', value = 'ping', inline = False)
    embed.add_field(name = '**~say <message to repeat>**', value = 'Mr. bot repeats message given', inline = False)
    
    if ctx.guild.id != 647960154079232041:
      embed.add_field(name = '**~yeet**', value = 'sends random memes', inline = False)


    await ctx.send(embed = embed)
    return


  elif message == 'mod' or message == 'Mod':
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
    return

  elif message == 'mal' or message == 'MAL':
    embed = discord.Embed(
      title = '**MAL COMMANDS**',
      description =  'Search MAL for manga and anime',
      colour = 0xFFC500
    )

    embed.set_footer(text = 'all weebs welcome here')
    embed.set_thumbnail(url = 'https://i.imgur.com/TXtizHw.png')
    embed.add_field(name = '**~ani <anime title>**', value = 'Displays detailed information on the title given', inline = False)
    embed.add_field(name = '**~anisearch <anime title>**', value = 'Displays top 5 search results for given title on MAL', inline = False)
    embed.add_field(name = '**~manga <manga title>**', value = 'Displays detailed information on the title given', inline = False)
    embed.add_field(name = '**~mangasearch <manga title>**', value = 'Displays top 5 search results for given title on MAL', inline = False)

    await ctx.send(embed = embed)
    return

  else:
    return



