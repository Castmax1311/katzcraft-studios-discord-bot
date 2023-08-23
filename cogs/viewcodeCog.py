import discord
from discord.ext import commands
from discord.commands import slash_command

version = '1.1'
class ViewcodeCog(commands.Cog):

    def __init__(self, bot):

        self.bot: commands.Bot = bot

    @slash_command(description="View the code of the bot", guild_ids=[798881392435134464, 906164029523890217])
    async def viewcode(self, ctx):
        embed = discord.Embed(title="Here you can see my code:", color=0x414cec)
        embed.add_field(name="https://github.com/Castmax1311/katzcraft-studios-discord-bot", value=" ", inline=False)
        embed.add_field(name=f"I'm on version {version}", value=" ", inline=False)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(ViewcodeCog(bot))