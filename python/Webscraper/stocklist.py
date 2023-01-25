from symtable import Symbol
import pandas as pd
import csv

table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]
df.to_csv('S&P500-Info.csv')
df.to_csv("S&P500-Symbols.csv", columns=['Symbol'])

with open('S&P500-Symbols.csv', newline='') as f:
    reader = csv.reader(f)
    ticker = list(reader)

for i in ticker:
    del i[0]
ticker=ticker[1:]
for i in ticker:
    x=str(i[:])
