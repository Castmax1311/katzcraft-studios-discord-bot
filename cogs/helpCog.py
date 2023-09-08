#This code is by Castmax1311
#Github repository: https://github.com/Castmax1311/katzcraft-studios-discord-bot
#Discord Server: https://discord.gg/ekCHh2Kfkn

import discord
from discord.ext import commands
from discord.commands import slash_command


class HelpCog(commands.Cog):

    def __init__(self, bot):

        self.bot: commands.Bot = bot

    @slash_command(description="View all commands")
    async def help(self, ctx):
        embed = discord.Embed(title="KatzcraftStudios Bot Commands", description="", color=0x0008ff)
        embed.add_field(name="Economy", value="`/games, /pay, /daily`", inline=False)
        embed.add_field(name="Profile **[More features coming soon]**", value="`/stats [In revision]`", inline=False)
        embed.add_field(name="Moderation", value="`/clear, /kick, /ban`", inline=False)
        embed.add_field(name="Support", value="`/bugreport, /progress, /viewcode`", inline=False)
        embed.add_field(name="About Katzcraft Studios", value="`/website, /youtube`", inline=False)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(HelpCog(bot))