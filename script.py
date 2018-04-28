import discord
import asyncio
import config

client = discord.Client()

def username(user):
    res = user.name
    if user.nick:
        res = "{} ({})".format(user.nick, user.name)
    return res

def sanitize(msg):
    return msg.replace("\n", "\\n").replace("`", " \` ")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("!help"):
        await client.send_message(message.channel, "no")

@client.event
async def on_message_delete(message):
    if message.author == client.user:
        return
    content_sanitized = sanitize(message.clean_content)
    author = username(message.author)
    await client.send_message(message.channel, "[deleted] {}: {}".format(author, content_sanitized))

@client.event
async def on_message_edit(before, after):
    if before.author == client.user or before.clean_content == after.clean_content:
        return
    author = username(before.author)
    before_sanitized = sanitize(before.clean_content)
    after_sanitized = sanitize(after.clean_content)
    await client.send_message(before.channel, "[edited] {}:\nfrom: {}\nto: {}".format(author, before_sanitized, after_sanitized))

client.run(config.token)
