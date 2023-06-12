import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension
import random

with open("data.json","r",encoding="utf8") as file:
    jfile = json.load(file)

class React(Cog_Extension): #繼承 Cog 類別  


    @commands.command()
    async def pic(self,ctx):
        r_pic = random.choice(jfile["picture"])
        await ctx.send(r_pic)


async def setup(bot):
    await bot.add_cog(React(bot))