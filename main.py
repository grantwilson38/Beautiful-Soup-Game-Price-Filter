from bs4 import BeautifulSoup
import requests

# Ask the user for a URL
url = input("Please enter a URL: ")

# Fetch the content from the URL
response = requests.get(url)

# Parse the content with BeautifulSoup
doc = BeautifulSoup(response.text, 'html.parser')

# Find all 'h4' elements
h4_elements = doc.find_all('h4')

# Initialize an empty list to hold the h4 text and associated prices
h4_price_list = []

# For each h4 element
for h4 in h4_elements:
	# Find the next 'p' element with class 'priceProductHolder'
	price = h4.find_next('p', class_='priceProductHolder')
	# If a price was found
	if price is not None:
		# Add the h4 text and price text to the list, stripping leading and trailing whitespace
		h4_price_list.append((h4.get_text().strip(), price.get_text().strip()))

# Ask the user for a price
user_price = float(input("Please enter a price: "))

# Print the games that are below the user's price
for item in h4_price_list:
	# Remove the dollar sign and convert the price to a float
	price = float(item[1].replace('$', ''))
	# If the price is less than the user's price
	if price < user_price:
		# Print the game and its price
		print(f"{item[0]}: {item[1]}")