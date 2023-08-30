#This code is by Castmax1311 (some Code by EnderKatze)
#Github repository: https://github.com/Castmax1311/katzcraft-studios-discord-bot
#Discord Server: https://discord.gg/ekCHh2Kfkn

import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from utils.MoneyManager import MoneyManager

import random

class GamesCog(commands.Cog):

    def __init__(self, bot):

        self.bot: commands.Bot = bot

    @slash_command(description="A dice from 1-6")
    async def dice(self, ctx, choice: Option(str, description="Choose a number between 1 and 6", required=True, choices=["1", "2", "3", "4", "5", "6"]), money: Option(int, min_value=1, required=True, description="Choose your bet")):
        moneyManager = MoneyManager()

        if choice.lower() not in ["1", "2", "3", "4", "5", "6"]:
            await ctx.respond("Please choose a number between 1 and 6")
            return

        user_id = ctx.author.id
        user_money = moneyManager.getMoney(user_id)

        if user_money < money:
            embed = discord.Embed(title="Error", description="You don't have enough money to play", color=0xff0000)
            embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
            await ctx.respond(embed=embed)
            return

        result = random.choice(["1", "2", "3", "4", "5", "6"])
        if choice.lower() == result:
            moneyManager.addMoney(user_id, money * 5)
            embed = discord.Embed(color=0x00ff59)
            embed.add_field(name="Result:", value="Congratulations, you won! Your bet was multiplied sixfold", inline=False)
        else:
            moneyManager.addMoney(user_id, -money)
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name="Result:", value=f"Too bad, you lost. Your bet of {money} KatzCoins is gone...", inline=False)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
        await ctx.respond(embed=embed)

    @slash_command(description="Play Rock, Paper, Scissors")
    async def rockpaperscissors(self, ctx, choice: Option(str, description="Choose 'rock', 'paper' or 'scissors'", required=True, choices=["rock", "paper", "scissors"]),
                   money: Option(int, min_value=1, required=True, description="Choose your bet")):
        moneyManager = MoneyManager()

        if choice.lower() not in ["rock", "paper", "scissors"]:
            await ctx.respond("Choose 'rock', 'paper' or 'scissors'")
            return

        user_id = ctx.author.id
        user_money = moneyManager.getMoney(user_id)

        if user_money < money:
            embed = discord.Embed(title="Error", description="You don't have enough money to play", color=0xff0000)
            embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
            await ctx.respond(embed=embed)
            return

        result = random.choice(["rock", "paper", "scissors"])
        if choice.lower() == result:
            moneyManager.addMoney(user_id, money * 2)
            embed = discord.Embed(color=0x00ff59)
            embed.add_field(name="Result:", value="Congratulations, you won! Your bet was tripled",
                            inline=False)
        else:
            moneyManager.addMoney(user_id, -money)
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name="Result:", value=f"Too bad, you lost. Your bet of {money} KatzCoins is gone...", inline=False)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
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
            embed = discord.Embed(title="Error", description="You don't have enough money to play", color=0xff0000)
            embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
            await ctx.respond(embed=embed)
            return

        result = random.choice(["head", "tail"])
        if choice.lower() == result:
            moneyManager.addMoney(user_id, money)
            embed = discord.Embed(color=0x00ff59)
            embed.add_field(name="Result:", value="Congratulations, you won! Your bet was doubled", inline=False)
        else:
            moneyManager.addMoney(user_id, -money)
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name="Result:", value=f"Too bad, you lost. Your bet of {money} KatzCoins is gone...", inline=False)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(GamesCog(bot))