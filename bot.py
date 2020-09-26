import discord, os, time
from discord.utils import get
from discord.ext import commands

client = discord.Client()
channel = None
msg = None

bot = commands.Bot(command_prefix='!')

messagePath = "message.txt"
messageFile = open(messagePath, "r")
message = messageFile.read()

reactions = ['☎️','⌨️','🖥️','🔢','🖱️','➗','🏢','⌚']

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	channel = client.get_channel(758852192370819122)
	msg = await channel.send(message)
	for emoji in reactions:
		await msg.add_reaction(emoji)

	time.sleep(3)

	while(True):
		reaction,user = await client.wait_for('reaction_add')
		if(reaction.emoji == u'☎️'):
			await user.add_roles(get(user.guild.roles, name="Telecom"))
		elif(reaction.emoji == u'⌨️'):
			await user.add_roles(get(user.guild.roles, name="OS"))
		elif(reaction.emoji == u'🖥️'):
			await user.add_roles(get(user.guild.roles, name="Database Design"))
		elif(reaction.emoji == u'🔢'):
			await user.add_roles(get(user.guild.roles, name="Software Engineering"))
		elif(reaction.emoji == u'🖱️'):
			await user.add_roles(get(user.guild.roles, name="Linux"))
		elif(reaction.emoji == u'➗'):
			await user.add_roles(get(user.guild.roles, name="Discrete Math"))
		elif(reaction.emoji == u'⌚'):
			await user.add_roles(get(user.guild.roles, name="Algorithms"))
		elif(reaction.emoji == u'🏢'):
			await user.add_roles(get(user.guild.roles, name="Data Structures"))
		else:
			print('lol')

client.run('key-here')
