# bot.py
import os

from discord.ext import commands
import discord
from discord.utils import get
from config import *
from strings import *

bot = commands.Bot(command_prefix='.', help_command=None)

@bot.event
async def on_ready():
    
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='help')
async def help_query(ctx):

    embed = discord.Embed()
    embed.title = "Lista comandi"
    embed.description = help_string
    await ctx.send(embed=embed) 

@bot.command(name='corsi')
async def courses_query(ctx):

    embed = discord.Embed()
    embed.title = "Lista completa di tutti i corsi"
    embed.description = courses_string
    await ctx.send(embed=embed)      

@bot.command(name='s1')
async def first_semester_query(ctx):

    embed = discord.Embed()
    embed.title = "Lista dei corsi del primo semestre"
    embed.description = first_semester_string
    await ctx.send(embed=embed) 

@bot.command(name='s2')
async def second_semester_query(ctx):

    embed = discord.Embed()
    embed.title = "Lista dei corsi del secondo semestre"
    embed.description = second_semester_string
    await ctx.send(embed=embed)
    
@bot.command(name='social')
async def social_query(ctx):

    embed = discord.Embed()
    embed.title = "Lista dei canali social della nostra classe"
    embed.description = social_string
    await ctx.send(embed=embed) 

@bot.command(name='appunti')
async def note_query(ctx):

    embed = discord.Embed()
    embed.title = "Lista di appunti da varie fonti"
    embed.description = note_string
    await ctx.send(embed=embed) 


@bot.command(name='unisa')
async def unisa_query(ctx):

    embed = discord.Embed()
    embed.title = "Lista di link utili dell'unisa"
    embed.description = unisa_string
    await ctx.send(embed=embed) 

@bot.command(name='info')
async def info_query(ctx):

    lux = get(ctx.guild.roles, name="Lux")
    bruschette = get(ctx.guild.roles, name="Bruschette")
    embed = discord.Embed()
    embed.title = "Info server e bot"
    embed.description = f"""\nPer info riguardanti il server discord, contattare i membri con tag {bruschette.mention} o {lux.mention}\n 
                            \nPer info e/o segnalazione di bug riguardanti il bot, contattare <@682322414772027443>\n"""
    await ctx.send(embed=embed) 

bot.run(TOKEN)
