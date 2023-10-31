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
    return html



"""
def parse_price():
    r = requests.get(url_main.format(stock, stock))
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    print(soup)
    #price = soup.find_all('div', {"class":"Fw(b) Fz(36px) Mb(-4px) D(ib)"})
    #return price
"""

print(get_price(stock))