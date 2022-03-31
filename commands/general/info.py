# info.py
# commands that provide info on the user / bot

import discord

from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

class info(commands.Cog):

  def __init__(self, bot):
    self.client = bot

  
  '''sends info for the bot including number of channels, members, and servers'''
  @cog_ext.cog_slash(name = 'botstatus', description = 'Bot Info', guild_ids = [840366699353866271])
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
  @cog_ext.cog_slash(
    name = "Server",
    description = "Server Stats",
    guild_ids = [840366699353866271]
  )
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
  @cog_ext.cog_slash(
    name = "userinfo",
    description = "Info about selected User",
    guild_ids = [840366699353866271],
    options = [
      create_option(
        name = "user",
        description = "pain",
        required = True, 
        option_type = 6
      )
    ]
  )
  async def userinfo(self, ctx, user):
    embed = discord.Embed(
      title = '**User Info**',
      colour = 0x09D2FF
    )

    mem = ctx.guild.get_member(int(user.id))
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
      url = str(mem.display_avatar)
    )

    embed.set_image(url = mem.display_avatar)
    await ctx.send(embed = embed)


def setup(bot):
  bot.add_cog(info(bot))