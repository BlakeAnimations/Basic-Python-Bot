import discord

from discord.ext import commands

Client = commands.Bot(command_prefix="S.")

Client.sniped_messages = {}

@Client.command()

async def Hello(ctx):

  await ctx.send('Hello!')

@Client.command()

async def ping(ctx):

    pongEmbed = discord.Embed(

        title="Ping command.",

        description=

        (f':ping_pong: Pong! {round(Client.latency * 100)}ms'),

        color=0x00ff00)

    await ctx.send(embed=pongEmbed)

@Client.command()

async def add(ctx, left: int, right: int):

    """Adds two numbers together."""

    await ctx.send(left + right)

@Client.event

async def on_ready():

    await Client.change_presence(status=discord.Status.online,

                                 activity=discord.Game("Minecraft"))

    print('Logged in as')

    print(Client.user.name)

    print(Client.user.id)

    print(

        'Token used: TOKENHERE'

    )

    print('------')

    print("Bot has started in a non-error state.")

@Client.command()

@commands.has_permissions(view_audit_log=True)

async def warn(ctx, member: discord.Member, *, reason=None):

    await ctx.send(

        f"Member warned. {ctx.author} warned {member} for the following reason: "

        + reason)

    await ctx.message.delete()

@Client.command()

async def kick(ctx):

    await ctx.send(

        "This command is currently being developed while you wait, try the lastest command: S.Hello"

    )

@Client.command()

async def credits(ctx):

    creditEmbed = discord.Embed(

        title="Credits.",

        description=

        "The bot has been made fully by BlakeAnimtions and no one else has helped so far.",

        color=0x00ff00)

    creditEmbed.set_footer(text="This bot is made in Python.")

    await ctx.send(embed=creditEmbed)

Client.run("TOKENHERE")
