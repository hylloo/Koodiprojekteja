from bs4 import BeautifulSoup
import requests

#URL= 'https://www.amazon.de/Amazon-Basics-Adjustable-Screens-Non-Slip/dp/B00X4SCCFG?ref_=ast_sto_dp&th=1&psc=1'
#headers = headers = {"User-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
#html_text = requests.get(URL, headers=headers)
html_text = requests.get('https://www.amazon.de/Amazon-Basics-Adjustable-Screens-Non-Slip/dp/B00X4SCCFG?ref_=ast_sto_dp&th=1&psc=1')
soup = BeautifulSoup(html_text, 'lxml')

title = soup.find_all('div')
#price = soup.find(id="priceblock_ourprice").get_text()