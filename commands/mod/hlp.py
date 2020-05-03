# hlp.py

import discord

async def help(ctx, message):
  if message == '':
    embed = discord.Embed(
      title = '**COMMANDS**',
      description = 'Mr. bot needs help',
      colour = 0xFFC500
    )

    embed.set_footer(text = '*great day gamers*')
    embed.set_thumbnail(url = 'https://i.imgur.com/TXtizHw.png')
    embed.set_author(name = 'Mr. bot', icon_url = 'https://i.imgur.com/NXWb7Ik.png')
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

    embed.set_footer(text = '*good day gamers*')
    embed.set_thumbnail(url = 'https://i.imgur.com/TXtizHw.png')
    embed.set_author(name = 'Mr. bot', icon_url = 'https://i.imgur.com/NXWb7Ik.png')
    embed.add_field(name = '**~8ball**', value = 'Ask the Magic 8Ball questions', inline = False)
    embed.add_field(name = '**~banjo**', value = 'Prints worlds worst ascii art', inline = False)
    embed.add_field(name = '**~cat**', value = 'Sends random cat pictures', inline = False)
    embed.add_field(name = '**~clear**', value = 'deletes number of messages given', inline = False)
    embed.add_field(name = '**~dog**', value = 'Sends random dog pictures', inline = False)
    embed.add_field(name = '**~flip**', value = 'Flips a coin', inline = False)
    embed.add_field(name = '**~help**', value = 'Shows help options', inline = False)
    embed.add_field(name = '**~hi**', value = 'Mr. bot says hello', inline = False)
    embed.add_field(name = '**~mathfun**', value = '***mathfun***', inline = False)
    embed.add_field(name = '**~ping**', value = 'pong', inline = False)
    embed.add_field(name = '**~pizza**', value = 'It does something idk', inline = False)
    embed.add_field(name = '**~pong**', value = 'ping', inline = False)
    
    if ctx.author.id == 275065846836101120 or ctx.author.id == 274379254131851264:
      embed.add_field(name = '**~yeet**', value = 'sends random memes', inline = False)


    await ctx.send(embed = embed)
    return


  elif message == 'mod' or message == 'Mod':
    embed = discord.Embed(
      title = '**MOD COMMANDS**',
      description = 'Mr. bot mod',
      colour = 0xFFC500
    )

    embed.set_footer(text = '*ok day gamers*')
    embed.set_thumbnail(url = 'https://i.imgur.com/TXtizHw.png')
    embed.set_author(name = 'Mr. bot', icon_url = 'https://i.imgur.com/NXWb7Ik.png')
    embed.add_field(name = '**~ban**', value = 'Bans user passed if calling user has permission', inline = False)
    embed.add_field(name = '**~kick**', value = 'Kicks user passed if calling user has permission', inline = False)
    embed.add_field(name = '**~unban**', value = 'Unbans user passed if calling user has permission', inline = False)

    await ctx.send(embed = embed)
    return

  else:
    return



