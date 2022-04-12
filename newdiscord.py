import discord
import datetime
import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials

client = discord.Client()

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = '{credentials.json}'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = '{https://docs.google.com/spreadsheets/d/1UUxldG6brJ87g-WJiPGlMtJQQWY59uh3C2GNXwGH9JI/edit?usp=sharing}'


# 스프레스시트 문서 가져오기
doc = gc.open_by_url(spreadsheet_url)

if message.content.startswith("!목록"):
# 시트 선택하기
worksheet = doc.worksheet('db')
range_list = worksheet.range('{"A1:C5"}')
    for cell in range_list:
        values[i].append(cell.value)
        break
    await message.channel.send(embed=embed)

"""worksheet.update_acell('B1', 'b1 updated')
# 특정 셀 쓰기

worksheet.append_row(['new1', 'new2', 'new3', 'new4'])
# 행 추가1

worksheet.insert_row(['new1', 'new2', 'new3', 'new4'], 4)
# 행 추가2"""


"""worksheet.resize(10,4)
# 크기 조정

gs = gc.create('{스프레드 시트명}')
# 스프레드시트 추가

worksheet = gs.add_worksheet(title='{시트명}', rows='{행 수}', cols='{열 수}')
# 시트 추가

gs.share('{이메일 주소}', perm_type='user', role='{권한}')
# 계정 공유"""


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
        embed=discord.Embed(title="제럴드 스왈로우", description="적기사단", color=0xff0000)
        embed.set_author(name="내정보", icon_url="https://i.imgur.com/zuAMJVl.png")
        embed.set_thumbnail(url="https://i.imgur.com/N7SSeGg.png")
        embed.add_field(name="힘", value="5", inline=True)
        embed.add_field(name="민첩", value="4", inline=True)
        embed.add_field(name="체력", value="4", inline=True)
        embed.add_field(name="정신", value="5", inline=True)
        embed.add_field(name="행운", value="2", inline=True)
        embed.add_field(name="가호", value="하인데, 포겐", inline=True)
        embed.add_field(name="HP", value="100", inline=True)
        embed.add_field(name="MP", value="100", inline=True)
        embed.add_field(name="스킬1", value="쿨타임", inline=True)
        embed.add_field(name="스킬2", value="쿨타임", inline=True)
        await message.channel.send(embed=embed)
        
access_token = os.environ['BOT_TOKEN']
client.run(access_token)

