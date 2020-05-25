import requests
URL= "https://www.worldometers.info/coronavirus/#countries"
page= requests.get(URL)
print(page)
from bs4 import BeautifulSoup
#from unidecode import unidecode
soup= BeautifulSoup(page.content,"html.parser")
#soup= unidecode(soup)
print(soup.encode("utf-8"))
