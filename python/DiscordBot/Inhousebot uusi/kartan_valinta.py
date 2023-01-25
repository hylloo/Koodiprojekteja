import discord
import random
import Pääohjelma
from discord.ext import commands
bot = commands.Bot(command_prefix='!')
client = discord.Client()

@client.command()
async def map(ctx):
    global mappilista
    global poistetutmapit
    mappi =  random.choice(mappilista)
    await ctx.send("Seuraava mappi: "+mappi)


@client.command()
async def mappoolreset(ctx):
    global mappilista
    global poistetutmapit
    mappilista = mappilista + poistetutmapit
    await ctx.send("Mappipooli resetattu. kaikki kartat arvonnassa mukana.")

async def lisääkartta(ctx, arg):
    global mappilista
    global poistetutmapit
    if arg not in mappilista:
        if arg in poistetutmapit:
            poistetutmapit.remove(arg)
        else:
            mappilista.append(arg)
    else:
        await ctx.send("Kartta "+arg+" on jo mappipoolissa.")


@client.command()
async def poistakartta(ctx, arg):
    global mappilista
    global poistetutmapit
    if arg not in poistetutmapit:
        poistetutmapit.append(arg)
    else:
        await ctx.send("Kartta "+arg+" on jo poistettujen listalla.")
    if arg in mappilista:
        mappilista.remove(arg)
        await ctx.send("Kartta "+arg+" poistettu.")
    else:
        await ctx.send("Karttaa "+arg+" ei löytynyt mappipoolissa.")

