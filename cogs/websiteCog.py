import discord
from discord.ext import commands
from discord.commands import slash_command


class WebsiteCog(commands.Cog):

    def __init__(self, bot):

        self.bot: commands.Bot = bot

    @slash_command(description="Check out our website", guild_ids=[798881392435134464, 906164029523890217])
    async def website(self, ctx):
        embed = discord.Embed(title="Our website:",
                              description="https://castmax1311.github.io/katzcraft-studios-website/",
                              color=0x0033ff)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(WebsiteCog(bot))