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
        await message.channel.send('こんにちはヒヒーン')

client.run(token)
