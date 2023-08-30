import discord
from discord import Option
from discord.ext import commands
from discord.commands import slash_command
from utils.MoneyManager import MoneyManager
import time
import json


class MoneyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file_path = "./Json/daily_data.json"
        self.daily_data = self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_data(self):
        with open(self.file_path, "w") as file:
            json.dump(self.daily_data, file)

    @slash_command(description="Claim your daily reward")
    async def daily(self, ctx):
        user_id = str(ctx.author.id)

        current_time = time.time()
        last_claim_time = self.daily_data.get(user_id, 0)

        # Calculate time since last claim in seconds
        time_since_last_claim = current_time - last_claim_time

        # Daily reward interval in seconds (24 hours)
        daily_interval = 24 * 60 * 60

        if time_since_last_claim < daily_interval:
            time_left = daily_interval - time_since_last_claim
            embed = discord.Embed(title="Daily reward", description=f"You've already claimed your daily reward. Please wait {int(time_left // 3600)} hours before claiming again.", color=0xff0000)
            embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
            await ctx.respond(embed=embed)
            return

        moneyManager = MoneyManager()  # Assuming MoneyManager is correctly defined
        moneyManager.addMoney(user_id, 100)  # Add 100 money to the user

        # Update last claim time in the data and save it
        self.daily_data[user_id] = current_time
        self.save_data()

        embed = discord.Embed(title="Daily reward", description="Congratulations! You've claimed your daily reward of 100 money", color=0x00ff59)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
        await ctx.respond(embed=embed)

    @slash_command(description="Give money to a member")
    async def pay(self, ctx,
                  user: Option(discord.Member, required=True),
                  amount: Option(int, required=True, min_value=1)):

        if user.id is ctx.author.id:
            embed = discord.Embed(title="Error", color=0xff0000)
            embed.add_field(name="Can't pay yourself money", value=" ", inline=False)
            embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
            await ctx.respond(embed=embed)

        else:
            moneyManager = MoneyManager()

            if moneyManager.getMoney(ctx.author.id) >= amount:

                moneyManager.addMoney(user.id, amount)
                moneyManager.addMoney(ctx.author.id, -amount)

                embed = discord.Embed(title="", color=0x414cec)
                embed.add_field(name=f"You paid {amount} KatzCoins to {user.name}", value=" ", inline=False)
                embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
                await ctx.respond(embed=embed)

            else:
                embed = discord.Embed(title="Error", color=0xff0000)
                embed.add_field(name="You don't have enough money!", value=" ", inline=False)
                embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
                await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(MoneyCog(bot))