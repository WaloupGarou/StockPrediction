import pandas as pd
import csv
import yahoo_fin.stock_info as si 
import yfinance as yf

table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]
df = df["Symbol"].to_list()

meta = yf.Ticker("META")
dict =  meta.info
df = pd.DataFrame.from_dict(dict,orient='index')
df = df.reset_index().to_csv("test.csv",sep=",")
with open('test.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
data = [[l[1],l[2]] for l in data ]    
print(data)