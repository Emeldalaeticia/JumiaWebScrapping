import requests 
from bs4 import BeautifulSoup

baseurl = 'https://www.jumia.co.ke/'
result = requests.get(baseurl) 
soup = BeautifulSoup(result.content, 'html.parser')

productlist = soup.find_all('div', class_= 'itm col')

productlinks = []

for item in productlist:
    for link in item.find_all('a', href=True):
        productlinks.append(baseurl + link['href'])

print(len(productlinks))

