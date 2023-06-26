import discord
from discord.commands import Option

intents = discord.Intents.default()

bot = discord.Bot(
    intents=intents,
    debug_guilds=[]
)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('in programming'))
    print(f"{bot.user} ist online")


@bot.slash_command(description="Grüße einen User")
async def greet(ctx, user: Option(discord.User, "Der User, den du grüßen möchtest")):
    await ctx.respond(f"Hallo {user.mention}")

@bot.slash_command(description="View all commands")
async def help(ctx):
    embed = discord.Embed(title="Help", description="The bot is currently under development", color=0x0008ff)
    embed.add_field(name="Look at progress & goals:", value="`/progress`", inline=False)
    embed.add_field(name="Check out the code on GitHub:", value="`/viewcode`", inline=True)
    embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
    await ctx.respond(embed=embed)

@bot.slash_command(description="Look at the progress")
async def progress(ctx):
    embed = discord.Embed(title="Progress", description="View the progress", color=0xff8800)
    embed.add_field(name="Add normal commands:", value="5%", inline=False)
    embed.add_field(name="Level system:", value="0%", inline=True)
    embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
    await ctx.respond(embed=embed)

bot.run("MTAxNDk5NTQzNTQ4MTQ4NTM0Mg.GZhr8F.yCDwGFamjntqxdfQsYpnV9kq_YoVE3WnufZJrc")