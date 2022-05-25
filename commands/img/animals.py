# animals.py
# handles the animal commands that send random images

import discord
import json
import aiohttp

from discord.ext import commands


class animals(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    """Sends random dog pictures by pinging the dog api
  sends them good bois"""

    @commands.command(aliases=["puppy", "doggo", "pup", "pupper", "hound", "mutt"])
    async def dog(self, ctx, message=""):
        embed = discord.Embed(colour=0xFF00FF)
        url = (
            "https://dog.ceo/api/breeds/image/random"
            if (message == "")
            else f"https://dog.ceo/api/breed/{message}/images/random"
        )

        async with aiohttp.ClientSession() as session:
            img = (await self.fetch(session, url))["message"]

        embed.set_image(url=img)
        msg = await ctx.fetch_message(int((await ctx.send(embed=embed)).id))
        await msg.add_reaction("🐶")
        await msg.add_reaction("🐕")  # reactions for re-dogging

        return  # returns

    """spooky borzoi for kendall"""

    @commands.command()
    async def borz(self, ctx):
        embed = discord.Embed(colour=0xFF00FF)

        if ctx.author.id == 275719364303519745:
            await ctx.send("Hi Kendall :)")  # Hi kendall

        url = "https://dog.ceo/api/breed/borzoi/images/random"
        async with aiohttp.ClientSession() as session:
            img = (await self.fetch(session, url))["message"]

        embed.set_image(url=img)
        await ctx.send(embed=embed)

    """Sends random cat pictures pinging cat api"""

    @commands.command(aliases=["kitty", "kitten"])
    async def cat(self, ctx):
        embed = discord.Embed(colour=0xFF00FF)
        headers = {"Authorization": "api_key=8589f552-4b09-4ffc-8561-cc6ef4e59018"}
        url = "https://api.thecatapi.com/v1/images/search"

        async with aiohttp.ClientSession(headers=headers) as session:
            img = (await self.fetch(session, url))[0]["url"]

        embed.set_image(url=img)
        msg = await ctx.fetch_message(int((await ctx.send(embed=embed)).id))
        await msg.add_reaction("🐱")  # reaction for re-catting

        with open("json/cat.json", "w+") as f:
            cats = {str(ctx.guild.id): str(msg.id)}  # 0 is arbitrary value
            json.dump(cats, f, indent=2)

        return

    """function used to obtain reponse of api's"""

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.json()


def setup(bot):
    bot.add_cog(animals(bot))
