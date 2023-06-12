import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

with open("data.json","r",encoding="utf8") as file:
    jfile = json.load(file)
    
class Event(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jfile["join_channel"]))
        await channel.send("{} join!".format(member))
    
    @commands.Cog.listener()
    async def on_memeber_remove(self,member):
        channel = self.bot.get_channel(int(jfile["leave_channel"]))
        await channel.send("{} leave!".format(member))
        
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.content.startswith("hi") and message.author != self.bot.user:
            await message.channel.send("hello {}".format(message.author))

async def setup(bot):
    await bot.add_cog(Event(bot))