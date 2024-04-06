import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension
from openai import AsyncOpenAI

with open(file=r"data.json",encoding="utf8") as file:
    jfile = json.load(file)


class React(Cog_Extension): #繼承 Cog 類別  

    #回傳 AI 的回覆
    @commands.command()
    async def chat(self,ctx,arg):
        client = AsyncOpenAI(api_key=jfile["api_key"])
        res = await client.completions.create(model="gpt-3.5-turbo-instruct",prompt=arg,max_tokens=2048) #等待回覆生成 使用 await 異步
        await ctx.send("{}".format(str(res.choices[0].text)))

    @commands.hybrid_command(name="打招呼")
    async def ping(self,ctx):
        await ctx.send("Hello")



async def setup(bot):
    await bot.add_cog(React(bot))