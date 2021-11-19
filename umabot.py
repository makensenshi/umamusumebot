from typing import Text
import discord
from discord.ext import commands
import asyncio
import glob



client = discord.Client()

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.event
async def on_ready():
    activity = discord.Game(name="ウマ娘エロ画像厳選中…", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("起動完了")
    


 
    

bot.run("")
