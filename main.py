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


bot.run(config.token)
