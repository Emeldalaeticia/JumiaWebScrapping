# JumiaWebScrapping
This code performs web scraping on the Jumia Kenya website to extract information about products, such as their names, ratings, prices, number of ratings, and number of reviews. The scraped data is then stored in a CSV file named "products.csv".


The code imports the necessary libraries: requests for making HTTP requests, BeautifulSoup for parsing HTML, and csv for working with CSV files.

The base URL for the Jumia Kenya website is defined as baseurl.

The code creates an empty list called productlinks to store the links to individual product pages.

A loop is used to iterate over the pages of the website (from page 1 to page 5). For each page, an HTTP GET request is made to retrieve the page content. The content is then parsed using BeautifulSoup to extract the links to product pages. These links are appended to the productlinks list.

After collecting all the product links, the code creates an empty list called products to store the scraped product information.

Another loop is used to iterate over each product link. For each link, an HTTP GET request is made to retrieve the product page content. The content is parsed using BeautifulSoup to extract the desired information such as the product name, price, rating, number of ratings, and number of reviews.

The scraped information for each product is stored in a dictionary called product.

Each product dictionary is appended to the products list.

The information for each product is printed.

Once all the products have been scraped, a CSV file named "products.csv" is opened in write mode using the csv module. A DictWriter object is created to write the data to the CSV file. The fieldnames for the CSV file are obtained from the keys of the first product dictionary in the products list. The header row is written to the CSV file using the writeheader() method. Then, for each product in the products list, the data is written to the CSV file using the writerow() method.
