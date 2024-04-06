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

    @commands.hybrid_command(name="伺服器狀態")
    async def status(self,ctx):
        embed = discord.Embed(title="伺服器狀態",
                      description="--------------------------------------------------------------",
                      colour=0xf59b00,
                      timestamp=datetime.now())

        embed.set_author(name="喜歡你耶",
                        url="https://i.postimg.cc/9QHcW1S6/head.jpg",
                        icon_url="https://i.postimg.cc/9QHcW1S6/head.jpg")

        embed.add_field(name="伺服器延遲",
                        value="** {}ms **".format(round(await self.bot.latency * 1000)),
                        inline=False)
        embed.add_field(name="伺服器人數",
                        value="** {} **".format(await self.bot.users),
                        inline=True)
        embed.add_field(name="在線人數",
                        value="**7 **",
                        inline=True)
        embed.add_field(name="離線人數",
                        value="**19**",
                        inline=True)

        embed.set_image(url="https://i.postimg.cc/MHrhkq4S/Chipi-Chapa-GIF-Chipi-Chapa-Chipi-chipi-Descubre-y-comparte-GIF.gif")

        embed.set_thumbnail(url="https://i.postimg.cc/9QHcW1S6/head.jpg")

        embed.set_footer(text="Example Footer",
                        icon_url="https://slate.dan.onl/slate.png")

        await ctx.send(embed=embed)



async def setup(bot):
    await bot.add_cog(React(bot))