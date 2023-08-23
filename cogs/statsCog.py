import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from utils.LevelManager import LevelManager


class StatsCog(commands.Cog):

    def __init__(self, bot):

        self.bot: commands.Bot = bot

    @slash_command(description="Look at the stats of users", guild_ids=[798881392435134464, 906164029523890217])
    async def stats(self, ctx, member: Option(discord.Member, "Stats of which person? (Optional)", required=False, default=None)):

        if member is None:
            member = ctx.author

        levelManager = LevelManager(ctx.guild.id, "./Json/levels.json")

        level = levelManager.getLevel(member.id)

        embed = discord.Embed(title="Stats of User:", color=0x00ffd5)
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="Username", value=member.name, inline=False)
        embed.add_field(name="Level", value=str(level) + f" ({levelManager.getExpToLevelup(member.id)} to level-up)", inline=False)
        embed.add_field(name="Joined Discord on", value=member.created_at.strftime("%d.%m.%Y %H:%M:%S"), inline=False)
        embed.add_field(name="Joined Server on", value=member.joined_at.strftime("%d.%m.%Y %H:%M:%S"), inline=False)
        badges = member.public_flags.all()
        badge_str = ', '.join([str(badge[0]).replace("_", " ").title() for badge in badges])
        embed.add_field(name="Badges", value=badge_str, inline=False)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(StatsCog(bot))