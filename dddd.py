import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("여캠 탐방")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("~채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)

@client.event
async def on_member_join(member):
    my_guild = client.get_guild(602815804588687371)
    if (member.guild.id == my_guild.id):
        channel = client.get_channel(606891813885837356)
        channel_name = '{}_members'.format(my_guild.member_count)
        await channel.edit(name=channel_name)

@client.event
async def on_member_remove(member):
    my_guild = client.get_guild(602815804588687371)
    if (member.guild.id == my_guild.id):
        channel = client.get_channel(606891813885837356)
        channel_name = '{}_members'.format(my_guild.member_count)
        await channel.edit(name=channel_name)



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
