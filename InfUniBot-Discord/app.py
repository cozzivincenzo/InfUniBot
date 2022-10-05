# bot.py
import os
from typing import Union
import interactions
import asyncio
from interactions import Button, ButtonStyle, SelectMenu, SelectOption, Embed
from interactions.ext import molter
#import discord
#from discord.ext import commands
from config import *
from strings import *

bot = interactions.Client(token=TOKEN)

molt = molter.Molter(bot)

@bot.event
async def on_ready():
    print(f'InfUniBot pronto a servirvi!')


@molt.message_command(aliases=["test2"])
async def test(ctx: molter.MolterContext, a_number: int):

    await ctx.reply(str(a_number))


button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="hello world!",
    custom_id="hello"
)

@bot.command(
    name="button_test",
    description="This is the first command I made!",
    scope=TEST_ID,
)
async def button_test(ctx):
    await ctx.send("testing", components=button)

@bot.component("hello")
async def button_response(ctx):
    await ctx.send("You clicked the Button :O", ephemeral=True)


"""loop = asyncio.get_event_loop()

task2 = loop.create_task(dpy.run(TOKEN))
task1 = loop.create_task(bot._ready())

gathered = asyncio.gather(task1, task2, loop=loop)
loop.run_until_complete(gathered)"""

bot.load("prefix_commands")
bot.load("slash_commands")
bot.start()


