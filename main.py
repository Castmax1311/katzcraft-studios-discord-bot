import discord
import random
import json

intents = discord.Intents.default()

bot = discord.Bot(
    intents=intents,
    debug_guilds=[]
)
version = '1.0.6'
token = json.load(open("./Json/config.json"))["token"]


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('/help'))
    print(f"{bot.user} is online")

@bot.slash_command(description="View all commands")
async def help(ctx):
    embed = discord.Embed(title="Help", description="The bot is currently under development", color=0x0008ff)
    embed.add_field(name="Play a game:", value="`/games`", inline=False)
    embed.add_field(name="Report bugs / errors here:", value="`/bugreport`", inline=False)
    embed.add_field(name="Look at progress & goals:", value="`/progress`", inline=False)
    embed.add_field(name="Check out the code on GitHub:", value="`/viewcode`", inline=False)
    embed.add_field(name="Check out our website:", value="`/website`", inline=False)
    embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
    await ctx.respond(embed=embed)

@bot.slash_command(description="If you find a bug or error, you can report it here")
async def bugreport(ctx):
    embed = discord.Embed(title="Oh. You found a bug or an error?", color=0xff0000)
    embed.add_field(name="Please report the issue on GitHub and it will be fixed as soon as possible.",
                    value="Thank you!", inline=False)
    embed.add_field(name="To GitHub issues:", value="https://github.com/Castmax1311/katzcraft-studios-discord-bot/issues", inline=False)
    embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
    await ctx.respond(embed=embed)

@bot.slash_command(description="Check out our website")
async def website(ctx):
    embed = discord.Embed(title="Our website:", description="https://castmax1311.github.io/katzcraft-studios-website/",
                          color=0x0033ff)
    embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
    await ctx.respond(embed=embed)

@bot.slash_command(description="Look at the progress")
async def progress(ctx):
    embed = discord.Embed(title="Progress", description="View the progress", color=0xff8800)
    embed.add_field(name="Add normal commands:", value="20%", inline=False)
    embed.add_field(name="Level system:", value="0%", inline=True)
    embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
    await ctx.respond(embed=embed)

@bot.slash_command(description="View the code of the bot")
async def viewcode(ctx):
    embed = discord.Embed(title="Here you can see my code:", color=0x414cec)
    embed.add_field(name="https://github.com/Castmax1311/katzcraft-studios-discord-bot", value=" ", inline=False)
    embed.add_field(name=f"I'm on version {version}", value=" ", inline=False)
    embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
    await ctx.respond(embed=embed)

@bot.slash_command(description="Look at the statisics of users")
async def stats(ctx, member: discord.Member):
    embed = discord.Embed(title="User statistics", color=0x00ffd5)
    embed.set_thumbnail(url=member.avatar.url)
    embed.addield(name="Username", value=member.name, inline=False)
    embed.add_field(name="Joined Discord on", value=member.created_at.strftime("%d.%m.%Y %H:%M:%S"), inline=False)
    embed.add_field(name="Joined Server on", value=member.joined_at.strftime("%d.%m.%Y %H:%M:%S"), inline=False)
    badges = member.public_flags.all()
    badge_str = ', '.join([str(badge[0]).replace("_", " ").title() for badge in badges])
    embed.add_field(name="Badges", value=badge_str, inline=False)
    await ctx.respond(embed=embed)

@bot.slash_command(description="Game list")
async def games(ctx):
    embed = discord.Embed(title="Game list", description="Currently not many games are available", color=0x00ff59)
    embed.add_field(name="Dice from 1-6:", value="`/dice`", inline=False)
    embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
    await ctx.respond(embed=embed)

@bot.slash_command(description="A dice from 1-6")
async def dice(ctx):
    number = random.randint(1, 6)
    username = ctx.author.display_name
    embed = discord.Embed(title="Dice", description=" ", color=0x00ff59)
    embed.add_field(name=f"@{username} rolled a:", value=f"{number}", inline=True)
    embed.set_footer(text="Discord Bot by Katzcraft Studios - castmax1311")
    await ctx.respond(embed=embed)

bot.run(token)
