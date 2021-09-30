#A list of my stocks
#Using JSON to save data and retrieve/read

import pandas as pd
import json


#Creating JSON Data via Lists of Dictionaries
stock = [
    {"Name":"Gamestop", "Ticker":"GME", "Shares" :4, "Price": 349.85, "Cost": 1399},
    {"Name":"AMC", "Ticker":"AMC", "Shares" :120, "Price": 14.30, "Cost": 1716},
    {"Name":"Black Berry", "Ticker":"BB", "Shares" :120, "Price": 17.80, "Cost": 2136},
    {"Name":"AMD", "Ticker":"AMD", "Shares" :100, "Price": 0, "Cost": 1196.95},
    {"Name":"Canopy Growth", "Ticker":"CGC", "Shares" :100, "Price": 0, "Cost": 997.55},
    {"Name":"iRobot", "Ticker":"IRBT", "Shares" :10, "Price": 0, "Cost": 1339.50},
]


def saveit():
    with open('C:/Users/billt/Documents/Python/stock.json', 'w') as f:
        json.dump(stock, f)

def readit():
    stock_df = pd.read_json('C:/Users/billt/Documents/Python/stock.json')
    print(stock_df.head(6))

    #trying to add the total cost together
    sumtime = stock_df['Cost'].tolist()
    print(sumtime)

#saveit()
readit()