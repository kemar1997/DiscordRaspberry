import discord
import config
from discord.ext import commands
import asyncio

# actual bot itself
bot = commands.Bot(commands_prefix="!")


@client.async_event
def on_ready():
	print("Logging in")
	print(client.user.name)
	print(client.user.id)
	print("------------")


client.run(config.token)
