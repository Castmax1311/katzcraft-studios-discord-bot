#This code is by Castmax1311 (some Code by EnderKatze)
#Github repository: https://github.com/Castmax1311/katzcraft-studios-discord-bot
#Discord Server: https://discord.gg/ekCHh2Kfkn

import os
import discord
import json

from utils.LevelManager import LevelManager

intents = discord.Intents.default()

bot = discord.Bot(
    intents=intents,
    debug_guilds=[]
)
token = json.load(open("./Json/config.json"))["token"]

cog_files = [f"cogs.{filename[:-3]}" for filename in os.listdir("cogs/") if filename.endswith(".py")]
for cog_file in cog_files:
    try:
        bot.load_extension(cog_file)
    except Exception as exception:
        print(exception)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('/help'))
    print(f"{bot.user} is online")

@bot.event
async def on_message(message):

    author = message.author
    levelManager = LevelManager(guildID=message.guild.id, pathToDatafile="./Json/levels.json")
    levelBefore = levelManager.getLevel(author.id)
    levelManager.addExp(author.id, json.load(open("./Json/config.json"))["expOnMessage"])
    levelAfter = levelManager.getLevel(author.id)

    if levelAfter > levelBefore:
        embed = discord.Embed(title=":tada: LEVEL UP! :tada: ", description="", color=0x00ffd5)
        embed.add_field(name=f"{author.name}, you just advanced to level {levelAfter}!", value="", inline=False)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
        await message.channel.send(embed=embed)


bot.run(token)