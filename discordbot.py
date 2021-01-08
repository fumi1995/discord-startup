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
    print('member join:' + member.display_name)
    for channel in member.server.channels:
        print('member join 2:' + channel.name)
        if channel.name == 'general' or channel.name == '一般':
            print('member join 3:' + channel.name)
            await client.send_message(channel, member.display_name + 'ちゃん初めましてだヒヒン!')

client.run(token)
