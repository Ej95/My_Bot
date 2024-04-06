import discord
import json
import random
from discord.ext import commands
import os
import asyncio


with open("data.json","r",encoding="utf8") as file:
    jfile = json.load(file)


intents  = discord.Intents.all()


bot = commands.Bot(command_prefix="/",intents=intents)


@bot.event
async def on_ready():
    print("> Bot is online")
    await bot.tree.sync()


@bot.command()
async def load(ctx,extension):
    await bot.load_extension("cmds.{}".format(extension))
    await ctx.send("Loaded {} done.".format(extension))
    

@bot.command()
async def unload(ctx,extension):
    await bot.unload_extension("cmds.{}".format(extension))
    await ctx.send("Un-loaded {} done.".format(extension))
    
    
@bot.command()
async def reload(ctx,extension):
    await bot.reload_extension("cmds.{}".format(extension))
    await ctx.send("Reloaded {} done.".format(extension))


async def main():
    for filename in os.listdir("./cmds"):
        if filename.endswith(".py"):
            await bot.load_extension("cmds.{}".format(filename[:-3]))
    await bot.start(jfile["token"])

if __name__=="__main__":
    asyncio.run(main())  