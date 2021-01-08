import discord
import os
import traceback
import random

token = os.environ['DISCORD_BOT_TOKEN']
intents = discord.Intents.all()
intents.typing = False
client = discord.Client(intents=intents)

def hello(user_name):
    hello_list = ['@' + user_name + '！こんにちはだヒヒーン！', '@' + user_name + '！元気だったヒヒン？']
    return random.choice(hello_list)


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if 'こんにちは' in message.content:
        await message.channel.send(hello(message.author.name))
    if '水' in message.content or 'みず' in message.content:
        m = 'ぶくぶくぶく...(白目)'
        await message.channel.send(m)

@client.event
async def on_member_join(member):
    print('member join:' + member.display_name)
    for channel in member.server.channels:
        print('member join 2:' + channel.name)
        if channel.name == 'general' or channel.name == '一般':
            print('member join 3:' + channel.name)
            await client.send_message(channel, member.display_name + 'ちゃん初めましてだヒヒン!')

client.run(token)
