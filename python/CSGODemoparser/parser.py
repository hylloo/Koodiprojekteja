from awpy import DemoParser
from awpy.analytics.stats import player_stats



demo_parser = DemoParser(
    demofile = "asd.dem", 
    demo_id = "asd", 
    parse_rate=128, 
    trade_time=5, 
    buy_style="hltv"
)
data = demo_parser.parse()

player_stats_json = player_stats(data["gameRounds"])
player_stats_df = player_stats(data["gameRounds"], return_type="df")

#x=0
#for i in player_stats_df["playerName"]:
    
#    print (player_stats_df["playerName"][x], player_stats_df["teammatesFlashed"][x], player_stats_df["teamKills"][x])
#    x=x+1

df = demo_parser.parse(return_type="df")
df.keys()
x=0
df2=df["damages"]
TD=df2["isFriendlyFire"]
TDcount=0
#print(df2)
lista=[]

class Pelaaja:
    def __init__(self,nimi=""):
        self.nimi=""
        self.vahinkokerrat=0
        self.damagelista=[]
    
class Damage:
    vahinko=0
    kierros=0

e=None
for i in TD:
    #print (TD[x])
   
    if TD[x]== True:
        e=df2["attackerName"][x]
        #print(e)

        found = False
        for i in lista:
            if e == i.nimi: #pelaaja on jo aikasemmin tehny dmg
                found= True
                break
        if found == False:
            pelaaja = Pelaaja()
            pelaaja.nimi=e
            lista.append(pelaaja) #lisätään pelaaja listaan
    x=x+1

for pelaaja in lista:
    print(pelaaja.nimi)
    
#print(TDcount)