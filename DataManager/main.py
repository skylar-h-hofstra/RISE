from Stock import Stock


s = Stock("TSLA")
s.print_table()




"""
import re
import json
from urllib import request
from urllib.request import Request, urlopen
import time
from bs4 import BeautifulSoup
#from openpyxl import load_workbookp
def parse_graph(ticker):
    url='https://finance.yahoo.com/quote/'+ticker

    print(url)
    try:
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        req = Request(url=url,headers=headers) 
        resp = urlopen(req)    
    except:
        print("no link")
    html = BeautifulSoup(resp, features="html.parser")

    for row in html.find_all('td'):
        
        print(row.text)

parse_graph("AAPL")
"""


"""
s = Stock("MSFT")
s2 = Stock("TSLA")

while(True):
    print("MSFT: " + s.get_stock_price())
    print("TSLA: " + s2.get_stock_price())
"""


"""
s = Stock("MSFT")

def debugging_module(ticker):
    s.update_stock(ticker)
    print(s.ticker)
    print(s.headers)
    print(s.url)
    print(s.get_stock_price())
    #print(s.soup)
    #s.print_soup()

debugging_module("TSLA")
debugging_module("AAPL")
"""


"""s.print_soup()

s.update_ticker("TSLA")

s.print_soup()"""

""" TESTING: Constant Price Update Testing
s = Stock("AAPL")
while(True):
    s.pull_data()
"""