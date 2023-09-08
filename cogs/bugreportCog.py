#This code is by Castmax1311 (some Code by EnderKatze)
#Github repository: https://github.com/Castmax1311/katzcraft-studios-discord-bot
#Discord Server: https://discord.gg/ekCHh2Kfkn

import discord
from discord.ext import commands
from discord.commands import slash_command


class BugreportCog(commands.Cog):

    def __init__(self, bot):

        self.bot: commands.Bot = bot

    @slash_command(description="If you find a bug or error, you can report it here")
    async def bugreport(self, ctx):
        embed = discord.Embed(title="Oh. You found a bug or an error?", color=0xff0000)
        embed.add_field(name="Please report the issue on GitHub and it will be fixed as soon as possible.",
                        value="Thank you!", inline=False)
        embed.add_field(name="To GitHub issues:",
                        value="https://github.com/Castmax1311/katzcraft-studios-discord-bot/issues", inline=False)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(BugreportCog(bot))