# mod.py
'''cotains commands useful for moderation'''


async def clear(ctx, amount):
  if amount <= 0:
    return
  else:
    await ctx.channel.purge(limit = amount)

async def kick(ctx, member, reason):
  await member.kick(reason = reason)
  await ctx.send(f'Banned {member.mention}')

async def ban(ctx, member, reason):
  await member.ban(reason = reason)
  await ctx.send(f'Banned {member.mention}')

async def unban(ctx, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'Unbanned {user.mention}')
      return









