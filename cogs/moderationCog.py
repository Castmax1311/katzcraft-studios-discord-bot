import discord
from discord.ext import commands
from discord.commands import slash_command

class ModerationCog(commands.Cog):

    def __init__(self, bot):

        self.bot: commands.Bot = bot

    @slash_command(description="View the moderation commands", guild_ids=[798881392435134464, 906164029523890217])
    async def moderation(self, ctx):
        embed = discord.Embed(title="Moderation commands", description="",
                              color=0x0008ff)
        embed.add_field(name="Delete message from a channel:", value="`/clear`", inline=False)
        embed.add_field(name="Kick a member from the server:", value="`/kick`", inline=False)
        embed.add_field(name="Ban a member from the server:", value="`/ban`", inline=False)
        embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
        await ctx.respond(embed=embed)

    @slash_command(description="Delete message from a channel", guild_ids=[798881392435134464, 906164029523890217])
    async def clear(self, ctx, amount: int):
        if ctx.author.guild_permissions.manage_messages:
            await ctx.channel.purge(limit=amount)
            embed = discord.Embed(color=0x00ff59)
            embed.add_field(name=f"{amount} message(s) deleted", value="", inline=False)
            embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name="You don't have the permission to manage messages", value="", inline=False)
            embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
            await ctx.respond(embed=embed)

    @slash_command(description="Kick a member from the server", guild_ids=[798881392435134464, 906164029523890217])
    async def kick(self, ctx, member: discord.Member, reason):
        if ctx.author.guild_permissions.kick_members:
            await member.kick(reason=reason)
            embed = discord.Embed(color=0x00ff59)
            embed.add_field(name=f"{member.name} was kicked", value="", inline=False)
            embed.add_field(name=f"Reason: {reason}", value="", inline=False)
            embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
            await ctx.respond(embed=embed)
            audit_log = f'{ctx.author.name} has kicked {member.name}#{member.discriminator} with the reason: {reason}'
            await ctx.guild.audit_log(reason=audit_log, action=discord.AuditLogAction.kick, target=member)
        else:
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name=f"You don't have the permission to kick members", value="", inline=False)
            embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
            await ctx.respond(embed=embed)

    @slash_command(description="Ban a member from the server", guild_ids=[798881392435134464, 906164029523890217])
    async def ban(self, ctx, member: discord.Member, reason):
        if ctx.author.guild_permissions.ban_members:
            await member.ban(reason=reason)
            embed = discord.Embed(color=0x00ff59)
            embed.add_field(name=f"{member.name} was banned", value="", inline=False)
            embed.add_field(name=f"Reason: {reason}", value="", inline=False)
            embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
            await ctx.respond(embed=embed)
            audit_log = f'{ctx.author.name} has banned {member.name}#{member.discriminator} with the reason: {reason}'
            await ctx.guild.audit_log(reason=audit_log, action=discord.AuditLogAction.kick, target=member)
        else:
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name=f"You don't have the permission to ban members", value="", inline=False)
            embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(ModerationCog(bot))