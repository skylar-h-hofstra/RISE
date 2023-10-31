import re
import json
from urllib import request
from urllib.request import Request, urlopen

#url_main = "https://finance.yahoo.com/quote/{}?p={}"
#url_hisorical = "https://finance.yahoo.com/quote/{}/history?p={}"
#url_stats = "https://finance.yahoo.com/quote/{}/key-statistics?p={}"
#url_profile = "https://finance.yahoo.com/quote/{}/profile?p={}"
#url_financial = "https://finance.yahoo.com/quote/{}/financials?p={}"

url = "https://query1.finance.yahoo.com/v8/finance/chart/{}?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance"

stock = "AAPL"

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
    #print(d3.meta)
    get_regularMarketPrice(d3)

def get_regularMarketPrice(d3):
    d4 = DummyClass()
    d4.__dict__ = d3.meta
    print(d4.regularMarketPrice)

def live_data_feed(stock):
    while True:
        get_price(stock)



class DummyClass:
    pass

"""
def parse_price():
    r = requests.get(url_main.format(stock, stock))
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    print(soup)
    #price = soup.find_all('div', {"class":"Fw(b) Fz(36px) Mb(-4px) D(ib)"})
    #return price
"""

live_data_feed(stock)