# api key 2AZ0R3B5JKBC14EQ
# must install requests if not installed, but should be preinstalled with pip
import requests
import pandas as pd
import pymongo
from bs4 import BeautifulSoup
from pymongo import MongoClient
from urllib.request import urlopen
from urllib.request import Request
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

CONNECTION_STRING= 'mongodb+srv://izzy:izzy123@cluster0.gv1uuxn.mongodb.net/'
client=MongoClient(CONNECTION_STRING)
collection_name=client['TempInfo']['TickerDay']
t='AAPL'

def Pull_Ticker(t):
    url='https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+t+'&interval=5min&apikey=A1CG6W2DT3G2A4W7'
    r = requests.get(url)
    data = r.json() 
    Push_To_Database(data)
    pdItem=pd.DataFrame.from_records(data)
    pdItem=pdItem.dropna
    print(pdItem)
    
    return pdItem

def Push_To_Database(data):
      collection_name.insert_one(data)

Pull_Ticker(t)

url='https://finance.yahoo.com/quote/aapl'
try:
  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
  req = Request(url=url,headers=headers) 
  resp = urlopen(req)    
except:
  raise Exception(f'Error for {etf}')
html = BeautifulSoup(resp, features="lxml")
