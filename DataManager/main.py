import re
import json
from urllib import request
from urllib.request import Request, urlopen
import time
from bs4 import BeautifulSoup
from openpyxl import load_workbook


#url_main = "https://finance.yahoo.com/quote/{}?p={}"
#url_hisorical = "https://finance.yahoo.com/quote/{}/history?p={}"
#url_stats = "https://finance.yahoo.com/quote/{}/key-statistics?p={}"
#url_profile = "https://finance.yahoo.com/quote/{}/profile?p={}"
#url_financial = "https://finance.yahoo.com/quote/{}/financials?p={}"

url = "https://query1.finance.yahoo.com/v8/finance/chart/{}?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance"

stock = "TSLA"

def get_price(stock):
    request_site = Request(url.format(stock), headers={"User-Agent":"Mozilla/5.0"})
    webpage = urlopen(request_site)
    html_byte = webpage.read()
    html = html_byte.decode("utf-8")
    pass_chart(html)
    #print(html)

def pass_chart(file):
    d = DummyClass()
    d.__dict__ = json.loads(file)
    # print(d.chart)
    pass_result(d)

def pass_result(d):
    d2 = DummyClass()
    d2.__dict__ = d.chart
    #print(d2.result)
    pass_meta(d2)

def pass_meta(d2):
    d3 = DummyClass()
    d3.__dict__ = d2.result[0]
    print(d3.meta)
    get_regularMarketPrice(d3)

def get_regularMarketPrice(d3):
    d4 = DummyClass()
    d4.__dict__ = d3.meta
    #print(d4.regularMarketPrice)

def live_data_feed(stock):
    while True:
        get_price(stock)
        time.sleep(1)


def getTickSymbol():
    data_file = 'DataManager/NASDAQ List.csv' #the csv file 
    wb = load_workbook(data_file) #loads the file 
    ws = wb['NASDAQ List'] #loads the specific sheet
    all_rows = list(ws.rows)    #gets the rows 
    Tickers = []                # using a list? might not be good tho if we want to read thru it
    for cell in all_rows[0]:    # first row, thats where the ticker symbols are 
        Tickers.append(row.value)

#https://ehmatthes.github.io/pcc_2e/beyond_pcc/extracting_from_excel/


class DummyClass:
    pass

get_price("TSLA")

"""
def parse_price():
    r = requests.get(url_main.format(stock, stock))
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    print(soup)
    #price = soup.find_all('div', {"class":"Fw(b) Fz(36px) Mb(-4px) D(ib)"})
    #return price(
"""

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

def get_news(stock):
    url='https://www.cnbc.com/quotes/' + stock + '?tab=news'
    try:
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        req = Request(url=url,headers=headers) 
        resp = urlopen(req)    
    except:
        print("no link")
    html = BeautifulSoup(resp, features="html.parser")

    #finds a class and finds the latest news while making sure href is true
    for row in html.find_all('a', class_='LatestNews-headline', href = True):
        print(row.text)
        print(row['href'])
    
    

        
# parse_graph(stock)
# live_data_feed(stock)
get_news('AAPL')
