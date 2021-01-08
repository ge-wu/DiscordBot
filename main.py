import os
import discord
import datetime
import collect_data

from discord.ext import commands
from keep_alive import keep_alive

prefix = '!'
client = discord.Client()
bot = commands.Bot(command_prefix=prefix)
data = collect_data.get_data()

@client.event
async def on_ready():
  print("Bot online")

@client.event
async def on_message(message):
  role = [r.name for r in message.author.roles]
  print(role)
  if message.content.startswith(prefix + "lc") and "ChalAdmin" in role:
    # cmd, num, topic = message.content.split()
    temp = message.content.split()
    num = temp[1]
    topic = ' '.join(temp[2:])
    
    cur_problem = data[int(num)]
    today = datetime.date.today()
    link = cur_problem["url"]
    difficulty = cur_problem["difficulty"]
    title = cur_problem["question_title"]
    
    embed = discord.Embed(title=f"LC daily challenge: {today}", url=link, color=0xFFA500)
    embed.set_thumbnail(url=
    "https://upload.wikimedia.org/wikipedia/commons/1/19/LeetCode_logo_black.png")
    embed.set_author(name="Will", icon_url=message.author.avatar_url)
    embed.add_field(name="Title", value=f"{num}. {title}", inline=False)
    embed.add_field(name="Topic", value=topic, inline=True)
    embed.add_field(name="Difficulty", value=difficulty, inline=True)
    embed.set_footer(text="Please post your accepted code in 24 hours.")

    await message.delete()
    await message.channel.send(embed=embed)
    
keep_alive()
client.run(os.getenv("TOKEN"))