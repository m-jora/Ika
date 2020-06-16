# info.py
# commands that provide info on the user / bot

import discord

from discord.ext import commands

class info(commands.Cog):

  def __init__(self, bot):
    self.client = bot

  @commands.command()
  async def botstatus(self, ctx):
    embed = discord.Embed(
      title = '**Bot Status**',
      colour = 0x09D2FF
    )

    channel = 0
    for guild in self.client.guilds:
      channel += len(guild.channels)

    members = 0
    for guild in self.client.guilds:
      members += len(guild.members)

    mem = ctx.guild.get_member(705683895055679521)
    name = mem.display_name

    embed.set_thumbnail(url = mem.avatar_url)
    embed.add_field(name = '**Bot Developer:**', value = 'mJoRa#3186')
    embed.add_field(name = '**' + name + ' is in:**', value = str(len(self.client.guilds)) + ' servers')
    embed.add_field(name = '**' + name + ' is watching:**', value = str(members) + ' users')
    embed.add_field(name = '**' + name + 'is watching:**', value = str(channel) + ' channels')
    embed.set_footer(text = 'Have a nice day :)')

    await ctx.send(embed = embed)


  @commands.command()
  async def userinfo(self, ctx, user = ''):
    embed = discord.Embed(
      title = '**User Info**',
      colour = 0x09D2FF
    )

    if user == '':
      embed.set_thumbnail(url = ctx.author.avatar_url)
      embed.add_field(name = '**DETAILS**', value = '```asciidoc\n • Username :: ' + ctx.author.name + '#' + str(ctx.author.discriminator) + '\n • ID       :: ' + str(ctx.author.id) + '\n • Created  :: ' + str(ctx.author.created_at)[:10] + '\n • Joined   :: ' + str(ctx.author.joined_at)[:10] + '```')
      if ctx.author.bot:
        typ =  'Beepboop, I\'m a bot.'

      else:
        typ = 'I\'m Human.'
        
      embed.add_field(name = '**STATUS**', value = '```asciidoc\n• Type      :: ' + typ + '\n• Presence  :: ' + str(ctx.author.status) + '```', inline = False)

    else:
      mem = ctx.guild.get_member(int(user[3:-1]))
      embed.set_thumbnail(url = mem.avatar_url)
      embed.add_field(name = '**DETAILS**', value = '```asciidoc\n • Username :: ' + mem.name + '#' + str(mem.discriminator) + '\n • ID       :: ' + str(mem.id) + '\n • Created  :: ' + str(mem.created_at)[:10] + '\n • Joined   :: ' + str(mem.joined_at)[:10] + '```')
      
      if mem.bot:
        typ =  'Beepboop, I\'m a bot.'

      else:
        typ = 'I\'m Human.'

      embed.add_field(name = '**STATUS**', value = '```asciidoc\n• Type      :: ' + typ + '\n• Presence  :: ' + str(mem.status) + '```', inline = False)

    await ctx.send(embed = embed)


  @commands.command()
  async def avatar(self, ctx, user = ''):
    if user == '':
      name = ctx.author.display_name
      url = str(ctx.author.avatar_url)

    else:
      mem = ctx.guild.get_member(int(user[3:-1]))
      name = mem.display_name
      url = str(mem.avatar_url)

    embed = discord.Embed(
      title = name + '\'s Avatar',
      colour = 0x09D2FF,
      url = url
    )

    if user == '':
      embed.set_image(url = ctx.author.avatar_url)
    
    else:
      embed.set_image(url = mem.avatar_url)

    await ctx.send(embed = embed)
    return


def setup(bot):
  bot.add_cog(info(bot))