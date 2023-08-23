import discord
from discord.ext import commands
from discord.commands import slash_command
import random

class GamesCog(commands.Cog):

    def __init__(self, bot):

        self.bot: commands.Bot = bot

    @slash_command(description="Game list", guild_ids=[798881392435134464, 906164029523890217])
    async def games(self, ctx):
        embed = discord.Embed(title="Game list", description="Currently not many games are available", color=0x00ff59)
        embed.add_field(name="Dice from 1-6:", value="`/dice`", inline=False)
        embed.add_field(name="Play heads or tails:", value="`/headornumber`", inline=False)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
        await ctx.respond(embed=embed)

    @slash_command(description="A dice from 1-6", guild_ids=[798881392435134464, 906164029523890217])
    async def dice(self, ctx):
        number = random.randint(1, 6)
        username = ctx.author.display_name
        embed = discord.Embed(title="Dice", description=" ", color=0x00ff59)
        embed.add_field(name=f"@{username} rolled a:", value=f"{number}", inline=True)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
        await ctx.respond(embed=embed)

    @slash_command(description="Play heads or tails", guild_ids=[798881392435134464, 906164029523890217])
    async def headornumber(self, ctx):
        result = "Head" if random.choice([True, False]) else "Tail"
        embed = discord.Embed(color=0x00ff59)
        embed.add_field(name="The result is:", value=f"{result}", inline=False)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(GamesCog(bot))