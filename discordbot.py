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
    drown_list = ['ぶくぶくぶく...(白目)', 'ひ、ひ、ひひん...(白目)', '水は飲んでも溺れるなって死んだじいちゃんが言ってたんだ。ヒヒン。']
    return random.choice(drown_list)

async def send_message_default_channel(client, message_text):
    for guild in client.guilds:
        for channel in guild.channels:
            if channel.name == 'general' or channel.name == '一般':
                await channel.send(message_text)

@client.event
async def on_ready():
    print('on_ready')
    #await send_message_default_channel(client, random.choice(['ヒヒーン！参上！', 'おはよー！ヒヒン！']))
    
@client.event
async def on_message_delete(message):
    print('on_message_delete')
    await send_message_default_channel(client, random.choice(['今"'+ message.content +'"ってやつ消した？ヒヒン？']))

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
            await channel.send(member.display_name + 'ちゃん初めましてだヒヒン!')

client.run(token)
