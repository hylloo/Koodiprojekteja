import pandas as pd
import csv
from dataa import long_rolling_msft
from dataa import short_rolling_msft
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data


with open('ema100.csv', 'w', newline= '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ',')
    my_writer.writerow(long_rolling_msft)

df= pd.DataFrame(long_rolling_msft)
tiedosto= pd.read_csv('ema100.csv')
tiedosto.drop(tiedosto.iloc[:, 0:99], inplace = True, axis = 1)


with open('ema20.csv', 'w', newline= '') as csvfile:
    my_writer2 = csv.writer(csvfile, delimiter = ',')
    my_writer2.writerow(short_rolling_msft)

df2= pd.DataFrame(short_rolling_msft)
tiedosto2= pd.read_csv('ema20.csv')
tiedosto2.drop(tiedosto2.iloc[:, 0:19], inplace = True, axis = 1)



arvo100=[]
arvo20=[]
for column in tiedosto:
    try:
        column=float(column)
        
    except:
        column= column[:-2]
    arvo100.append(float(column))

for column in tiedosto2:
    try:
        column=float(column)
        
    except:
        column= column[:-2]
    arvo20.append(float(column))


subtracted = []
for item1, item2 in zip(arvo100, arvo20):
    item = item1 - item2
    subtracted.append(float(item))
jäännös= []
for i in subtracted:
    if i>0:
        i=1
    if i<0:
        i=-1
    jäännös.append(i)

def piirto2(jäännös):

    fig, ax = plt.subplots()
    plt.plot(jäännös)
    
    

piirto2(jäännös)
plt.show()  


tiedosto.to_csv('ema100.csv',encoding='utf-8', index=False)
tiedosto2.to_csv('ema20.csv',encoding='utf-8', index=False)