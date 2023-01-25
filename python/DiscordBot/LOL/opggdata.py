import requests
from bs4 import BeautifulSoup
#https://eune.op.gg/summoner/userName=olio
URL= 'https://yle.fi/'
r = requests.get(URL)

soup = BeautifulSoup(r.content, "html.parser")
#with open('rawdata.txt', 'w') as f:
   #f.write(str(soup))
#print(soup)
results = soup.find_all("div", {"class": "yle-header-search-input"})
print(results)