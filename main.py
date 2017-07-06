import discord
import config
from discord.ext import commands
import asyncio

# actual bot itself
bot = commands.Bot(command_prefix="!")


@bot.async_event
def on_ready():
	print("Logging in")
	print(bot.user.name)
	print(bot.user.id)
	print("------------")

# some custom commands
@bot.command()
@asyncio.coroutine
def test():
	yield from bot.say("Testing... Testing?")

@bot.command()
@asyncio.coroutine
def commands():
	# add a list of commands here
	yield from bot.say("!commands, !test")

@bot.command(pass_context = True)
@asyncio.coroutine
def echo(ctx, *, echo: str):
	yield from bot.delete_message(ctx.message)
	yield from bot.say(":slight_smile: " + echo + " " + ctx.message.author.mention)

bot.run(config.token)
