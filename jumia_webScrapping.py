import requests 
from bs4 import BeautifulSoup
import csv

baseurl = 'https://www.jumia.co.ke/'

productlinks = []


for x in range (1,6):

    result = requests.get(f'https://www.jumia.co.ke/mlp-free-delivery/?page={x}#catalog-listing') 
    soup = BeautifulSoup(result.content, 'html.parser')

    productlist = soup.find_all('div', class_= 'itm col')

    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl + link['href'])

# print(len(productlinks))

# testlink = 'https://www.jumia.co.ke/new-sports-casual-fashion-sports-mens-shoes-white-fashion-mpg248626.html'

for link in productlinks:
    result = requests.get(link)

    soup = BeautifulSoup(result.content, 'html.parser')


    name = soup.find('h1', class_='-fs20 -pts -pbxs').text.strip()
    
    price = soup.find('span', class_='-b -ltr -tal -fs24').text.strip()
    try:
        rating = soup.find('div', class_='stars _s _al').text.strip()
    except: 
        rating = 'no rating'
   
    # discount = soup.find('span', class_='bdg _dsct _dyn -mls').text.strip()

    try:
        no_of_ratings = soup.find('a', class_='-plxs _more').text.strip()
    except:
        no_of_ratings = 'unavailable'

    try:
        no_of_reviews = soup.find('h2', class_='-fs14 -m -upp -ptm').text.strip()
    except:
        no_of_reviews = 'unavailable'

# Create a dictionary to store the information
    product = {
        'name' : name,
        'rating' : rating,
        'price': price,
        'no_of_ratings' : no_of_ratings,
        'no_of_reviews' : no_of_reviews
    }
# print(name, rating, price, no_of_ratings, no_of_reviews)


print(product)


# Create a list of dictionary to store the product information
products = [product]

# Open the CSV file in write mode
with open('products.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=product.keys())
    writer.writeheader()
    for product in products:
        writer.writerow(product)