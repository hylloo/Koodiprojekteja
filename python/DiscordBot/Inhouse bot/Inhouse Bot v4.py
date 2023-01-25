#Made by Tom.

import platform
import discord
import asyncio
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Member
import youtube_dl
import decimal
import random
import math
import sys
import time


pelaajamaara = 0
pelaajalista = []
mappilista = ['de_dust2','de_cache','de_inferno','de_overpass','de_mirage','de_train','de_nuke']
poistetutmapit = []
defaultmapit = ['de_dust2','de_cache','de_inferno','de_overpass','de_mirage','de_train','de_nuke']



TOKEN = 'NTY5NzA5NTIzNTI3MjcwNDAx.XL0_1g.OFSBRKH2RtcQjQ20BPQYbZGw974'
BOT_PREFIX = "!"
client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print("Inhousebotti ready!")
    print("Discord.py versio",discord.__version__)
    print("Python versio",platform.python_version())
    activity = discord.Game(name="Inhouse Bot by Tom.")
    await client.change_presence(status=discord.Status.idle, activity=activity)

#@client.command()
#async def joined(ctx, *, member: discord.Member):                                 #TÄMÄ EI TOIMI VIELÄ
#    await ctx.send('{0} joined on {0.joined_at}'.format(member))

@client.event
async def on_message(message):  #VÄLITTÄÄ VIESTIN

    nimi = message.author
    nimi = str(nimi)
    nimi = nimi[:-5]
    viesti = message.content
    print("(",message.channel,")  ",nimi,":", message.content)

    if message.author == client.user:
        return

    await client.process_commands(message)



@client.command()
async def map(ctx):
    global mappilista
    global poistetutmapit
    mappi =  random.choice(mappilista)
    await ctx.send("Seuraava mappi: "+mappi)

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



@client.command()
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
async def mappoolreset(ctx):
    global mappilista
    global poistetutmapit
    mappilista = mappilista + poistetutmapit
    await ctx.send("Mappipooli resetattu. kaikki kartat arvonnassa mukana.")








#@client.command()   #TESTILISTA
#async def randomlista(ctx):
#    nimiä = ['Pekka89','BiruB0b','TepiB0b','Pte','LaDe'] #testitarkoitukseen!!!
#    nimiä = str(nimiä).replace("[", "").replace("]", "").replace("'", "").replace(",", "").split(" ")
#    pelaajalista.append(nimiä)
#    await ctx.send("lista tehty")
#    print(pelaajalista)

@client.command()
async def lisää(ctx, arg):
    global pelaajamaara
    global pelaajalista
    if ctx.message.author.name == arg and pelaajamaara > 0 and arg in pelaajalista:
        await ctx.send("Pelaaja "+arg+" on jo pelaajalistalla.")
    else:
        pelaajamaara += 1
        pelaajalista.append(arg)
        plisää = ("Pelaaja " + arg + " lisätty")
        await ctx.send(plisää)

@client.command()
async def poista(ctx, arg):
    global pelaajamaara
    global pelaajalista
    if  arg in pelaajalista:
        pelaajalista.remove(arg)
        pelaajamaara -= 1
        ppoista = ("Pelaaja " + arg + " poistettu")
        await ctx.send(ppoista)
    else:
        await ctx.send("Pelaajaa "+ arg + " ei löytynyt. Yritä uudelleen.")

@client.command()
async def resetoi(ctx):
    global pelaajamaara
    global pelaajalista
    global mappilista
    global poistetutmapit
    pelaajamaara = ""
    pelaajalista = ""
    mappilista = ['de_dust2','de_cache','de_inferno','de_overpass','de_mirage','de_train','de_nuke'];
    await ctx.send("Kaikki listat resetoitu.")

@client.command()
async def viesti(ctx, arg):
    await ctx.send(arg)

@client.command()
async def ping(ctx):
    await ctx.send('PONG!')

@client.command()
async def vihu(ctx, arg):
    prosentti =(decimal.Decimal('%d.%d' % (random.randint(0,100),random.randint(0,99))))
    prosentti = round(prosentti, 1)
    global pelaajalista
    if pelaajamaara > 0 and arg != ctx.message.author.name:
        vihu1 = random.choice(pelaajalista)
        await ctx.send("Ens pelin kovin vihu tulee olemaan "+(str(vihu1))+". Ammu päihin ja matto alta. \n"
        "Voitat 1v1:ssä "+(str(prosentti))+"%:n varmuudella.")
    else:
        await ctx.send("Servulla ei ole vielä vihuja valmiina listassa tai yritit lisätä itsesi :(")

@client.command(pass_context=True)
async def ketä(ctx):
    channel = discord.Object(id='404002392296914953')
    embed = discord.Embed(
    title = 'Inhouset',
    description = 'Pelaajat ilmojärjestyksessä. \n Käytä komentoja !peleille, !peleiltä, !lisää ja !poista.',
    colour = discord.Colour.red()
    ) #KIINNI

    embed.add_field(name="Pelaajia:",value=(str(pelaajamaara)), inline=True)
    embed.add_field(name="Pelaajat:",value="\n ".join(str(pelaaja) for pelaaja in pelaajalista), inline=False)
    try:
        await ctx.send(embed=embed)
    except:
        await ctx.send("Nimilista on tyhjä.")

@client.command(pass_context=True)
async def kartat(ctx):
    channel = discord.Object(id='404002392296914953')
    embed = discord.Embed(
    title = 'Arvonnassa mukana olevat kartat',
    description = 'Käytä komentoja !map, !poistakartta, !lisääkartta ja !mappoolreset.',
    colour = discord.Colour.blue()
    ) #KIINNI

    embed.add_field(name="Karttoja:",value=(len(mappilista)), inline=True)
    embed.add_field(name="Kartat:",value="\n ".join(str(kartta) for kartta in mappilista), inline=False)
    try:
        await ctx.send(embed=embed)
    except:
        await ctx.send(embed=embed)

@client.command(pass_context=True)
async def peleille(ctx):
    global pelaajamaara
    global pelaajalista
    if ctx.message.author.name in pelaajalista:
        await ctx.send("Olet jo listalla!")

    else:
        pelaajamaara +=  1
        pelaajalista.append(ctx.message.author.name)
        if pelaajamaara == 8:
            await ctx.send("@everyone Tarvitaan enää kaksi pelaajaa!")
        if pelaajamaara == 9:
            await ctx.send("@everyone Tarvitaan enää yksi pelaaja!")
        #await ctx.send(pelaajalista)

        if pelaajamaara <= 9:
            print("Pelaaja lisätty. Pelaajia ",int(pelaajamaara),"Kpl")
            await ctx.send("Pelaaja lisätty. Pelaajia "+(str(pelaajamaara))+" Kpl")
        if pelaajamaara >= 10 and pelaajamaara < 15:
            await ctx.send("Pelit täynnä. Pelaajia "+(str(pelaajamaara))+" Kpl. Eikun servulle! @everyone")

        elif pelaajamaara >= 15:
            print("Pelaajalista Täynnä. Pelaajia 15 Kpl")
            await ctx.send("Pelaajalista Täynnä. Pelaajia 15 Kpl")
@client.command()
async def peleiltä(ctx):
    global pelaajamaara
    global pelaajalista
    if ctx.message.author.name in pelaajalista:
        pelaajalista.remove(ctx.message.author.name)
        if pelaajamaara == 0:
            print("Ei pelaajia listalla")
            await ctx.send("Ei pelaajia listalla")

        if pelaajamaara > 0:
            pelaajamaara = pelaajamaara - 1
            print("Pelaaja poistettu. Pelaajia",int(pelaajamaara),"Kpl")
            await ctx.send("Pelaaja poistettu, Pelaajia "+(str(pelaajamaara))+" Kpl.")
    else:
        await ctx.send("Sinua ei löydy pelaajalistalta.")


@client.command()
async def ammuperkele(ctx, arg):
    await ctx.send(arg+" ÄÄH VITTU PERKELE NIITÄ PÄITÄ.")

@client.command()
async def mestari(ctx, arg):
    global Pelaajalista
    prosentti =(decimal.Decimal('%d.%d' % (random.randint(0,100),random.randint(0,99))))
    prosentti = round(prosentti, 1)
    if arg != ctx.message.author.name:
        await ctx.send("Tän pelin mestari, nuori osuja tulee olemaan "+Pelaajalista+". Vittu mitkä takut. Komea mies varsinkin!")


@client.command()
async def moti(pass_context=True):
    prosentti =(decimal.Decimal('%d.%d' % (random.randint(0,100),random.randint(0,99))))
    prosentti = round(prosentti, 1)
    if ctx.message.author.name != arg:
        if prosentti > 50:
            print("Voitto tulee",prosentti,"%:n varmuudella, heleppo.")
            await ctx.send("Voitto tulee "+(str(prosentti))+" %:n varmuudella, heleppo.")
        elif prosentti < 50:
            havioprosentti = str(100 - prosentti)
            print("Paska tiimi, häviö tulee",(100 - prosentti),"%:n varmuudella. RIP moti.")
            await ctx.send("Paska tiimi, häviö tulee "+havioprosentti+" %:n varmuudella. RIP moti.")

        elif prosentti == 50:
            print("fifti fifti, osuu tai ei osu, voitatte tai häviätte",prosentti,"%:n varmuudella.")
            await ctx.send("fifti fifti, osuu tai ei osu, voitatte tai häviätte "+prosentti+" %:n varmuudella.")

@client.command()
async def steam(pass_context=True):
    steamurl = "https://s.team/chat/g3i5pWQb"
    await ctx.send("Jos ette jo ole, liittykää meidän Steamin Inhouse ryhmään. Jos linkki ei toimi, ota yhteyttä Tomiin tai admineihin. \n"
                   "https://s.team/chat/g3i5pWQb")

@client.command(pass_context=True)
async def autopost(ctx):
    print("Autopost on, pelaajalista chattiin 10min välein.")
    #await ctx.send("Autopost on, pelaajalista chattiin 10min välein.")

    for i in range(1,500):
        aika = 60 * 30
        print("autopost on")
        await ctx.send("Autopost on. Pelaajalistaa discordiin puolen tunnin välein. Komento !autopost off lopettaa.")
        viesti = '!ketä'
        if arg == "off":
            break
        else:
            await client.say(viesti)
            await asyncio.sleep(aika)





            #await ctx.send("Autopost off!")







@client.command()
async def komennot(ctx):
    print("Inhouse botin komennot: \n"
               "                            !peleille : Lisää pelaajan pelaajaluetteloon \n"
               "                            !peleiltä  : Poistaa pelaajan pelaajaluettelosta \n"
               "                            !ketä : Näyttää ketä on pelaamassa \n"
               "                            !lisää : Lisää pelaajan pelaajaluetteloon \n"
               "                            !poista : Poistaa pelaajan pelaajaluettelosta  \n"
               "                            !vihu : Tulevan pelin maalitaulu \n"
               "                            !moti : voittoprosentti-motibooster \n"
               "                            !komennot : näyttää tämän komentolistan")

    viesti6 = ("Inhouse botin komennot: \n"
               "                            !peleille : Lisää pelaajan pelaajaluetteloon \n"
               "                            !peleiltä  : Poistaa pelaajan pelaajaluettelosta \n"
               "                            !ketä : Näyttää ketä on pelaamassa \n"
               "                            !lisää : Lisää pelaajan pelaajaluetteloon \n"
               "                            !poista : Poistaa pelaajan pelaajaluettelosta  \n"
               "                            !map : arpoo seuraavan kartan \n"
               "                            !poistakartta : poistaa kartan arvontapoolista \n"
               "                            !lisääkartta : lisää kartan arvonapooliin \n"
               "                            !kartat : näyttää poolissa olevat kartat \n"
               "                            !mappoolreset : resettaa mappiarvontapoolin \n"
               "                            !vihu : Tulevan pelin maalitaulu \n"
               "                            !moti : Voittoprosentti-motibooster \n"
               "                            !steam : Antaa linkin Inhouse Steam ryhmään \n"
               "                            !komennot : Näyttää tämän komentolistan \n")
    await ctx.send(viesti6)





client.run(TOKEN)
