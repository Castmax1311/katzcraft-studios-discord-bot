import discord
from discord.ext import commands
from discord.commands import slash_command


class AboutCog(commands.Cog):

    def __init__(self, bot):

        self.bot: commands.Bot = bot

    @slash_command(description="Check out our website")
    async def website(self, ctx):
        embed = discord.Embed(title="Our website:",
                              description="https://castmax1311.github.io/katzcraft-studios-website/",
                              color=0x0033ff)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
        await ctx.respond(embed=embed)

    @slash_command(description="Check out our YouTube channel")
    async def youtube(self, ctx):
        embed = discord.Embed(title="Our YouTube channel:",
                              description="https://www.youtube.com/@Katzcraft_Studios",
                              color=0x0033ff)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311 & enderkatze")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(AboutCog(bot))