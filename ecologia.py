import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "$", intents=intents)

@bot.event
async def on_ready():
    print(f"Hai fatto accesso come {bot.user}")

@bot.command()
async def ciao(ctx):
    await ctx.send(f"Ciao! Sono un bot {bot.user}!")

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def plastica(ctx):
    await ctx.send(f"Riduci la quantità di plastica utilizzata in casa")

bot.run("TOKEN")
