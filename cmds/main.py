import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension): #繼承 Cog 類別
        
    @commands.command()
    async def ping(self,ctx): # ctx 代表上下文
        await ctx.send("{} (ms)".format(round(self.bot.latency * 1000)))
        
async def setup(bot):
    await bot.add_cog(Main(bot))