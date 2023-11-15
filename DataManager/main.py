from Stock import Stock

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

"""s.print_soup()

s.update_ticker("TSLA")

s.print_soup()"""

""" TESTING: Constant Price Update Testing
s = Stock("AAPL")
while(True):
    s.pull_data()
"""