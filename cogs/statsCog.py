#This code is by Castmax1311 (some Code by EnderKatze)
#Github repository: https://github.com/Castmax1311/katzcraft-studios-discord-bot
#Discord Server: https://discord.gg/ekCHh2Kfkn

import discord
from discord.ext import commands
from discord.commands import slash_command, Option

from utils import ImageUtils
from utils.LevelManager import LevelManager
from utils.MoneyManager import MoneyManager


class StatsCog(commands.Cog):

    def __init__(self, bot):

        self.bot: commands.Bot = bot

    @slash_command(description="Look at the stats of users")
    async def stats(self, ctx, member: Option(discord.Member, "Stats of which person? (Optional)", required=False, default=None)):

        await ctx.defer()

        if member is None:
            member = ctx.author

        levelManager = LevelManager(ctx.guild.id)

        level = levelManager.getLevel(member.id)

        moneyManager = MoneyManager()

        money = moneyManager.getMoney(member.id)

        embed = discord.Embed(title="Stats of User:", color=0x00ffd5)
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="Username", value=member.name, inline=False)
        embed.add_field(name="Level", value=str(level) + f" ({levelManager.getExpToLevelup(member.id)} to level-up)", inline=False)
        embed.add_field(name="Money", value=f" {money} KatzCoin(s)", inline=False)
        embed.add_field(name="Joined Discord on", value=member.created_at.strftime("%d.%m.%Y %H:%M:%S"), inline=False)
        embed.add_field(name="Joined Server on", value=member.joined_at.strftime("%d.%m.%Y %H:%M:%S"), inline=False)
        badges = member.public_flags.all()
        badge_str = ', '.join([str(badge[0]).replace("_", " ").title() for badge in badges])
        embed.add_field(name="Badges", value=badge_str, inline=False)

        await ctx.respond(embed=embed, file=ImageUtils.CreateProfileImage().getImage(member, "yellow_hills"))

def setup(bot):
    bot.add_cog(StatsCog(bot))