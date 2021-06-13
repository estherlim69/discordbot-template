import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check

client = discord.Client()

client = commands.Bot(command_prefix = '!') #put your own prefix here

@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online
    
@client.command()
async def ping(ctx):
    await ctx.send("pong!") #example command that replies with pong! when you use !ping
async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) #simple kick command
    except:
        await ctx.send("bot does not have the kick members permission!")

client.run(os.getenv("TOKEN")) #replace TOKEN with your actual bot token
#commands are case-sensitive
