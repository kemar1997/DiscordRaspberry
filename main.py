import discord
import config
from discord.ext import commands
import asyncio
import random
import time

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
	fightResponses = ["%s fell to the floor, 'accidentally'. KO >:)",
			  "Somehow I managed to knockout %s with my :fist:",
			  "My fists felt like hurt someone... Sorry, %s! :punch:"]

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


@bot.command(pass_context = True)
@asyncio.coroutine
def fight(ctx, *, member : discord.Member = None):
	if member is None:
		yield from bot.say(ctx.message.author.mention + (": I can't fight "
 		"someone unless you tell me who you want to fight!"))
		return

	if member.id == "330239386526679040":
		yield from bot.say(ctx.message.author.mention + (": You can't "
		"start a fight with me if I start it first :fist:!"))

	# checks if the bot is trying to fight me and I am sending the message
	elif member.id == "276233346286092291" and member.id == ctx.message.author.mention:
		yield from bot.say(ctx.message.author.mention + ": Are you sure "
		"my creator?"))

	# checks if the bot is trying to fight me but I am not sending the message
	elif member.id == "276233346286092291":
		yield from bot.say(ctx.message.author.mention + (": Why must "
		"I fight with my creator?... He is the best."))

	# checks if someone else calls the fight command on themselves
	elif member.id == ctx.message.author:
		yield from bot.say(ctx.message.author.mention + (": Why do "
		"you want me to fight with you?"
	
	else:
		random.seed(time.time())
		choice = fightResponses [random.randrange(len(fightResponses))] % member.mention
		yield from bot.say(ctx.message.author.mention + ": " + choice)

bot.run(config.token)
