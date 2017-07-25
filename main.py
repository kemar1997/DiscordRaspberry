import discord
import config
from discord.ext import commands
import asyncio
import random
# import schedule
import time

# actual bot itself
bot = commands.Bot(command_prefix="!")
fightResponses = ["%s fell to the floor, 'accidentally'. KO >:)",
                  "Somehow I managed to knockout %s with my :fist:",
		  "%s likes to throwdown... Too bad my fists are made of steel",
		  "Oops my fist meet %s face",
                  "My fists felt like hurting someone... Sorry, %s! :punch:"]

commandsList = [
   '!doc (github page)',
   '!commands',
   '!test',
   '!hellotts (sends a custom text-to-speech message)',
   '!echo (this command requires a string)',
   '!fight',
   '!slave (this command requires a string)',
   '!noslave',
   '!choice (chooses from a comma-delimited list)',
   '!guess (starts a small number guessing game)',
   '!doc (link to github repo)'
]

@bot.async_event
def on_ready():
	print("Logging in")
	print(bot.user.name)
	print(bot.user.id)
	print("------------")

@bot.async_event
def on_message(message):
	# stops the bot from replying to itself
	if message.author == bot.user:
		return
	
	if message.content.startswith('!guess'):
		yield from bot.send_message(message.channel, 'Guess a number 1 to 100')
		
		def guess_check(m):
			return m.content.isdigit()

		guess = yield from bot.wait_for_message(timeout=12.0, author=message.author, check=guess_check)
		answer = random.randint(1, 100)

		if guess is None:
			fmt = 'Sorry, you took too long. It was {}.'
			yield from bot.send_message(message.channel, fmt.format(answer))
			return
		if int(guess.content) == answer:
			yield from bot.send_message(message.channel, 'You are right!')
		else:
			yield from bot.send_message(message.channel, 'Sorry. It is actually {}.'.format(answer))


# Welcomes new members to a server
@bot.async_event
def on_member_join(member):
	server = member.server
	msg = 'Hello World! {0.mention}, Welcome to {1.name}!'
	yield from bot.send_message(server, msg.format(member, server))

# some custom commands
@bot.command()
@asyncio.coroutine
def test():
	yield from bot.say("Testing... Testing?")

@bot.command()
@asyncio.coroutine
def doc():
	git_url = "https://github.com/kemar1997/DiscordRaspberry"
	yield from bot.say("My main code is on this github page: " + git_url)

@bot.command()
@asyncio.coroutine
def commands():
	# add a list of commands here
	yield from bot.say(' '.join(commandsList))

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
	elif member.id == "276233346286092291" and member.id == ctx.message.author.id:
		yield from bot.say(ctx.message.author.mention + (": Are you sure "
		"my creator?"))

	# checks if the bot is trying to fight me but I am not sending the message
	elif member.id == "276233346286092291":
		yield from bot.say(ctx.message.author.mention + (": Why must "
		"I fight with my creator?... He is the best."))

	# checks if someone else calls the fight command on themselves
	elif member.id == ctx.message.author:
		yield from bot.say(ctx.message.author.mention + (": Why do "
		"you want me to fight with you?"))

	else:
		random.seed(time.time())
		choice = fightResponses[random.randrange(len(fightResponses))] % member.mention
		yield from bot.say(ctx.message.author.mention + ": " + choice)

@bot.command(pass_context = True)
@asyncio.coroutine
def choice(ctx, *, choices: str):
	choicesArr = choices.split(",")
	chosen = choicesArr[random.randrange(len(choicesArr))]
	yield from bot.say(ctx.message.author.mention + ": I choose " + chosen)

@bot.command(pass_context = True)
@asyncio.coroutine
def slave(ctx):
	for member in ctx.message.server.members:
		try:
			yield from bot.change_nickname(member, "DRslave " + member.name)
		except discord.errors.Forbidden:
			pass
	yield from bot.say(ctx.message.author.mention + ": Everyone is now a "
			   "slave of DiscordRaspberry!! :smirk_cat:")

@bot.command(pass_context = True)
@asyncio.coroutine
def noslave(ctx):
	for member in ctx.message.server.members:
		try:
			yield from bot.change_nickname(member, member.name)
		except discord.errors.Forbidden:
			pass
	yield from bot.say(ctx.message.author.mention + ": Everyone's name has "
			   "been restored.")

# worked out the problem just by passing ctx into the function
@bot.command(pass_context = True)
@asyncio.coroutine
def hellotts(ctx):
	yield from bot.send_message(ctx.message.channel, 'Hello, everyone... I am '
				    'DiscordBerry. And, my creator is Kemar', 
				    tts = True)

# @bot.command(pass_context = True)
# @bot.async_event
# def auto(ctx):
#	yield from bot.send_message(ctx.message.channel, "I am DiscordBerry, "
#				    "feel free to use my commands by using "
#				    "!commands to see the other commands I "
#				    "I have to offer.")

# Event handler to automate the message

# schedule.every().hour.do(auto)

# while True:
#	schedule.run_pending()
#	time.sleep(1)
	
bot.run(config.token)
