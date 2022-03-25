import interactions
from interactions.ext import molter
from strings import *

author = interactions.EmbedAuthor (
    name = "concozzi#6475",
    url = "https://discord.com/users/682322414772027443/" 
)

footer = interactions.EmbedFooter(
    text = "\u00A9 cozzivincenzo.it",
    icon_url = "https://cozzivincenzo.it/wp-content/themes/cozzivincenzo-theme/assets/img/logosvgdark.png"
)

class PrefixCommands(molter.MolterExtension):
    def __init__(self, bot: interactions.Client):
        self.bot = bot

    @molter.msg_command()
    async def help(self, ctx: molter.MolterContext):

        embed = interactions.Embed(
            title = "Lista comandi",
            description = help_string,
            author = author,
            footer = footer
        ) 

        await ctx.reply(embeds=embed)

    ######################################################

    @molter.msg_command()
    async def corsi(self, ctx: molter.MolterContext, anno:str='', semestre:str=''):
        
        if anno == "1":
            if anno == "1" and semestre == "1":

                embed = interactions.Embed(
                    title = "Lista dei link ai corsi del 1\N{DEGREE SIGN} Anno 1\N{DEGREE SIGN} Semestre",
                    description = first_year_first_semester_string,
                    author = author,
                    footer = footer
                )

                await ctx.reply(embeds=embed)

            elif  anno == "1" and semestre == "2":

                embed = interactions.Embed(
                    title = "Lista dei link ai corsi del 1\N{DEGREE SIGN} Anno 2\N{DEGREE SIGN} Semestre",
                    description = first_year_second_semester_string,
                    author = author,
                    footer = footer
                )

                await ctx.reply(embeds=embed)

            else:

                embed = interactions.Embed(
                    title = "Lista dei link ai corsi del 1\N{DEGREE SIGN} Anno",
                    description = first_year_string,
                    author = author,
                    footer = footer
                )

                await ctx.reply(embeds=embed)

        if anno == "2":
            if anno == "2" and semestre == "1":

                embed = interactions.Embed(
                    title = "Lista dei link ai corsi del 2\N{DEGREE SIGN} Anno 1\N{DEGREE SIGN} Semestre",
                    description = second_year_first_semester_string,
                    author = author,
                    footer = footer
                )

                await ctx.reply(embeds=embed)

            elif  anno == "2" and semestre == "2":

                embed = interactions.Embed(
                    title = "Lista dei link ai corsi del 2\N{DEGREE SIGN} Anno 2\N{DEGREE SIGN} Semestre",
                    description = second_year_second_semester_string,
                    author = author,
                    footer = footer
                )

                await ctx.reply(embeds=embed)

            else:

                embed = interactions.Embed(
                    title = "Lista dei link ai corsi del 2\N{DEGREE SIGN} Anno",
                    description = second_year_string,
                    author = author,
                    footer = footer
                )

                await ctx.reply(embeds=embed)
        
        if anno == "":

            embed = interactions.Embed(
                title = "Selezionare l'anno e/o il semestre ( ;corsi <anno> <semestre> ) \n Ricordati di inserire lo spazio tra <anno> e <semestre>",
                author = author,
                footer = footer
            )

            await ctx.reply(embeds=embed)
            

    ######################################################

    @molter.msg_command()
    async def social(self, ctx: molter.MolterContext):
        embed = interactions.Embed(
            title = "Lista dei canali social della nostra classe",
            description = social_string,
            author = author,
            footer = footer
        )
        await ctx.reply(embeds=embed)

    ######################################################

    @molter.msg_command()
    async def appunti(self, ctx: molter.MolterContext):
        embed = interactions.Embed(
            title = "Lista di appunti da varie fonti",
            description = note_string,
            author = author,
            footer = footer
        )
        await ctx.reply(embeds=embed)

    ######################################################

    @molter.msg_command()
    async def unisa(self, ctx: molter.MolterContext):
        embed = interactions.Embed(
            title="Lista di link utili dell'unisa",
            description=unisa_string,
            author = author,
            footer = footer
        )
        await ctx.reply(embeds=embed)

    ######################################################

    @molter.msg_command()
    async def info(self, ctx: molter.MolterContext):

        pommodoro = interactions.Role(
            id = 761215483298578443
        )

        bruschette = interactions.Role(
            id = 760928430149337138
        )

        info_string = f"""\nPer info riguardanti il server discord, contattare i membri con tag {pommodoro.mention} o {bruschette.mention}\n 
                            \nPer info e/o segnalazione di bug riguardanti il bot, contattare <@682322414772027443>\n""" + "\n \U00002615 " + ' ' + " [Bello un caffè a piacere](" + URLS['donation'] +")\n"

        embed = interactions.Embed(
            title = "Info server e bot",
            description = info_string,
            author = author,
            footer = footer
        )
        await ctx.reply(embeds=embed)

def setup(bot: interactions.Client):
    PrefixCommands(bot)