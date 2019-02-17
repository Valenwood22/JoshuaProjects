
__author__ = "Timothy Alexander, Joshua Gisi"
__copyright__ = "Copyright 2018, Project Money Tree"
__version__ = "SupportJack1.0Alpha"
__email__ = "TJEnterprises2019@gmail.com"
__status__ = "pre-Alpha"

#<editor-fold desc="Imports">
import math
import time
import json
import datetime
import configparser
import sqlite3

# import tensorflow as tf

import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.positions as positions

from oandapyV20 import API
from oandapyV20.contrib.requests import ( MarketOrderRequest, TakeProfitDetails,  StopLossDetails, PositionCloseRequest)
# from twilio.rest import Client

#</editor-fold

#<editor-fold desc="Credentials">
accountID = "xxx-xxx-xxxxxxx-xxx"
api = API(access_token="xxxxxxxxxxxxxxxxxxxxxxxx", environment="live", headers=None)
#</editor-fold>



def exeSql(command):
    connection = sqlite3.connect('Database/currenciesDB')

    # Get a cursor to execute sql statements
    cursor = connection.cursor()

    cursor.execute(command)
    rows = cursor.fetchall()
    connection.close()
    return rows

def getCandleStick():
    client = api
    paramsV = {"count": 1, "granularity": "M15"}
    v = instruments.InstrumentsCandles(instrument="EUR_USD", params=paramsV)
    client.request(v)
    return v.response['candles'][0]

'''
Key
[0] = PID
[1] = time stamp
[2] = open
[3] = high
[4] = low
[5] = close
[6] = volume
'''

if __name__ == '__main__':
    #rtrn = exeSql("SELECT * FROM EUR_USD10to16 WHERE PID = 3")
    print(getCandleStick())





