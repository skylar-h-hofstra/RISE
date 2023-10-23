
import pyEX;


c = pyEX.Client(api_token='sk_96c6bd9e777f4c0589c75219df75a44a', version='v1', api_limit=5)
#print(c.chartDF('aapl'))

data=c.symbolsDF()


for d in data.index:
    print(d)
    print('_____')

def GetSymbol(string symbol):
    dc=c.ceoDem
    return




