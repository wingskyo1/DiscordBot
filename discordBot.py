import discord
import os
import random

client = discord.Client()
foodList = []
lobbyChannelId = 557519719947698197

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    channel = message.channel
    sendMessage =''
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
            sendMessage += foodName + '\n'
        await channel.send(sendMessage)
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

    await lobbyChannel.send(str(userName) + msg)


TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)

