# info.py
# commands that provide info on the user / bot

import discord

from discord.ext import commands

class info(commands.Cog):

  def __init__(self, bot):
    self.client = bot

  '''sends info for the bot including number of channels, members, and servers'''
  @commands.command()
  async def botstatus(self, ctx):
    embed = discord.Embed(
      title = '**Bot Status**',
      colour = 0x09D2FF
    )

    ids = [
      264445053596991498,
      374071874222686211,
      446425626988249089,
      110373943822540800,
      450100127256936458
    ]

    servers = [guild for guild in self.client.guilds if guild.id not in ids]
    members = sum([len(server.members) for server in servers])
    channel = sum([len(server.channels) for server in servers])

    mem = ctx.guild.get_member(705683895055679521)

    embed.set_thumbnail(url =  mem.avatar_url)
    embed.add_field(name = '**Bot Developer:**', value = 'mJoRa#0002')
    embed.add_field(name = f'**{mem.display_name} is in:**', value = f'{str(len(servers))} servers')
    embed.add_field(name = f'**{mem.display_name} is watching:**', value = f'{str(members)} users')
    embed.add_field(name = f'**{mem.display_name} is watching:**', value = f'{str(channel)} channels')
    embed.set_footer(text = 'Have a nice day :)')

    await ctx.send(embed = embed)


  '''server info command'''
  @commands.command(aliases = ['Sherbert-status'])
  async def server(self, ctx):
    embed = discord.Embed(
      title = f'**{ctx.guild.name}**',
      colour = 0x09D2FF
    )

    embed.set_thumbnail(url = ctx.guild.icon_url)
    embed.add_field(name = '**Server Created:**', value = str(ctx.guild.created_at)[:10])
    embed.add_field(name = '**Server Owner:**', value = f'<@{str(ctx.guild.owner_id)}>')
    embed.add_field(name = '**Number of Members:**', value = len(ctx.guild.members))
    embed.add_field(name = '**Number of Channels:**', value = len(ctx.guild.channels))
    embed.add_field(name = '**Number of Emotes:**', value = len(ctx.guild.emojis))
    embed.add_field(name = '**Number of Roles:**', value = len(ctx.guild.roles))

    await ctx.send(embed = embed)


  '''information about user'''
  @commands.command()
  async def userinfo(self, ctx, user = ''):
    embed = discord.Embed(
      title = '**User Info**',
      colour = 0x09D2FF
    )

    if user is '':
      embed.set_thumbnail(url = ctx.author.avatar_url)
      embed.add_field(name = '**DETAILS**', value = f'```asciidoc\n• Username :: {ctx.author.name}#{str(ctx.author.discriminator)}\n• ID       :: {str(ctx.author.id)}\n• Created  :: {str(ctx.author.created_at)[:10]}\n• Joined   :: {str(ctx.author.joined_at)[:10]}```')
      typ = 'Beepboop, I\'m a bot.' if ctx.author.bot else 'I\'m a Human.'
      embed.add_field(name = '**STATUS**', value = f'```asciidoc\n• Type      :: {typ}\n• Presence  :: {str(ctx.author.status)}```', inline = False)

    # if user is passed in
    else:
      mem = ctx.guild.get_member(int(user[3:-1]))
      embed.set_thumbnail(url = mem.avatar_url)
      embed.add_field(name = '**DETAILS**', value = f'```asciidoc\n• Username :: {mem.name}#{str(mem.discriminator)}\n• ID       :: {str(mem.id)}\n• Created  :: {str(mem.created_at)[:10]}\n• Joined   :: {str(mem.joined_at)[:10]}```')
      typ = 'Beepboop, I\'m a bot.' if mem.bot else 'I\'m a Human.'
      embed.add_field(name = '**STATUS**', value = f'```asciidoc\n• Type      :: {typ}\n• Presence  :: {str(mem.status)}```', inline = False)

    embed.set_footer(text = f'Replying to: {str(ctx.author)}')
    await ctx.send(embed = embed)


  '''sends embed of users avatar'''
  @commands.command()
  async def avatar(self, ctx, user = ''):
    mem = ctx.author if (user is '') else ctx.guild.get_member(int(user[3:-1]))

    embed = discord.Embed(
      title = f'{mem.display_name}\'s Avatar',
      colour = 0x09D2FF,
      url = str(mem.avatar_url)
    )

    embed.set_image(url = mem.avatar_url)
    await ctx.send(embed = embed)


def setup(bot):
  bot.add_cog(info(bot))