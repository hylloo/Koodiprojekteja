import discord
import os
from discord.ext.commands import Bot
import json
from discord.ext.commands.errors import DisabledCommand
from riotwatcher import LolWatcher
from discord.ext import commands
import requests




TOKEN = 'ODczNTc5MzM3MjIyMzI0Mjg0.YQ6eKA.MPB5CIrH81oz5LTk0h8ZQzwhavc'
BOT_PREFIX = "-"
client = Bot(command_prefix=BOT_PREFIX)
channel=client.get_channel(873588039643955230)
channel2= client.get_channel(874068263829647380)


@client.event
async def on_ready():
    channel=client.get_channel(873588039643955230)
    await channel.send("Käytä komentoja '-'(eune) ja '€'(EUW)")
    
    
@client.event
async def on_message(message):
    channel=client.get_channel(873588039643955230)
    if message.content.startswith('-'):
        user= message.content
        summonerName = str(user[1:])
        server='eune'
        await printStats(summonerName)
        
    if message.content.startswith('€'):
        user=message.content
        summonerName = str(user[1:])
        server='EUW'
        await printStats2(summonerName)

    if message.content.startswith('!'):
        champion=message.content
        champion= str(champion[1:])
        #championlist= string.capwords(champion)
        #data = requests.get('http://api.champion.gg/champion/' + champion + '/items/finished/mostWins?api_key=' + DiscordCredentials.championgg_token)


async def printStats(summonerName):
    server='eun1'
    key = 'RGAPI-754e4998-d958-4a68-b07a-01cc8e7815e9'
    watcher= LolWatcher(key)
    channel=client.get_channel(873588039643955230)
    olli = watcher.summoner.by_name(server, summonerName)
    summonerLevel= olli['summonerLevel']
    
    stats = watcher.league.by_summoner(server, olli['id'])
    
    if 1>=len(stats):
        await channel.send("Käyttäjällä ei ole rankkia")
        
    tier = stats [0]['tier']
    tier=str(tier)
    rank= stats[0]['rank']
    rank=str(rank)
    rank2=rank
    lp=stats[0]['leaguePoints']
    lp=str(lp)
    lp = lp.replace(',', '')
    lp = lp.replace("'", '')
    rank=tier+' '+rank
    
    if rank.startswith("DIAMOND"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Diamond_1.png'
    if rank.startswith("GOLD"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Gold_1.png'
    if rank.startswith("SILVER"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Silver_1.png'
    if rank.startswith("BRONZE"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Bronze_1.png'
    if rank.startswith("IRON"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Iron_1.png'
    if rank.startswith("PLATINUM"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Platinum_1.png'
    if rank.startswith("MASTER"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Master_1.png'
    if rank.startswith("GRANDMASTER"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Grandmaster_1.png'
    if rank.startswith("CHALLENGER"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Challenger_1.png'
    
    embed=discord.Embed(title=summonerName, description=rank, color=0x00ffee)
    embed.set_thumbnail(url=url)
    embed.add_field(name="lp", value=lp, inline=True)
    embed.add_field(name="Summoner Level", value=summonerLevel, inline=True)
    #embed.add_field(name="Voittoprosentti", value=voittoprosentti, inline=True)
    await channel.send(embed=embed)


async def printStats2(summonerName):

    server='euw1'
    key = 'RGAPI-ad368975-2b79-4108-9f1a-7c373f994dfa'
    watcher= LolWatcher(key)
    channel=client.get_channel(873588039643955230)
    olli = watcher.summoner.by_name(server, summonerName)
    stats = watcher.league.by_summoner(server, olli['id'])
    
    #if 1>=len(stats):
        #await channel.send("Käyttäjällä ei ole rankkia")
          
    tier = stats [0]['tier']
    tier=str(tier)
    rank= stats[0]['rank']
    rank=str(rank)
    rank2=rank
    lp=stats[0]['leaguePoints']
    lp=str(lp)
    lp = lp.replace(',', '')
    lp = lp.replace("'", '')
    rank=tier+' '+rank
    
    if rank.startswith("DIAMOND"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Diamond_1.png'
    if rank.startswith("GOLD"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Gold_1.png'
    if rank.startswith("SILVER"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Silver_1.png'
    if rank.startswith("BRONZE"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Bronze_1.png'
    if rank.startswith("IRON"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Iron_1.png'
    if rank.startswith("PLATINUM"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Platinum_1.png'
    if rank.startswith("MASTER"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Master_1.png'
    if rank.startswith("GRANDMASTER"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Grandmaster_1.png'
    if rank.startswith("CHALLENGER"):
        url='https://img.rankedboost.com/wp-content/uploads/2014/09/Season_2019_-_Challenger_1.png'
    
    embed=discord.Embed(title=summonerName, description=rank, color=0x00ffee)
    embed.set_thumbnail(url=url)
    embed.add_field(name="lp", value=lp, inline=True)
    await channel.send(embed=embed)  

client.run(TOKEN)
