import discord
import sys
import os
import asyncio
from discord import message
from discord.ext import commands
from discord import ext
from discord.ext.commands import Bot
bot = commands.Bot(command_prefix='!')
client = discord.Client()
import time
from mytoken import TOKEN

####ohjelmat joita tarvitaan####
from antimoi import *
from interface import *
##################
#################################### DISCORDIN KANAVAT
#general_channel = client.get_channel (728629508785176617)
#testi_channel = client.get_channel (87264870901444616)
####################################


@client.event
async def on_ready():
    
    general_channel = client.get_channel (728629508785176617)
    testi_channel = client.get_channel (872648709014446160)
    await testi_channel.send('Botti valmis toimimaan')

async def on_message(message):
    #kaikki chattikomennot tähän##################################################################
    if message.content == ('!peliä') :
        peliä()

    if message.content == ('!peleille'):
        peleille()
    if message.content == ('antimoi'):
        antimoi()
        
    if message.content == ('!peleille'):

    if message.content == ('!peliä'):

    if message.content == ('!peleille'):

    else: 
        await testi.channel.send('tuntematon komento')
        return
################################################################


async def interface(message):

    if message.content == '!peliä':
        testi_channel = client.get_channel (872648709014446160)
       ####embed laatikko####
        myEmbed = discord.Embed(title="Peli Botti", description="Reagoi alle ja olet mukana arvonnassa", color=0x00ff00)
        myEmbed.set_author(name="Patonki Anneli")
        myEmbed.add_field(name="Mode: 5v5 inhouse", value="arvotaan 9 paikkaa peleille", inline=False)
        await testi_channel.send(embed=myEmbed)



client.run('')