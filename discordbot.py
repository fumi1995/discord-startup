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

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == 'general' or channel.name == '一般':
            await client.send_message(channel, member.display_name + 'ちゃん初めましてだヒヒン!')

client.run(token)
