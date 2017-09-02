import discord
from time import sleep
from random import randint

PREFIX = "dev_"
TOKEN = "token"

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
    if message.content.startswith(PREFIX):
        global messages
        valid = False
        print("command detected")
        if message.content == PREFIX + "clear":
            await _clear(message)
        elif message.content == PREFIX + "roll":
            valid = True
            await _roll(message)
        if valid:
            messages.append(message)

async def _clear(message):
    global messages
    msg = await client.send_message(message.channel, 'Clearing...')
    messages.append(msg)
    for msg in messages:
        await client.delete_message(msg)
    await client.delete_message(message)
    deleted = len(messages)
    msg = await client.send_message(message.channel, 'Deleted ' + str(deleted) + ' messages')
    messages = []
    sleep(5)
    await client.delete_message(msg)

async def _roll(message):
        global messages
        rand = randint(1, 6)
        msg = await client.send_message(message.channel, rand)
        messages.append(msg)


client.run(TOKEN)
