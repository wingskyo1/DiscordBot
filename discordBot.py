import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import os

description = '''EchoBot by EchoNoahGaming'''
bot = commands.Bot(command_prefix='-', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def announcement(ctx, *, args):
    """Announcement command!"""
    embed=discord.Embed(title="Announcement", description=args, color=0x7700aa)
    embed.set_footer(text="By EchoNoahGaming")
    await ctx.send("@everyone", embed=embed)

bot.run(str(os.environ.get('DISCORD_BOT_SECRET')))