#This code is by Castmax1311 (some Code by EnderKatze)
#Github repository: https://github.com/Castmax1311/katzcraft-studios-discord-bot
#Discord Server: https://discord.gg/ekCHh2Kfkn

import discord
from discord.ext import commands
from discord.commands import slash_command


class ProgressCog(commands.Cog):

    def __init__(self, bot):

        self.bot: commands.Bot = bot

    @slash_command(description="Look at the progress")
    async def progress(self, ctx):
        embed = discord.Embed(title="Progress", description="View the progress", color=0xff8800)
        embed.add_field(name="Add normal commands:", value="55%", inline=False)
        embed.add_field(name="Add moderation commands:", value="50%", inline=False)
        embed.add_field(name="Economy system:", value="100% :white_check_mark: ", inline=False)
        embed.add_field(name="Leveling system:", value="100% :white_check_mark: ", inline=False)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(ProgressCog(bot))