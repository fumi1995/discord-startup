import discord
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if 'こんにちは' in message.content:
        m = 'こんにちは' + message.author.name + 'ヒヒーン'
        await message.channel.send(m)

client.run(token)
