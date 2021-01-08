import discord
import os
import traceback
import random

token = os.environ['DISCORD_BOT_TOKEN']
intents = discord.Intents.all()
intents.typing = False
client = discord.Client(intents=intents)

def hello(user_name):
    hello_list = ['@' + user_name + '！こんにちは！ヒヒン！', '@' + user_name + '！元気だった？ヒヒン？', '今日馬レースする？' + user_name + 'ヒヒン？']
    return random.choice(hello_list)

def drown():
    drown_list = ['ぶくぶくぶく...(白目)', 'ひ、ひ、ひひん...(白目)']

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if 'こんにちは' in message.content:
        await message.channel.send(hello(message.author.name))
    if '水' in message.content or 'みず' in message.content:
        await message.channel.send(drown())

@client.event
async def on_member_join(member):
    print('member join:' + member.display_name)
    for channel in member.server.channels:
        print('member join 2:' + channel.name)
        if channel.name == 'general' or channel.name == '一般':
            print('member join 3:' + channel.name)
            await client.send_message(channel, member.display_name + 'ちゃん初めましてだヒヒン!')

client.run(token)
