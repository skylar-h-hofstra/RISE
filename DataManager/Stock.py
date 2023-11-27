from bs4 import BeautifulSoup
import requests
import test
from Table import Table
from Graph import Graph

class Stock:
    def __iter__(self):
        return iter([
            ('ticker', self.ticker),
            ('url', self.url),
            ('current_price', self.current_price),
            ('headers', self.headers)
        ])
    
    #Constructor
    def __init__(self, ticker):
        #Base Stock Attributes
        self.ticker = ""
        self.url = ""
        self.soup = ""
        self.current_price = -1
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0'}

        self.Table = None

        self.Graph = None

        #Initializer Call
        self.update_stock(ticker)

    #Stock Initializer/Update Function
    def update_stock(self, new_ticker):
        self.update_ticker(new_ticker)
        self.update_url()
        self.update_soup()
        self.update_table()
        self.update_graph("2m", "1d")

    #Ticker:
    def update_ticker(self, new_ticker):
        self.ticker = new_ticker

    #URL:
    def update_url(self):
        self.url = f"https://finance.yahoo.com/quote/{self.ticker}?p={self.ticker}"

    #Soup:
    def update_soup(self):
        self.soup = str(self.get_soup())

    def get_soup(self):
        response = requests.get(self.url, headers=self.headers)
        return BeautifulSoup(response.text, "html.parser")

    #Table:    
    def update_table(self):
        if self.Table == None:
            self.Table = Table(self.get_table())
        else:
            self.Table.update_table(self.get_table())
            
    def get_table(self):
        result = BeautifulSoup(self.soup, "html.parser").find_all('td')
        return result

    #Graph:
    def update_graph(self, interval, range):
        self.interval = interval
        self.range = range
        if self.Graph == None:
            self.Graph = Graph(self.ticker, self.interval, self.range)
        else:
            self.Graph.update_graph(self.ticker, self.interval, self.range)




    #DEBUGGING: Used to Interpret Soup Contents
    def print_soup(self):
        print(self.soup)

    #Stock Price Function:
    def get_stock_price(self):
        current = self.soup.select_one(f'fin-streamer[data-field="regularMarketPrice"][data-symbol="{self.ticker}"]')
        self.current_price = current['value']
        return self.current_price

    #DEBUGGING: Used to Interpret Table Data Output
    def print_table(self):
        self.Table.print_table()

    def print_graph(self):
        self.Graph.update_graph_json()

""" RESERVE: Working Current Price Function
    def pull_data(self):
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        current = soup.select_one(f'fin-streamer[data-field="regularMarketPrice"][data-symbol="{ticker}"]')
        print(current['value'])
        #with open("") as fp:
        #    return BeautifulSoup(fp, "html.parser")
"""

""" RESERVE: Traversing Table Data
counter = 0
for row in result:
    #Accesses Data Values
    if counter % 2 == 1: 
        print(row.text)
    counter += 1

    #Accesses Data Labels
    if counter % 2 == 0: 
        print(row.text)
"""

""" TESTING: HTML Access and Soup Creation 
    with open("DataManager/test.html") as fp:
        self.soup = BeautifulSoup(fp, "html.parser")
    print(soup)
"""