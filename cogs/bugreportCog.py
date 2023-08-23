import discord
from discord.ext import commands
from discord.commands import slash_command


class BugreportCog(commands.Cog):

    def __init__(self, bot):

        self.bot: commands.Bot = bot

    @slash_command(description="If you find a bug or error, you can report it here", guild_ids=[798881392435134464, 906164029523890217])
    async def bugreport(self, ctx):
        embed = discord.Embed(title="Oh. You found a bug or an error?", color=0xff0000)
        embed.add_field(name="Please report the issue on GitHub and it will be fixed as soon as possible.",
                        value="Thank you!", inline=False)
        embed.add_field(name="To GitHub issues:",
                        value="https://github.com/Castmax1311/katzcraft-studios-discord-bot/issues", inline=False)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(BugreportCog(bot))