import discord
from discord.ext import commands
from discord.commands import slash_command


class ProgressCog(commands.Cog):

    def __init__(self, bot):

        self.bot: commands.Bot = bot

    @slash_command(description="Look at the progress", guild_ids=[798881392435134464, 906164029523890217])
    async def progress(self, ctx):
        embed = discord.Embed(title="Progress", description="View the progress", color=0xff8800)
        embed.add_field(name="Add normal commands:", value="35%", inline=False)
        embed.add_field(name="Economy system:", value="40%", inline=False)
        embed.add_field(name="Leveling system:", value="100%", inline=False)
        embed.add_field(name="Add moderation commands:", value="40%", inline=False)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(ProgressCog(bot))