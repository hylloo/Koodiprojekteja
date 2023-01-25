import discord
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
import decimal
import random
import math
import sys



TOKEN = 'NTY5NzA5NTIzNTI3MjcwNDAx.XL0_1g.OFSBRKH2RtcQjQ20BPQYbZGw974'
BOT_PREFIX = "!"
client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    global channel
    print("Inhousebotti ready!")
    print("Discord.py versio",discord.__version__)
    activity = discord.Game(name="Work in Progress")
    await client.change_presence(status=discord.Status.idle, activity=activity)

@client.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.format(member))

@client.event
async def on_message(message):  #VÄLITTÄÄ VIESTIN

    nimi = message.author
    nimi = str(nimi)
    nimi = nimi[:-5]
    print("(",message.channel,")  ",nimi,":", message.content)
    global pelaajamaara
    global channel
    global pelaajalista
    global bot

    if message.author == client.user:
        return
    await client.process_commands(message)
@client.command()
async def foo(ctx, arg):
    await ctx.send(arg)

@client.command()
async def ping(ctx):
    await ctx.send('PONG!')

@client.command()
async def lista(ctx):
    channel = discord.Object(id='404002392296914953')
    embed = discord.Embed(
    title = 'Pelaajalista',
    description = 'Valmiit/Pelaamassa olevat, käytä komentoja !peleille ja !poispeleiltä',
    colour = discord.Colour.blue()
    )

    embed.set_footer(text =  "this is a footer.")
    embed.add_field(name="pelaajalista",value="Field Value", inline=True)
    embed.add_field(name="pelaajalista1",value="Field Value", inline=True)
    embed.add_field(name="pelaajalista2",value="Field Value", inline=True)
    embed.add_field(name="pelaajalista2",value="Field Value", inline=True)
    await ctx.send(embed=embed)

@client.command()
async def peleille(ctx):
    global pelaajamaara
    global channel
    global pelaajalista
    global bot

    if ctx.message == "!peleille":
        pelaajamaara = pelaajamaara + 1
        ctx.send("Pelaaja lisätty. Pelaajia",pelaajamaara,"Kpl.")

        if pelaajamaara <= 9:
            print("Pelaaja lisätty, pelaajia ",int(pelaajamaara),"Kpl")
            viesti = 'Pelaaja lisätty, pelaajia',int(pelaajamaara),'Kpl'
            #viesti = str(viesti).replace("'", "").replace(",", "").strip(")(")
            await ctx.send(viesti)

        elif pelaajamaara >= 10:
            viestitaynna = 'Pelit täynnä. Pelaajia',int(pelaajamaara),'Kpl. Eikun servulle!'
            #viestitaynna = str(viestitaynna).replace("'", "").replace(",", "").strip(")(")
            await ctx.send(viestitaynna)

@client.command()
async def poispeleiltä(ctx):
    if pelaajamaara == 0:
        print("Ei pelaajia listalla")
        viesti1 = "Ei pelaajia listalla"
        #viesti1 = str(viesti1).replace('"', "")
        await ctx.send(viesti1)

    if pelaajamaara > 0:
        pelaajamaara = pelaajamaara - 1
        print("Pelaaja poistettu, pelaajia",int(pelaajamaara),"Kpl")
        viesti2 = 'Pelaaja poistettu, pelaajia',int(pelaajamaara),'Kpl'
        #viesti2 = str(viesti2).replace("'", "").replace(",", "").strip(")(")
        await ctx.send(viesti2)

@client.command()
async def moti(ctx):

    prosentti =(decimal.Decimal('%d.%d' % (random.randint(0,100),random.randint(0,99))))
    prosentti = round(prosentti, 1)

    if prosentti > 50:
        print("Voitto tulee",prosentti,"%:n varmuudella, heleppo.")
        viesti3 = 'Voitto tulee',prosentti,'%:n varmuudella. heleppo.'
        viesti3 = str(viesti3).replace("'", "").replace("Decimal", "").replace("(", "").replace(")", "").replace(",", "")
        await ctx.send(viesti3)
    elif prosentti < 50:
        print("Paska tiimi, häviö tulee",(100 - prosentti),"%:n varmuudella. RIP moti.")
        viesti4 = 'Paska tiimi ja häviö tulee',(100 - prosentti),'%:n varmuudella. RIP moti.'
        viesti4 = str(viesti4).replace("'", "").replace("Decimal", "").replace("(", "").replace(")", "").replace(",", "")
        await ctx.send(viesti4)

    elif prosentti == 50:
        print("fifti fifti, osuu tai ei osu, voitatte tai häviätte",prosentti,"%:n varmuudella.")
        viesti5 = 'fifti fifti, osuu tai ei osu, voitatte tai häviätte',prosentti,'%:n varmuudella.'
        viesti5 = str(viesti5).replace("'", "").replace("Decimal", "").replace("(", "").replace(")", "")
        await ctx.send(viesti5)

@client.command()
async def komennot(ctx):
    print("Inhouse botin komennot: \n"
               "!peleille : Lisää pelaajan pelaajaluetteloon" "\n"
               "!poispeleiltä  : Poistaa pelaajan pelaajaluettelosta" "\n"
               "!moti : voittoprosentti-motibooster")

    viesti6 = ("Inhouse botin komennot: \n"
               "                            !peleille : Lisää pelaajan pelaajaluetteloon \n"
               "                            !poispeleiltä  : Poistaa pelaajan pelaajaluettelosta \n"
               "                            !moti : voittoprosentti-motibooster \n"
               "                            !komennot : näyttää tämän komentolistan")
    await ctx.send(viesti6)
































client.run(TOKEN)
