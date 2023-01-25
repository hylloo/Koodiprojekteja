import discord
from discord import Game
from discord.ext.commands import Bot
import decimal
import random
import math
import sys
from discord.ext import commands


prefix = "!"
#client = commands.Bot(command_prefix=prefix)
pelaajamaara = 0
pelaajalista = []
TOKEN = 'NTY5NzA5NTIzNTI3MjcwNDAx.XL0_1g.OFSBRKH2RtcQjQ20BPQYbZGw974'

#client = discord.Client()
client = commands.Bot(command_prefix = '.')
channel = discord.Object(id='404002392296914953')


@client.event
async def on_ready():
    global channel
    print("Inhousebotti ready!")
    activity = discord.Game(name="Work in Progress")
    await client.change_presence(status=discord.Status.idle, activity=activity)

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)

@client.command()
async def displayembed():
    embed - discord.Embed(
    title = 'Title',
    description = 'This is a description',
    color = discord.Color.blue()
    )

    embed.set_footer(text =  "this is a footer.")
    embed.add_field(name="pelaajalista",value="Field Value", inline=True)

    await client.say(embed=embed)










@client.event
async def on_message(message):

    nimi = message.author
    nimi = str(nimi)
    nimi = nimi[:-5]
    print("(",message.channel,")  ",nimi,":", message.content)
    global pelaajamaara
    global channel
    global pelaajalista
    global bot

    if message.author == client.user:
        return message





        #if message.content == "!pelaajat"
        return message

@client.command()
async def info(message):
    global pelaajamaara
    global channel
    global pelaajalista
    global bot

    if message.author == client.user:
        return
    if message.content == "!ketä":
        Embed = discord.Embed(title="Inhouse pelaajalista", description="Tämän hetkiset pelaajat ja mahdolliset jonottajat.", color=0xeee657)
        await  client.say(Embed=Embed)
@client.event
async def peleille(message):
    global pelaajamaara
    global channel
    global pelaajalista
    global bot

    if message.content == "!peleille":
        pelaajamaara = pelaajamaara + 1

        if pelaajamaara <= 9:
            print("Pelaaja lisätty, pelaajia ",int(pelaajamaara),"Kpl")
            viesti = 'Pelaaja lisätty, pelaajia',int(pelaajamaara),'Kpl'
            viesti = str(viesti).replace("'", "").replace(",", "").strip(")(")
            await message.channel.send(viesti)

        elif pelaajamaara >= 10:
            viestitaynna = 'Pelit täynnä. Pelaajia',int(pelaajamaara),'Kpl. Eikun servulle!'
            viestitaynna = str(viestitaynna).replace("'", "").replace(",", "").strip(")(")
            await message.channel.send(viestitaynna)

    if message.content == "!poispeleiltä":

        if pelaajamaara == 0:
            print("Ei pelaajia listalla")
            viesti1 = "Ei pelaajia listalla"
            viesti1 = str(viesti1).replace('"', "")
            await message.channel.send(viesti1)

        if pelaajamaara > 0:
            pelaajamaara = pelaajamaara - 1
            print("Pelaaja poistettu, pelaajia",int(pelaajamaara),"Kpl")
            viesti2 = 'Pelaaja poistettu, pelaajia',int(pelaajamaara),'Kpl'
            viesti2 = str(viesti2).replace("'", "").replace(",", "").strip(")(")
            await message.channel.send(viesti2)

@client.event
async def moti(message):
    if message.content == "!moti":
        prosentti =(decimal.Decimal('%d.%d' % (random.randint(0,100),random.randint(0,99))))
        prosentti = round(prosentti, 1)

        if prosentti > 50:
            print("Voitto tulee",prosentti,"%:n varmuudella, heleppo.")
            viesti3 = 'Voitto tulee',prosentti,'%:n varmuudella. heleppo.'
            viesti3 = str(viesti3).replace("'", "").replace("Decimal", "").replace("(", "").replace(")", "").replace(",", "")
            await message.channel.send(viesti3)

        elif prosentti < 50:
            print("Paska tiimi, häviö tulee",(100 - prosentti),"%:n varmuudella. RIP moti.")
            viesti4 = 'Paska tiimi ja häviö tulee',(100 - prosentti),'%:n varmuudella. RIP moti.'
            viesti4 = str(viesti4).replace("'", "").replace("Decimal", "").replace("(", "").replace(")", "").replace(",", "")
            await message.channel.send(viesti4)

        elif prosentti == 50:
            print("fifti fifti, osuu tai ei osu, voitatte tai häviätte",prosentti,"%:n varmuudella.")
            viesti5 = 'fifti fifti, osuu tai ei osu, voitatte tai häviätte',prosentti,'%:n varmuudella.'
            viesti5 = str(viesti5).replace("'", "").replace("Decimal", "").replace("(", "").replace(")", "")
            await message.channel.send(viesti5)

@client.event
async def komennot(message):
    if message.content == "!komennot":
        print("Inhouse botin komennot: \n"
               "!peleille : Lisää pelaajan pelaajaluetteloon" "\n"
               "!poispeleiltä  : Poistaa pelaajan pelaajaluettelosta" "\n"
               "!moti : voittoprosentti-motibooster")

        viesti6 = ("Inhouse botin komennot: \n"
               "                            !peleille : Lisää pelaajan pelaajaluetteloon \n"
               "                            !poispeleiltä  : Poistaa pelaajan pelaajaluettelosta \n"
               "                            !moti : voittoprosentti-motibooster \n"
               "                            !komennot : näyttää tämän komentolistan")
        await message.channel.send(viesti6)













    @bot.command()
    async def add(ctx, a: int, b: int):
        await ctx.send(a)
    @bot.command()
    async def greet(ctx):
        await ctx.send(":smiley: :wave: Hello, there!")
client.run(TOKEN)
