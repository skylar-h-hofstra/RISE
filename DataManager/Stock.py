from bs4 import BeautifulSoup
import requests
import test

class Stock:
    #Constructor
    def __init__(self, ticker):
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0'}
        self.update_stock(ticker)
        
    def update_stock(self, new_ticker):
        self.update_ticker(new_ticker)
        self.update_url()
        self.update_soup()

    def update_ticker(self, new_ticker):
        self.ticker = new_ticker

    def update_url(self):
        self.url = f"https://finance.yahoo.com/quote/{self.ticker}?p={self.ticker}"

    def update_soup(self):
        self.soup = self.get_soup()

    def get_soup(self):
        response = requests.get(self.url, headers=self.headers)
        return BeautifulSoup(response.text, "html.parser")

    def print_soup(self):
        print(self.soup)

    def get_stock_price(self):
        current = self.soup.select_one(f'fin-streamer[data-field="regularMarketPrice"][data-symbol="{self.ticker}"]')
        return current['value']


""" RESERVE: Working Current Price Function
    def pull_data(self):
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        current = soup.select_one(f'fin-streamer[data-field="regularMarketPrice"][data-symbol="{ticker}"]')
        print(current['value'])
        #with open("") as fp:
        #    return BeautifulSoup(fp, "html.parser")
"""

""" TESTING: HTML Access and Soup Creation 
    with open("DataManager/test.html") as fp:
        self.soup = BeautifulSoup(fp, "html.parser")
    print(soup)
"""