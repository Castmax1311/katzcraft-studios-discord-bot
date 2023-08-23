import discord
from discord.ext import commands
from discord.commands import slash_command


class HelpCog(commands.Cog):

    def __init__(self, bot):

        self.bot: commands.Bot = bot

    @slash_command(description="View all commands", guild_ids=[798881392435134464, 906164029523890217])
    async def help(self, ctx):
        embed = discord.Embed(title="Help", description="The bot is currently under development", color=0x0008ff)
        embed.add_field(name="Play a game:", value="`/games`", inline=False)
        embed.add_field(name="Moderation commands:", value="`/moderation`", inline=False)
        embed.add_field(name="Report bugs / errors here:", value="`/bugreport`", inline=False)
        embed.add_field(name="Look at progress & goals:", value="`/progress`", inline=False)
        embed.add_field(name="Check out the code on GitHub:", value="`/viewcode`", inline=False)
        embed.add_field(name="Check out our website:", value="`/website`", inline=False)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(HelpCog(bot))