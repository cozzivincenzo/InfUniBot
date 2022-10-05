import interactions
from config import *
from strings import *

author = interactions.EmbedAuthor (
    name = "concozzi#6475",
    url = "https://discord.com/users/682322414772027443/" 
)

footer = interactions.EmbedFooter(
    text = "\u00A9 cozzivincenzo.it",
    icon_url = "https://cozzivincenzo.it/wp-content/themes/cozzivincenzo-theme/assets/img/logosvgdark.png"
)

class SlashCommands(interactions.Extension):
    def __init__(self, bot) -> None:
        self.bot = bot

    ######################################################

    @interactions.extension_command(
        name="social",
        description="Link ai social della nostra classe",
        scope=GUILD_ID,
    )
    async def social(self, ctx):
        embed = interactions.Embed(
            title = "Lista dei canali social della nostra classe",
            description = social_string,
            author = author,
            footer = footer
        )
        await ctx.send(embeds=embed, ephemeral=True)

    ######################################################

    @interactions.extension_command(
        name="help",
        description="Lista comandi",
        scope=GUILD_ID,
    )
    async def help(self, ctx):

        embed = interactions.Embed(
            title = "Lista comandi",
            description = help_string,
            author = author,
            footer = footer
        ) 

        await ctx.send(embeds=embed, ephemeral=True)

    ######################################################

    @interactions.extension_command(
        name="appunti",
        description="Lista di appunti da varie fonti",
        scope=GUILD_ID,
    )
    async def appunti(self, ctx):
        embed = interactions.Embed(
            title = "Lista di appunti da varie fonti",
            description = note_string,
            author = author,
            footer = footer
        )
        await ctx.send(embeds=embed, ephemeral=True)

    ######################################################

    @interactions.extension_command(
        name="unisa",
        description="Lista di link utili dell'unisa",
        scope=GUILD_ID,
    )
    async def unisa(self, ctx):
        embed = interactions.Embed(
            title="Lista di link utili dell'unisa",
            description=unisa_string,
            author = author,
            footer = footer
        )
        await ctx.send(embeds=embed, ephemeral=True)

    ######################################################

    @interactions.extension_command(
        name="info",
        description="Info sul server e sul bot",
        scope=GUILD_ID,
    )
    async def unisa(self, ctx):
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
        await ctx.send(embeds=embed, ephemeral=True)

    ######################################################

    """@interactions.extension_command(
        name="corsi",
        description="Link ai corsi",
        scope=GUILD_ID,
        options=[
            interactions.Option(
                name="primo_anno",
                description="Corsi primo anno",
                type=interactions.OptionType.SUB_COMMAND,
                options=[
                    interactions.Option(
                        name="semestre",
                        description="Seleziona semestre (1/2)",
                        type=interactions.OptionType.INTEGER,
                        required=False,
                    ),
                ],
            ),
            interactions.Option(
                name="secondo_anno",
                description="Corsi secondo anno",
                type=interactions.OptionType.SUB_COMMAND,
                options=[
                    interactions.Option(
                        name="semestre",
                        description="Seleziona semestre (1/2)",
                        type=interactions.OptionType.INTEGER,
                        required=False,
                    ),
                ],
            ),
        ],
    )
    async def corsi(self, ctx: interactions.CommandContext, sub_command: str = '', semestre: int = None):

        print(sub_command)

        if sub_command == "primo_anno":
            if semestre == 1:

                embed = interactions.Embed( 
                    title = "Lista dei link ai corsi del 1\N{DEGREE SIGN} Anno 1\N{DEGREE SIGN} Semestre",
                    description = first_year_first_semester_string,
                    author = author,
                    footer = footer
                )

                await ctx.send(embeds=embed, ephemeral=True)

            elif semestre == 2:

                embed = interactions.Embed(
                    title = "Lista dei link ai corsi del 1\N{DEGREE SIGN} Anno 2\N{DEGREE SIGN} Semestre",
                    description = first_year_second_semester_string,
                    author = author,
                    footer = footer
                )

                await ctx.send(embeds=embed, ephemeral=True)

            else:

                embed = interactions.Embed(
                    title = "Lista dei link ai corsi del 1\N{DEGREE SIGN} Anno",
                    description = first_year_string,
                    author = author,
                    footer = footer
                )

                await ctx.send(embeds=embed, ephemeral=True) 

        elif sub_command == "second_command":

            if semestre == "1":

                embed = interactions.Embed(
                    title = "Lista dei link ai corsi del 2\N{DEGREE SIGN} Anno 1\N{DEGREE SIGN} Semestre",
                    description = second_year_first_semester_string,
                    author = author,
                    footer = footer
                )

                await ctx.send(embeds=embed, ephemeral=True)

            elif semestre == "2":

                embed = interactions.Embed(
                    title = "Lista dei link ai corsi del 2\N{DEGREE SIGN} Anno 2\N{DEGREE SIGN} Semestre",
                    description = second_year_second_semester_string,
                    author = author,
                    footer = footer
                )

                await ctx.send(embeds=embed, ephemeral=True)

            else:

                embed = interactions.Embed(
                    title = "Lista dei link ai corsi del 2\N{DEGREE SIGN} Anno",
                    description = second_year_string,
                    author = author,
                    footer = footer
                )

                await ctx.send(embeds=embed, ephemeral=True) """

    @interactions.extension_command(
        name="base_command",
        description="This description isn't seen in UI (yet?)",
        scope=GUILD_ID,
        options=[
            interactions.Option(
                name="command_name",
                description="A descriptive description",
                type=interactions.OptionType.SUB_COMMAND,
                options=[
                    interactions.Option(
                        name="option",
                        description="A descriptive description",
                        type=interactions.OptionType.INTEGER,
                        required=False,
                    ),
                ],
            ),
            interactions.Option(
                name="second_command",
                description="A descriptive description",
                type=interactions.OptionType.SUB_COMMAND,
                options=[
                    interactions.Option(
                        name="second_option",
                        description="A descriptive description",
                        type=interactions.OptionType.STRING,
                        required=True,
                    ),
                ],
            ),
        ],
    )
    async def cmd(self, ctx: interactions.CommandContext, sub_command: str, second_option: str, option: int = None):
        if sub_command == "command_name":
            await ctx.send(f"You selected the command_name sub command and put in {option}")
        elif sub_command == "second_command":
            await ctx.send(f"You selected the second_command sub command and put in {second_option}")

def setup(bot):
    SlashCommands(bot)