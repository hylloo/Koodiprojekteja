import discord
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
from discord import guild
import decimal
import random
import math
import sys

pelaajamaara = 0
pelaajalista = []




TOKEN = 'NTY5NzA5NTIzNTI3MjcwNDAx.XL0_1g.OFSBRKH2RtcQjQ20BPQYbZGw974'
BOT_PREFIX = "!"
client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
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

    if message.author == client.user:
        return

    await client.process_commands(message)

@client.command()
async def randomlista(ctx):
    nimiä = ['Pekka89','BiruB0b','TepiB0b','Pte','LaDe'] #testitarkoitukseen!!!
    nimiä = str(nimiä).replace("[", "").replace("]", "").replace("'", "").replace(",", "").split(" ")
    pelaajalista.append(nimiä)
    await ctx.send("lista tehty")
    print(pelaajalista)

@client.command()
async def lisää(ctx, arg):
    global pelaajamaara
    global pelaajalista
    if ctx.message.author.name == arg and pelaajamaara > 0 or arg in pelaajalista:
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
async def viesti(ctx, arg):
    await ctx.send(arg)

@client.command()
async def ping(ctx):
    await ctx.send('PONG!')

@client.command()
async def vihu(ctx):
    prosentti =(decimal.Decimal('%d.%d' % (random.randint(0,100),random.randint(0,99))))
    prosentti = round(prosentti, 1)
    global pelaajalista
    if pelaajamaara > 0:
        vihu1 = random.choice(pelaajalista)
        await ctx.send("Ens pelin kovin vihu tulee olemaan "+(str(vihu1))+". Ammu päihin ja matto alta. \n"
        "Voitat 1v1:ssä "+(str(prosentti))+"%:n varmuudella.")
    else:
        await ctx.send("Servulla ei ole vielä vihuja valmiina listassa :(")

@client.command(pass_context=True)
async def ketä(ctx):
    channel = discord.Object(id='404002392296914953')
    embed = discord.Embed(
    title = 'Inhouse-Pelaajat '+(str(pelaajamaara)),
    description = 'Valmiit/Pelaamassa olevat, käytä komentoja !peleille ja !poispeleiltä',
    colour = discord.Colour.red()
    ) #KIINNI

    embed.add_field(name="Pelaajia:",value=(str(pelaajamaara)), inline=True)
    embed.add_field(name="Pelaajat:",value="\n ".join(str(pelaaja) for pelaaja in pelaajalista), inline=False)
    try:
        await ctx.send(embed=embed)
    except:
        await ctx.send("Nimilista on tyhjä.")

@client.command(pass_context=True)
async def peleille(ctx):
    global pelaajamaara
    global pelaajalista
    if ctx.message.author.name in pelaajalista:
        await ctx.send("Olet jo listalla!")

    else:
        pelaajamaara +=  1
        pelaajalista.append(ctx.message.author.name)
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
async def moti(ctx):
    prosentti =(decimal.Decimal('%d.%d' % (random.randint(0,100),random.randint(0,99))))
    prosentti = round(prosentti, 1)

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
async def komennot(ctx):
    print("Inhouse botin komennot: \n"
               "!peleille : Lisää pelaajan pelaajaluetteloon" "\n"
               "!poispeleiltä  : Poistaa pelaajan pelaajaluettelosta" "\n"
               "!moti : voittoprosentti-motibooster")

    viesti6 = ("Inhouse botin komennot: \n"
               "                            !peleille : Lisää pelaajan pelaajaluetteloon \n"
               "                            !peleiltä  : Poistaa pelaajan pelaajaluettelosta \n"
               "                            !ketä : Näyttää ketä on pelaamassa \n"
               "                            !lisää : Lisää pelaajan pelaajaluetteloon \n"
               "                            !poista : Poistaa pelaajan pelaajaluettelosta  \n"

               "                            !moti : voittoprosentti-motibooster \n"
               "                            !komennot : näyttää tämän komentolistan")
    await ctx.send(viesti6)

















client.run(TOKEN)
