# Web Scrapping

import requests
from bs4 import BeautifulSoup  #Analyse et extraction des données
import pandas as pd            #Manipulation des données

names = []
prices = []
images = []
for i in range(0, 24):
    page = requests.get("https://www.jumia.ma/smartphones-android/?page=" +str(i))
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find(class_='-paxs row _no-g _4cl-3cm-shs')
    items = data.find_all(class_='prd _fb col c-prd')    #Chaque produit
    names = names + [item.find(class_='name').text for item in items]
    prices = prices + [item.find(class_='prc').text for item in items]
    images = images + [item.find(class_='img').get('data-src') for item in items]
    print('Web Scraping ......:', i)
df = pd.DataFrame({
    'nom de téléphone': names,
    'prix': prices,
    'images': images
})
df.to_csv('telephones_android.csv')
df.to_html('telephones_android.html')