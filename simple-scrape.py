# scraper-python.py
# code by Joe Osborne, https://medium.com/@joerosborne/intro-to-web-scraping-build-your-first-scraper-in-5-minutes-1c36b5c4b110
# To run this script, paste `python scraper-python.py` in the terminal

import requests
from bs4 import BeautifulSoup


def scrape():
    
    url = 'https://www.example.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print soup: outputs all of the HTML for the page
    # print(soup)
    title = soup.select_one('h1').text
    text = soup.select_one('p').text
    link = soup.select_one('a').get('href')

    print(title)
    print(text)
    print(link)


if __name__ == '__main__':
    scrape()