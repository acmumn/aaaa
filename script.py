import discord
import asyncio
import config

client = discord.Client()

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
    content_sanitized = message.clean_content.replace("\n", "\\n")
    author = message.author.nick or message.author.name
    await client.send_message(message.channel, "[deleted] {}: {}".format(author, content_sanitized))

@client.event
async def on_message_edit(before, after):
    if before.author == client.user or before.clean_content == after.clean_content:
        return
    author = before.author.nick or before.author.name
    before_sanitized = before.clean_content.replace("\n", "\\n")
    after_sanitized = after.clean_content.replace("\n", "\\n")
    await client.send_message(before.channel, "[edited] {}:\nfrom: {}\nto: {}".format(author, before_sanitized, after_sanitized))

client.run(config.token)
