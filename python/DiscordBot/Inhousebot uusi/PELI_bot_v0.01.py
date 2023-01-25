import discord
import sys
import os
import asyncio
from discord.ext import commands
#from discord import ext
from discord.ext.commands import Bot
bot = commands.Bot(command_prefix='!')
client = discord.Client()
import time


  
#################################### DISCORDIN KANAVAT
#general_channel = client.get_channel (728629508785176617)
#testi_channel = client.get_channel (87264870901444616)
####################################

@client.event
async def on_ready():
    
  general_channel = client.get_channel (728629508785176617)
  testi_channel = client.get_channel (872648709014446160)
  #interface(message)

@client.event
#async def on_message(message):
 # pelaajalista= []
 # if message.content == 'p': #komento jolla pelit laitetaan aluille
 #   testi_channel = client.get_channel (872648709014446160)
 #   
 #   await testi_channel.send('@here pistetään pelit pystyyn')
 #   await testi_channel.send(message.author.name)
 #   pelaaja= str(message.author.name)
 #   pelaaja= pelaaja
 #   tägi=[]
 #   tägi.append(message.author.name)
 #   
 #   pelaajalista.append(pelaaja)
 #   await testi_channel.send(pelaajalista)
 #   await täys(pelaajalista)
 


 #if message.content.startswith('!peliä'):
 #  general_channel = client.get_channel (728629508785176617)
 #  testi_channel = client.get_channel (872648709014446160)
 #  #####embed laatikko
 #  myEmbed = discord.Embed(title="Peli Botti", description="Reagoi alle ja olet mukana arvonnassa", color=0x00ff00)
 #  myEmbed.set_author(name="Patonki Anneli")
 #  myEmbed.add_field(name="Mode: 5v5 inhouse", value="arvotaan 9 paikkaa peleille", inline=False)
 #  await testi_channel.send(embed=myEmbed)

@client.event
async def on_message(message):
    user=[]
    testi_channel = client.get_channel (872648709014446160)
    if message.content.startswith('!peliä'):
      general_channel = client.get_channel (728629508785176617)
      testi_channel = client.get_channel (872648709014446160)
      testi_channel = client.get_channel (872648709014446160)
      #####embed laatikko
      myEmbed = discord.Embed(title="Peli Botti", description="Reagoi alle ja olet mukana arvonnassa", color=0x00ff00)
      myEmbed.set_author(name="Patonki Anneli")
      myEmbed.add_field(name="Mode: 5v5 inhouse", value='sdasdasdasdsa', inline=False)
      msg=await testi_channel.send(embed=myEmbed)
      reaction = await msg.add_reaction("✅")
      check(reaction,user,msg)
      user=user.append

      if message.content.startswith('valmis'):
        await testi_channel.send(user)
     
async def check(reaction, user, msg):
    return user == msg.author and str(reaction.emoji) == '✅'


    #if message.author.id == bot.user.id:
    #    return
#def pelaajalista():
#    return 
#
#@client.event
#async def on_message(message):
#    
#      if message.content.startswith('!peliä'):
#          msg = '{0.author.mention}'.format(message)
#          pelaaja=msg
#          pelaaja= str(pelaaja)
#          await message.channel.send("lista")
#      if message.content.startswith('!lista'):
#          await message.channel.send("lista")
#      if message.content.startswith('!tyhjennä'):
#          pelaajat= []
#
client.run('ODcyNjQ5NjIxMTUzOTA2Nzc4.YQs8Sg.IF84f4QKg2GCrIkxvo464mNJVD4')