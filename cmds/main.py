import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension): #繼承 Cog 類別
        
    @commands.hybrid_command(name="回傳伺服器延遲")
    async def ping(self,ctx):
        await ctx.send("{} (ms)".format(round(self.bot.latency * 1000)))
        
async def setup(bot):
    await bot.add_cog(Main(bot))