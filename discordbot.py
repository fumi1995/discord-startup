import discord
import os
import traceback
import random

token = os.environ['DISCORD_BOT_TOKEN']
intents = discord.Intents.all()
intents.typing = False
client = discord.Client(intents=intents)

def hello(user_name):
    hello_list = [user_name + '！こんにちは！ヒヒン！', user_name + '！元気だった？ヒヒン？', user_name + 'さん今日馬レースする？ヒヒン？']
    return random.choice(hello_list)

def goodbye(user_name):
    goodbye_list = [user_name + 'さんおやすみヒヒン', user_name + '乙', 'ねむみちゃんからの' + user_name + 'ちゃん']
    return random.choice(goodbye_list)

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
    
@client.event
async def on_message_delete(message):
    print('on_message_delete')
    await message.channel.send(random.choice(['今"'+ message.content +'"ってやつ消した？ヒヒン？']))

@client.event
async def on_message(message):
    print('on_message')
    if message.author.bot:
        return
    if 'こんにち' in message.content or 'おは' in message.content or 'こんばん' in message.content:
        await message.channel.send(hello(message.author.name))
    if 'おやすみ' in message.content or '乙' in message.content or 'おつ' in message.content:
        await message.channel.send(goodbye(message.author.name))
    if '水' in message.content or 'みず' in message.content:
        await message.channel.send(drown())

@client.event
async def on_reaction_add(reaction, user):
    print('on_reaction_add')


@client.event
async def on_member_join(member):
    await send_message_default_channel(client, random.choice([member.display_name + "さんようこそ！ヒヒン！", member.display_name + "！はじめましてだ！ヒヒン！"]))

client.run(token)
