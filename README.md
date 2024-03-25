**Beautiful Soup Web Scraper**

This Python script uses the BeautifulSoup library to scrape a webpage for 'h4' elements and associated prices. It then filters and prints the items that are below a user-specified price.

**Requirements**

- Python 3
- BeautifulSoup
- requests
- You can install the required Python packages with pip:

**Usage**

To run the script, use the following command:

When prompted, enter the URL of the webpage you want to scrape. The script will fetch the content of the webpage and parse it with BeautifulSoup.

It will then find all 'h4' elements on the page and for each 'h4' element, it will find the next 'p' element with the class 'priceProductHolder'. If a price is found, it will add the 'h4' text and price text to a list, stripping leading and trailing whitespace.

After all 'h4' elements and associated prices have been found, the script will prompt you to enter a price. It will then print all items that are below the price you entered.

**Note**

This script is intended for educational purposes only. Always respect the terms of service of the website you are scraping.
