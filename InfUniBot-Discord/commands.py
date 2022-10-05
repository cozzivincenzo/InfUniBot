import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed()
        embed.title = "Lista comandi"
        embed.description = help_string
        await ctx.send(embed=embed) 

def setup(bot):
    bot.add_cog(help(bot))

    