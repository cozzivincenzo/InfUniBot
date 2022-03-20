import discord
from discord.ext import commands
from discord.utils import get
from strings import *

embed = discord.Embed()

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed.title = "Lista comandi"
        embed.description = help_string
        await ctx.send(embed=embed) 

####################################################

class corsi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def corsi(self, ctx, anno:str="", semestre:str=""):
        embed.title = "Lista dei link ai corsi"

        if anno == "1":
            if anno == "1" and semestre == "1":
                embed.description = first_year_first_semester_string
                embed.title = "Lista dei link ai corsi "
                await ctx.send(embed=embed)
            elif  anno == "1" and semestre == "2":
                embed.description = first_year_second_semester_string
                await ctx.send(embed=embed)
            else:
                embed.description = first_year_string
                await ctx.send(embed=embed)

        if anno == "2":
            if anno == "2" and semestre == "1":
                embed.description = second_year_first_semester_string
                await ctx.send(embed=embed)
            elif  anno == "2" and semestre == "2":
                embed.description = second_year_second_semester_string
                await ctx.send(embed=embed)
            else:
                embed.description = second_year_string
                await ctx.send(embed=embed)
        
        if anno == "":
            embed.description = "Selezionare l'anno e/o il semestre ( ;corsi <anno> <semestre> ) \n Ricordati di inserire lo spazio tra <anno> e <semestre>"
            await ctx.send(embed=embed)

####################################################

class social(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def social(self, ctx):
        embed.title = "Lista dei canali social della nostra classe"
        embed.description = social_string
        await ctx.send(embed=embed) 

####################################################

class appunti(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def appunti(self, ctx):
        embed.title = "Lista di appunti da varie fonti"
        embed.description = note_string
        await ctx.send(embed=embed) 

####################################################

class unisa(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unisa(self, ctx):
        embed.title = "Lista di link utili dell'unisa"
        embed.description = unisa_string
        await ctx.send(embed=embed)

####################################################

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        pommodoro = get(ctx.guild.roles, name="Pommodoro")
        bruschette = get(ctx.guild.roles, name="Bruschette")
        embed.title = "Info server e bot"
        embed.description = f"""\nPer info riguardanti il server discord, contattare i membri con tag {bruschette.mention} o {pommodoro.mention}\n 
                                \nPer info e/o segnalazione di bug riguardanti il bot, contattare <@682322414772027443>\n""" + "\n \U00002615 " + ' ' + " [Bello un caffè a piacere](" + URLS['donation'] +")\n"
        await ctx.send(embed=embed) 


def setup(bot):
    bot.add_cog(help(bot))
    bot.add_cog(corsi(bot))
    bot.add_cog(social(bot))
    bot.add_cog(appunti(bot))
    bot.add_cog(unisa(bot))
    bot.add_cog(info(bot))

    