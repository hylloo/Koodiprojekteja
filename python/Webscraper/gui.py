from cProfile import label
from cgitb import enable
from stocklist import ticker
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

root = Tk()
root.title('STOCK ANALYSIS')
root.iconbitmap('C:/Users/pitka/OneDrive/Työpöytä/python/webscraper/images/bitmap.ico')
root.geometry('400x400')
#label widget


# Create a database or connect to one
conn = sqlite3.connect('valinta.db')
#c.execute("""CREATE TABLE valinta(
# valinta text)
#""")
c=conn.cursor()

valinta= Entry(root, width=40, borderwidth=4)

e = Entry(root, width=40, borderwidth= 4)
e.grid(row=0, column=0, columnspan=30, padx=100, pady=100)
e.pack()
e.get()
e.delete(0,END)
e.insert(0,'')

def show():
    e.delete(0,END)
    if len(e.get())==0:
        stock=clicked.get()
    else:
        stock=e.get()
    stock=str(stock[1:-1])

    label = Label(root,borderwidth=5, text='Loading '+ stock + ' Stock Price')
    valinta=stock
    label.pack()
    df=valinta
    
    #print(valinta)
    return(valinta)

def klikkaus2():
    label = Label(root,borderwidth=5, text='Exiting...')
    label.pack()

def submit():
    #clear textbox
    e.delete(0,END)

    stock=clicked.get()
    label = Label(root,borderwidth=5, text='Loading '+ stock + ' Stock Price')
    valinta=stock
    label.pack()
    conn = sqlite3.connect('valinta.db')
    c=conn.cursor()

    #insert into table
    c.execute("INSERT INTO valinta VALUES(:valinta)",
    {
        'valinta': valinta
    })

    #commit and close connection
    conn.commit()
    conn.close()
    print(valinta)
    return valinta


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


def viivat(valinta):

    # Create a database or connect to one
	conn = sqlite3.connect('valinta.db')
	# Create cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT *, oid FROM valinta")
	records = c.fetchall()
	# Loop Thru Results
	print_records = ''
	for record in records:
		print_records += str(record[0]) 

    #Commit Changes
	conn.commit()
	# Close Connection 
	conn.close()

def hakemus(valinta):
    panel_data = data.DataReader(valinta, 'yahoo', start_date, end_date)
    close = panel_data['Close']
    msft = closemsft = close.loc[:, valinta]


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


viivat(valinta)
hakemus(valinta)
piirto(short_rolling_msft, long_rolling_msft, very_long_rolling_msft)



#very_long_rolling_msft = valinta.rolling(window=200).mean()





nappi1= Button(root, text= 'Add selected stock to database', borderwidth=3,state=ACTIVE, padx=20, pady=10, command=submit)
nappi_quit= Button(root, text= 'Exit', borderwidth=3,state=ACTIVE, padx=20, pady=10, command=root.quit)
query_btn = Button(root, text="Show Database", command=viivat)
query_btn.pack()

#submit.pack()
#print (ticker)
clicked=StringVar()
drop= OptionMenu(root, clicked, *ticker)


#työnnetään näytölle
drop.pack()
nappi1.pack()
nappi_quit.pack()

var = IntVar()


c1= Checkbutton(root,text='Enable EMA 100', variable=var)
c2= Checkbutton(root,text='Enable EMA 20', variable=var)


c1.pack()
c2.pack()

conn.commit()
conn.close()
root.mainloop()
