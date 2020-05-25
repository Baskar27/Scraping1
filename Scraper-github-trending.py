import requests
from bs4 import BeautifulSoup
# soup= Beautifulsoup('html','html.parser')
#page=requests.get('https://github.com/Baskar27/Scraping1.git')

page=requests.get('https://github.com/trending')
print(page)
soup=BeautifulSoup(page.text,'html.parser')
print(soup.encode("utf-8"))
#create a BeautifulSoup object
