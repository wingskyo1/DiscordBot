# import discord
import os
import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='>', description="Wing Bot")

foodList = ['八方雲集','麥當勞','肯德基','貓貓蟲']

TOKEN = os.environ.get("DISCORD_BOT_SECRET")
aaa = 'NzMwNDUwOTgzMTIxMDU5ODU4.XwnEfw.Y4vEv8cYhY9rSZsyiYrQhlofh6Q'
client = discord.Client()
discord.ClientUser
lobbyChannelId = 557519719947698197


@client.event
async def on_message(message):
    channel = message.channel

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('add '):
        foodName = message.content[4:]
        foodList.append(foodName)
        await channel.send('已新增' + foodName)
    elif message.content.startswith('food'):
        await channel.send('食物清單如下 : ')
        for foodName in foodList:
            await channel.send(foodName)
    elif "吃" in message.content:
        await channel.send(random.choice(foodList))



@client.event
async def on_voice_state_update(member, before, after):
    lobbyChannel = client.get_channel(lobbyChannelId)
    msg = ""
    userName = member.nick
    beforeMute = before.self_mute
    beforeChannel = before.channel
    afterMute = after.self_mute
    afterChannel = after.channel
    if beforeMute != afterMute:
        msg += ' 把自己' + "靜音" if after.self_mute else "解除靜音"

    if beforeChannel != afterChannel:
        if afterChannel == None:
            msg += '離開了語音頻道: ' + before.channel.name 
        else :
            msg += ' 加入了語音頻道'  + after.channel.name 

    await lobbyChannel.send(userName + msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

print(TOKEN)
client.run(TOKEN)
