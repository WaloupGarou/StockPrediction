import pandas as pd
import csv
import yfinance as yf

table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]
df = df["Symbol"].to_list()

amazon = yf.Ticker("AMZN")
balance_sheet = amazon.balance_sheet
income_statement = amazon.income_stmt
cash_flow = amazon.cashflow

"""
print("                 #######cashflow############")
print(cash_flow)
print("                 #######incomestatement############")
print(income_statement)
print("                 #######balance_sheet############")
print(balance_sheet)

print("                 #######financials############")
print(amazon.financials)

df = pd.DataFrame.from_dict(dict,orient='index')
df = df.reset_index().to_csv("test.csv",sep=",")

with open('test.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
data = [[l[1],l[2]] for l in data ]    
"""

info = amazon.history(period="max")
print(info["regularMarketEPS"])