import discord
from discord.commands import slash_command, Option
from discord.ext import commands

from utils.LevelManager import LevelManager
from utils.MoneyManager import MoneyManager


class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def admin(self, ctx, hack: Option(str, required=True, choices=["givemoney", "givexp"]), value: int, user: Option(discord.Member, required=False)):
        author_id = ctx.author.id

        if author_id == 698113221051154453 or author_id == 644902514155585542:

            if user is None:
                user = ctx.author

            if hack == "givemoney":
                moneyManager = MoneyManager()

                moneyManager.addMoney(user.id, value)
                embed = discord.Embed(title="", color=0x414cec)
                embed.add_field(name=f"You manipulated the matrix and gave {value} KatzCoins to {user.name}", value=" ", inline=False)
                embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
                await ctx.respond(embed=embed)

            elif hack == "givexp":
                levelManager = LevelManager(ctx.guild.id)

                levelManager.addExp(user.id, value)
                embed = discord.Embed(title="", color=0x414cec)
                embed.add_field(name=f"You manipulated the matrix and gave {value} Experience points to {user.name}", value=" ", inline=False)
                embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
                await ctx.respond(embed=embed)

            else:
                embed = discord.Embed(title="", color=0xff0000)
                embed.add_field(name="Not a valid hack", value=" ", inline=False)
                embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
                await ctx.respond(embed=embed)

        else:
            embed = discord.Embed(title="", color=0xff0000)
            embed.add_field(name="HOW DARE YOU TRY TO HARNESS THE POWER OF THE MATRIX??? YOU FOOL!!! MUAHAHA!!!", value=" ", inline=False)
            embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(AdminCog(bot))