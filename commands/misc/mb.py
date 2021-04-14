# mb.py
# handles misc goofy commands that just kinda exist
# rip mr.bot

import random
import discord
import json

from discord.ext import commands


class mb(commands.Cog):

  def __init__(self, bot):
    self.client = bot


  @commands.command(name = '8ball')
  async def _8ball(self, ctx, *, question):
    responses = [
      'As I see it, yes',
      'Ask again later',
      'Better not tell you now',
      'Cannot predict now',
      'Concentrate and ask again',
      'Don\'t count on it',
      'It is certain',
      'It is decidedly so',
      'Most likely',
      'My reply is no',
      'My sources say no',
      'Outlook not so good',
      'Outlook good',
      'Reply hazy, try again',
      'Signs point to yes',
      'Very doubtful',
      'Without a doubt',
      'Yes',
      'Yes - definitely',
      'You may rely on it',
      'Please shake again',
      'Who said I had the answers',
      'Ask someone else',
      'Why would you ask me that?',
    ]

    if question == '':
      await ctx.send('Ask me a question by typing m:8ball <question>')
      return

    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')


  @commands.command() 
  async def flip(self, ctx):
    sides = ['heads','tails',]
    await ctx.send(f'It\'s {random.choice(sides)}')


def setup(bot):
  bot.add_cog(mb(bot))