from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date
import numpy as np
import math
import csv
from pandas import DataFrame
import os
from aika import end_date, start_date
from numpy import var
from tkinter import *
from PIL import ImageTk,Image
import sqlite3

def piirto(short_rolling_msft, long_rolling_msft, very_long_rolling_msft):

    fig, ax = plt.subplots(figsize=(16,9))
    ax.plot(valinta.index, valinta, label=valinta)
    ax.plot(short_rolling_msft.index, short_rolling_msft, label='20 days rolling')
    ax.plot(long_rolling_msft.index, long_rolling_msft, label='100 days rolling')
    #ax.plot(very_long_rolling_msft.index, very_long_rolling_msft, label='200 days rolling')

    ax.set_xlabel('Date')
    ax.set_ylabel('Adjusted closing price ($)')
    ax.legend()
    plt.show()
    return

def viivat(valinta):

    # Create a database or connect to one
	conn = sqlite3.connect('valinta.db')
	# Create cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT *, oid FROM valinta")
	records = c.fetchone()
	# Loop Thru Results
	print_records = ''
	for record in records:
		print_records += str(record[0])  

      #Commit Changes
	conn.commit()
	# Close Connection 
	conn.close()

  

panel_data = data.DataReader(print_records, 'yahoo', start_date, end_date)
close = panel_data['Close']
msft = closemsft = close.loc[:, print_records]


short_rolling_msft = msft.rolling(window=20).mean()
short_rolling_msft=round(short_rolling_msft,4)
long_rolling_msft = msft.rolling(window=100).mean()
long_rolling_msft=round(long_rolling_msft,4)

ema20=[]
ema100=[]

for i in msft: 
    close20=short_rolling_msft[int(i)]
    try:
        ema20.append(int(close20))
    except:
        pass


for i in msft: 
    close100=long_rolling_msft[int(i)]
    try:
        ema100.append(int(close100))
    except:
        pass
    


very_long_rolling_msft = msft.rolling(window=200).mean()
piirto(short_rolling_msft, long_rolling_msft, very_long_rolling_msft)


viivat()
