import requests
from urllib.request import Request, urlopen

class Graph:
    #def __dict__()
    
    def __init__(self, ticker: str, interval: str, range: str):
        self.ticker = ""
        self.interval = ""
        self.range = ""
        self.graph_url = ""
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0'}
        self.graph_json = None
        

        #Initializer Call
        self.update_graph(ticker, interval, range)

    #Graph Initializer/Update Function
    def update_graph(self, ticker, interval, range):
        self.update_graph_ticker(ticker)
        self.update_graph_interval(interval)
        self.update_graph_range(range)
        self.update_graph_url()
        self.update_graph_json()

    def update_graph_ticker(self, ticker):
        self.ticker = ticker

    def update_graph_interval(self, interval):
        self.interval = interval
    
    def update_graph_range(self, range):
        self.range = range

    def update_graph_url(self):
        self.graph_url = f"https://query1.finance.yahoo.com/v8/finance/chart/{self.ticker}?region=US&lang=en-US&includePrePost=false&interval={self.interval}&useYfid=true&range={self.range}&corsDomain=finance.yahoo.com&.tsrc=finance"
    
    def update_graph_json(self):
        data_request = Request(self.graph_url, headers=self.headers)
        page = urlopen(data_request)
        self.graph_json = page.read().decode("utf-8")
        #print(self.graph_json)