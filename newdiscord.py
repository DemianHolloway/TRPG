import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.uesr.id)
    print("ready")
    game = discord.Game("테스트봇")
    await  client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_member_join(member):
    role = ""
    for i in member.server.roles:
        role = i
        break
        await client.add_roles(member, role)

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):

        await message.channel.send("응")

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)

    if message.content.startswith(":Dm"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

    if message.content.startswith("!정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year)+"년" + str(date.month)+"월" +str(date.day)+"일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

