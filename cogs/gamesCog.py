import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from utils.MoneyManager import MoneyManager

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

    @slash_command(description="Play heads or tails")
    async def coinflip(self, ctx, choice: Option(str, description="Choose 'head' or 'tail", required=True, choices=["head", "tail"]), money: Option(int, min_value=1, required=True, description="Choose your bet")):
        moneyManager = MoneyManager()

        if choice.lower() not in ["head", "tail"]:
            await ctx.send("Please choose 'head' or 'tail")
            return

        user_id = ctx.author.id
        user_money = moneyManager.getMoney(user_id)

        if user_money < money:
            await ctx.send("You don't have enough money to play")
            return

        result = random.choice(["head", "tail"])
        if choice.lower() == result:
            moneyManager.addMoney(user_id, money)
            embed = discord.Embed(color=0x00ff59)
            embed.add_field(name="Result:", value="Congratulations, you have won! Your bet was doubled", inline=False)
        else:
            moneyManager.addMoney(user_id, -money)
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name="Result:", value="Too bad, you have lost. Your bet is gone", inline=False)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(GamesCog(bot))