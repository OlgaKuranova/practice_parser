import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(soup, quotes):
    quote_elements = soup.find_all('div', class_='quote')

    for quote_element in quote_elements:
        text = quote_element.find('span', class_='text').text
        author = quote_element.find('small', class_='author').text

        quotes.append(
            {
                'text': text,
                'author': author,
            }
        )

main_url = 'https://quotes.toscrape.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/107.0.0.0  YaBrowser/24.4.1.899 Safari/537.36'
}
page = requests.get(main_url, headers=headers)

bs = BeautifulSoup(page.text, 'html.parser')

quotes = []

scrape_page(bs, quotes)

next_li_element = bs.find('li', class_='next')

while next_li_element is not None:
    next_page_url_element = next_li_element.find('a', href=True)['href']
    page = requests.get(main_url + next_page_url_element, headers=headers)
    bs = BeautifulSoup(page.text, 'html.parser')
    scrape_page(bs, quotes)
    next_li_element = bs.find('li', class_='next')


csv_file = open('quotes.csv', 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(csv_file)
writer.writerow(['Text', 'Author'])

for quote in quotes:
    writer.writerow(quote.values())

csv_file.close()