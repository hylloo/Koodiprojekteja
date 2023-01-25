import discord
from discord.ext import commands
from discord.ext.commands import Bot
bot = commands.Bot(command_prefix='!')
client = discord.Client()


async def interface(message):

    if message.content == '!peliä':
        testi_channel = client.get_channel (872648709014446160)
       ####embed laatikko####
        myEmbed = discord.Embed(title="Peli Botti", description="Reagoi alle ja olet mukana arvonnassa", color=0x00ff00)
        myEmbed.set_author(name="Patonki Anneli")
        myEmbed.add_field(name="Mode: 5v5 inhouse", value="arvotaan 9 paikkaa peleille", inline=False)
        await testi_channel.send(embed=myEmbed)
        #####################