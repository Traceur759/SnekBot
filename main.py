import discord
from time import sleep
from random import randint

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
client = discord.Client()
messages = []


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith("-"):
        global messages
        valid = False
        print("command detected")
        if message.content == "-clear":
            msg = await client.send_message(message.channel, 'Clearing...')
            messages.append(msg)
            for msg in messages:
                await client.delete_message(msg)
            await client.delete_message(message)
            deleted = len(messages)
            msg = await client.send_message(message.channel, 'Deleted ' + str(deleted) + ' messages')
            messages.append(msg)
            messages = []
        elif message.content == "-roll":
            valid = True
            rand = randint(1, 6)
            print("roll called")
            msg = await client.send_message(message.channel,rand)
            messages.append(msg)
        if valid:
            messages.append(message)

client.run('token')
