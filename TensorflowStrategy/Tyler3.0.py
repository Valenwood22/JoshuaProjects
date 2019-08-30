
__author__ = "Joshua Gisi, Timothy Alexander"
__copyright__ = "2019, Project Money Tree"
__version__ = "Tyler3.0"
__email__ = "TJEnterprises2019@gmail.com"
__status__ = "Demo"
__DatabaseFilePath__ = "/root/Tyler+Jack/Database/currenciesDB"



# <editor-fold desc="Imports">
import math
import sqlite3
import sys
import time
from datetime import datetime
import numpy as np
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.pricing as pricing
import pytz
from oandapyV20 import API
from oandapyV20.contrib.requests import (MarketOrderRequest, TakeProfitDetails, StopLossDetails)
from twilio.rest import Client
# </editor-fold



# <editor-fold desc="Twilio Setup">
# Twilio authentication setup
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
client = Client(account_sid, auth_token)
# </editor-fold>



# <editor-fold desc="Variables">
# An array of all the currencies the bot will be checking
currencies = ["AUDCAD", "EURCHF", "EURGBP", "NZDCAD", "USDCAD", "USDCHF", "NZDUSD", "EURUSD", "GBPUSD", "AUDUSD"]
currenciesIndex = {}
for i in range(len(currencies)):    # Creates a dictionary from the currency list
    currenciesIndex[currencies[i]] = i
# Initiate global variables
probabilities = [0] * len(currencies)
leverage = 20
oldTrade = False
buyConditions = [0] * 22
sentError = False
lastPID = [0] * len(currencies)
doNotBuy = False
# </editor-fold



# <editor-fold desc="Credentials">
# Oanda API Credentials setup (should be encrypted)
accountID = "xxx-xxx-xxxxxxx-xxx"
api = API(access_token="xxxxxxxxxxxxxxxxxxxxxxxx", environment="live", headers=None)
# </editor-fold>







def exeSqlInsert(command):
    """
    Used to insert new rows into the database such as order information
    :param command: A string containing a SQL 'Insert' command
    :return:
    """
    connection = sqlite3.connect(__DatabaseFilePath__)  # Create a database if not exists and get a connection to it
    cursor = connection.cursor()    # Get a cursor to execute sql statements
    cursor.execute(command)     # Execute the insert command
    connection.commit()
    connection.close()







def exeSqlSelect(command):
    """
    Used to select data from the database such as candlesticks
    :param command: A string containing a SQL 'Select' command
    :return: The resulting rows as a matrix
    """
    connection = sqlite3.connect(__DatabaseFilePath__)  # Create a database if not exists and get a connection to it
    cursor = connection.cursor()    # Get a cursor to execute sql statements
    cursor.execute(command)
    rows = cursor.fetchall()
    connection.close()
    return rows







def openPosition(money, currency, stopLoss, takeProfit):
    """
    Creates a new buy order
    :param money: Amount to buy
    :param currency: Currency pair to buy
    :param stopLoss: Stop loss price
    :param takeProfit: Take profit price
    :return:
    """
    exchange = currency[:3] + "_" + currency[3:]    # Format the currency pair by removing the '_'
    stopLossOnFill = StopLossDetails(price=stopLoss)    # Stop loss and take profit details
    takeProfitOnFill = TakeProfitDetails(price=takeProfit)
    mo = MarketOrderRequest(instrument=exchange, units=money, stopLossOnFill=stopLossOnFill.data,
                            takeProfitOnFill=takeProfitOnFill.data)  # exchange="EUR_USD"
    time_current = datetime.now(pytz.timezone('America/Chicago'))
    r = orders.OrderCreate(accountID, data=mo.data)     # Create the order request
    rv = api.request(r)     # perform the request







def getPrice(currency):
    """
    An API request to get the current price at the given pair
    :param currency: Currency pair to get current price
    :return: A float of the current price
    """
    pair = currency[:3] + "_" + currency[3:]    # Format the currency pair by removing the '_'
    params = {"instruments": pair}
    r = pricing.PricingInfo(accountID=accountID, params=params)
    rv = api.request(r)     # Create the order request
    r = r.response["prices"][0]["asks"][0]['price']     # parse response from dictionary
    r = float(r)    # convert data to a float
    return r







def getSpread(currency):
    """
    Gets the spread of the given pair
    :param currency: Currency to get the spread of
    :return: A float that represents the difference between the buy and sell prices
    """
    pair = currency[:3] + "_" + currency[3:]    # Format the currency pair by removing the '_'
    params = {"instruments": pair}
    r = pricing.PricingInfo(accountID=accountID, params=params)
    rv = api.request(r)     # Create the order request
    sell = r.response['prices'][0]['bids'][0]['price']  # parse response from dictionary
    buy = r.response['prices'][0]['asks'][0]['price']
    spread = float(buy) - float(sell)
    return spread







def inTrade():
    """
    Gets whether the bot is currently in a trade so it doesnt double order
    :return: A boolean representing if the bot is in a trade
    """
    r = accounts.AccountDetails(accountID)
    try:
        api.request(r)
        currentPosition = int(r.response["account"]["openPositionCount"])
        if currentPosition == 0:    # If open position count is 0 the bot is not in a trade
            return False
        else:
            return True
    except ConnectionError as e:
        write("\n\nConnection Exception in inTrade()")
        write(e)
        return oldTrade
    except:
        write("\n\nUnknown Error in inTrade()")
        return oldTrade







def getBalance():
    """
    Gets the account balance
    :return: A float that represents the amount of money in the account
    """
    r = accounts.AccountDetails(accountID)
    api.request(r)
    balance = r.response["account"]["balance"]
    balance = float(balance)
    return balance







def getRow(currency):
    """
    A method that has the SQL command preformatted to select one row from the candle chart
    :param currency: Currency to get return the row of
    :return: An array with the candle data
    """
    rtrn = exeSqlSelect("SELECT * FROM " + str(currency) + "_Candles WHERE PID = ( SELECT MAX(PID) FROM " + str(
        currency) + "_Candles )")
    return rtrn[0];







def getIndicatorRow(currency):
    """
    A method that has the SQL command preformatted to select one row from the indicator chart
    :param currency: Currency to get return the row of
    :return: An array with the indicator data
    """
    rtrn = exeSqlSelect("SELECT * FROM " + str(currency) + "_Indicators ORDER BY PID desc limit 2")
    row = [rtrn[0][2] / 50, rtrn[0][3] / 50, rtrn[0][4] / 20, rtrn[0][5] * 400000, rtrn[0][6], rtrn[0][7],
           rtrn[1][2] / 50, rtrn[1][3] / 50, rtrn[1][4] / 20, rtrn[1][5] * 400000, rtrn[1][6], rtrn[1][7]]
    return rtrn[0][0], row







def checkRowPID(i, pid):
    """
    Check that a duplicate row is not being inserted
    :param i: Index for the lastPID Array
    :param pid: Current pid
    :return:
    """
    write("last row before: " + str(lastPID[i]) + "pid" + str(pid))
    if (lastPID[i] == pid):
        doNotBuy = True
    lastPID[i] = pid
    write("last row after: " + str(lastPID[i]) + "pid" + str(pid))







def softmax(X, theta=1.0, axis=None):
    """
    Compute the softmax of each element along an axis of X.
    :param X: ND-Array of floats.
    :param theta: (optional): float parameter, used as a multiplier prior to exponentiation. Default = 1.0
    :param axis: (optional): axis to compute values along. Default is the first non-singleton axis.
    :return: An array the same size as X. The result will sum to 1 along the specified axis.
    """
    y = np.atleast_2d(X)    # make X at least 2d
    if axis is None:    # find axis
        axis = next(j[0] for j in enumerate(y.shape) if j[1] > 1)

    y = y * float(theta)    # multiply y against the theta parameter,
    y = y - np.expand_dims(np.max(y, axis=axis), axis)  # subtract the max for numerical stability
    y = np.exp(y)   # exponentiate y
    ax_sum = np.expand_dims(np.sum(y, axis=axis), axis)     # take the sum along the specified axis
    p = y / ax_sum  # divide elementwise
    if len(X.shape) == 1: p = p.flatten() # flatten if X was 1D
    return p







def probabilityOfWinning(row):
    """
    Finds the portability of winning a trade based on back testing data and indicator row
    :param row: A set of indicator values
    :return: A float representing the probability of winning the trade
    """
    x = row     # input row based on on indicator values
    # Hidden layer of the network. Initiate first weight derived from TensorFlow on the back testing data
    W_first = [[0.2674143, -0.13602254, 0.25855905, -0.63510758, 0.27080637, -0.44800586],
               [-0.2118697, -0.17606132, -0.38301662, 0.22135556, -0.31785804, 0.88210326],
               [-0.07804935, 0.70079964, 0.1985106, 0.29745147, -0.52636606, -0.30851617],
               [-0.48654309, -0.32864228, -0.0277993, 0.15970418, -0.5472132, -0.02248748],
               [-0.11180561, 0.01589578, 0.4809337, -0.10619023, 0.27672544, 0.36266512],
               [-0.17766167, -0.20696238, 0.11279804, -0.42190251, -0.41778123, -0.14781103],
               [-0.10487799, -1.13296437, 0.82121748, -0.36616519, -0.13266717, -0.0323681],
               [-0.16874324, 0.23045945, -0.19771418, -0.59912908, -0.67152047, -0.34913382],
               [-0.09743168, 0.41105247, 0.40275237, -0.01321134, -0.49528709, 0.45305115],
               [-0.30838808, -0.40806404, 0.10838525, -0.17665125, 0.28190359, -0.32747224],
               [0.82682592, -0.51781052, -0.05786101, 0.73364472, -0.43769872, -0.09365544],
               [0.39350814, -0.10950764, 0.0027272, -0.24248472, 0.20206389, -0.69102567]]
    # Initiate the first bias derived from TensorFlow on the back testing data
    b_first = [0.30165455, -1.29986799, 0.59115952, -0.26020217, 0.40834394, -0.46914196]
    # Transforms the data from the weight and bias
    x_first = softmax(np.matmul(x, W_first) + b_first)

    # Hidden layer of the network. Initiate second weight derived from TensorFlow on the back testing data
    W_second = [[-1.23024571, -1.02231431], [-0.4900434, -0.09810875], [-0.14168939, -0.06477789],
                [0.66917253, -0.26791057], [-0.33941135, 0.59516281], [-0.6115821, 0.23300457]]
    # Initiate the second bias derived from TensorFlow on the back testing data
    b_second = [-0.19898981, -0.13274601]
    # Transforms the data from the weight and bias
    y = softmax(np.matmul(x_first, W_second) + b_second)

    return y[0]







def decide(probabilities):
    """
    Decide if the probability of winning is high enough to create a new order.
    :param probabilities: Floats representing the probability of winning for each currency
    :return: The amount to be invested. Zero means don't buy
    """
    maxIndex = 0
    for i in range(len(currencies)):
        if probabilities[i] > probabilities[maxIndex]:
            maxIndex = i

    if probabilities[maxIndex] >= 0.52:     # If probability is greater than 0.52 create order
        if currencies[maxIndex][3:] == "USD":
            investment = math.floor(leverage * 0.96 * getBalance() / getPrice(currencies[maxIndex])) - 1
        elif currencies[maxIndex][:3] == "USD":
            investment = math.floor(leverage * 0.96 * getBalance()) - 1
        else:
            investment = math.floor(leverage * 0.96 * getBalance() * getPrice(currencies[maxIndex])) - 1
    else:
        investment = 0

    return currencies[maxIndex], investment







def checkSpread(currency):
    """
    Check that the spread for a given currency is not out of control
    :param currency: The currency to check the spread of
    :return:
    """
    if (getSpread(currency) > (0.0003 * getPrice(currency))):
        doNotBuy = True







def execute(currency, amount):
    """
    Opens a new position and records the data surrounding the situation for back testing
    :param currency: Currency pair to buy
    :param amount: Amount to buy
    :return:
    """
    if amount > 1 and not doNotBuy:
        openPosition(amount, currency,
                     getPrice(currency) - (0.0001 * round(4.5 * getPrice(currency))) - (getSpread(currency) / 2),
                     getPrice(currency) + (0.0003 * round(4.5 * getPrice(currency))) + (getSpread(currency) / 2))

        # Records conditions surrounding the trade for debugging and analysis
        buyConditions[0] = currency
        buyConditions[1] = datetime.now(pytz.timezone('America/Chicago'))
        buyConditions[2] = getPrice(currency)
        row = getRow(currency)
        i = 3
        while i < 8:
            buyConditions[i] = row[i - 1]
            i += 1

        i = 8
        temp, row = getIndicatorRow(currency)
        while i < 20:
            buyConditions[i] = row[i - 8]
            i += 1

        buyConditions[20] = getBalance()
        buyConditions[21] = probabilities[currenciesIndex[currency]]
        write("Buy Conditions: " + str(buyConditions))
        write("Indicator row: " + str(row))







def zuluToCenteral(time, timezone):
    """
    Converts the time Digital ocean time zone to central time
    :param time: time to be converted
    :param timezone: The time timzone of the to be converted time
    :return:
    """
    time = datetime.strptime(str(time), "%Y-%m-%d %H:%M:%S")
    zuluTime = pytz.timezone(timezone)
    centeralTime = pytz.timezone("America/Chicago")

    # returns datetime in the new timezone
    return zuluTime.localize(time).astimezone(centeralTime)







def SMSsend(textString):
    """
    Sends a text to notify us of a crash or daily report using Twilio
    :param textString: The body of the text message
    :return:
    """
    if datetime.today().weekday() != 6:
        message = client.api.account.messages.create(to="+15072020637",
                                                     from_="+15076160276",
                                                     body="\n\nHello Timothy, \nYour daily report is ready!\n" +
                                                          textString + "\n\nYour loyal companion Zulu")

        message = client.api.account.messages.create(to="+15079932821",
                                                     from_="+15076160276",
                                                     body="\n\nGreetings Joshua, \nYour daily report is ready!\n" +
                                                          textString + "\n\nBest regards")
    else:
        message = client.api.account.messages.create(to="+15072020637",
                                                     from_="+15076160276",
                                                     body="\n\nHello Timothy, \nYour weekly report is ready!\n" +
                                                          textString + "\n\nYour loyal companion Zulu")

        message = client.api.account.messages.create(to="+15079932821",
                                                     from_="+15076160276",
                                                     body="\n\nGreetings Joshua, \nYour weekly report is ready!\n" +
                                                          textString + "\n\nBest regards")







def marketOpen():
    """
    Gets whether the market is currently open used to pause the program during the weekend
    :return: A boolean representing whether the market is open or not.
    """
    params = {"instruments": "EUR_USD"}
    r = pricing.PricingInfo(accountID=accountID, params=params)
    try:
        rv = api.request(r)
        r = r.response["prices"][0]["tradeable"]
        r = bool(r)
    except ConnectionError as e:
        print("Connection Exception in marketOpen()")
        write("Connection Exception in marketOpen()")
        print(e)
        write(e)
        r = False
    except:
        print("Unknown Error in marketOpen()")
        r = False

    return r








def write(text):
    """
    A method used to log the bots activity for debugging
    :param text: The message to be written to the log
    :return:
    """
    text_file = open(__version__ + "Output.txt", "a")
    text_file.write(str(text) + "\n\n")
    text_file.close()


if __name__ == '__main__':
    print("Running Practice: " + __version__)
    write("Running Practice: " + __version__)

    while True:
        try:
            # Runs this statement at 5:00 central time to send a text of the days activity
            if datetime.now().hour == 0 and datetime.now().minute == 0 and datetime.now().second == 0:
                try:
                    if datetime.today().weekday() != 6:

                        rows = exeSqlSelect('''SELECT * FROM Tyler3_0_TradeHistory
                                        WHERE TIMESELL >= datetime('now','-1 day')''')  # look at time
                    else:
                        rows = exeSqlSelect('''SELECT * FROM Tyler3_0_TradeHistory
                                        WHERE TIMESELL >= datetime('now','-7 day')''')  # look at time

                    initalBalance = rows[0][25]
                    finalBalance = rows[-1][24]
                    date = datetime.today().strftime('%Y-%m-%d')
                    goodTrades = 0
                    badTrades = 0
                    isInATrade = inTrade()
                    profit = finalBalance - initalBalance
                    profit = '{0:.2f}'.format(profit)
                    for row in rows:
                        if (row[25] < row[24]):
                            goodTrades += 1
                        else:
                            badTrades += 1
                    textString = "\n" + "Date:      " + str(date) + "\n" + "Version: " + str(
                        __version__) + "\n" + "Profit:                        $" + str(
                        profit) + "\n" + "Profitible Trades:       " + str(
                        goodTrades) + "\n" + "Nonprofitible trades: " + str(badTrades) + "\n" + "In Trade: " + str(
                        isInATrade)
                except:
                    date = datetime.today().strftime('%Y-%m-%d')
                    isInATrade = inTrade()
                    textString = "\n" + "Date:      " + str(date) + "\n" + "Version: " + str(
                        __version__) + "\n" + "In Trade: " + str(isInATrade) + "\n" + "No new Trades."

                SMSsend(textString)
                time.sleep(1)







            # Check if the bot has recently completed a trade to record the results
            if datetime.now().second % 30 == 15:
                if not inTrade() and oldTrade:
                    exeSqlInsert("INSERT INTO Tyler3_0_TradeHistory (PAIR, TIMEBUY, TIMESELL, PIPS, PIPFEE, SELL, "
                                 "BUYOPEN, BUYHIGH, BUYLOW, BUYCLOSE, VOLUME, RSI, D, ADX,  MACDmag, "
                                 "MACDdir, OBV, RSIprev, Dprev, ADXprev, MACDmagPrev, MACDdirprev, OBVprev, "
                                 "INITIALBALANCE, FINALBALANCE, CERTAINTY) VALUES ( " +
                                 "'" + str(buyConditions[0]) + "'" + ", " +
                                 "'" + str(buyConditions[1]) + "'" + ", " +
                                 "'" + str(datetime.now(pytz.timezone('America/Chicago'))) + "'" + ", " +
                                 str(10000 * (getPrice(buyConditions[0]) - buyConditions[2])) + ", " +
                                 str(10000 * (getPrice(buyConditions[0]) - buyConditions[2]) -
                                     getSpread(buyConditions[0])) + ", " +
                                 str(getPrice(buyConditions[0])) + ", " +
                                 str(buyConditions[3]) + ", " +
                                 str(buyConditions[4]) + ", " +
                                 str(buyConditions[5]) + ", " +
                                 str(buyConditions[6]) + ", " +
                                 str(buyConditions[7]) + ", " +
                                 str(buyConditions[8]) + ", " +
                                 str(buyConditions[9]) + ", " +
                                 str(buyConditions[10]) + ", " +
                                 str(buyConditions[11]) + ", " +
                                 str(buyConditions[12]) + ", " +
                                 str(buyConditions[13]) + ", " +
                                 str(buyConditions[14]) + ", " +
                                 str(buyConditions[15]) + ", " +
                                 str(buyConditions[16]) + ", " +
                                 str(buyConditions[17]) + ", " +
                                 str(buyConditions[18]) + ", " +
                                 str(buyConditions[19]) + ", " +
                                 str(buyConditions[20]) + ", " +
                                 str(getBalance()) + ", " +
                                 str(buyConditions[21]) +
                                 " )")

                oldTrade = inTrade()
                time.sleep(1.1)







            # Main logic that gets the current 15 min candle and calls methods to check the probability of winning
            if datetime.now().minute % 15 == 0 and datetime.now().second == 10:
                if marketOpen():
                    doNotBuy = False
                    for i in range(len(currencies)):
                        pid, row = getIndicatorRow(currencies[i])
                        checkRowPID(i, pid)
                        probabilities[i] = probabilityOfWinning(row)

                    print(str(datetime.now(pytz.timezone('America/Chicago'))) + " EURUSD, GBPUSD, AUDUSD, NZDUSD: " +
                          str(probabilities))
                    write(str(datetime.now(pytz.timezone('America/Chicago'))) + " EURUSD, GBPUSD, AUDUSD, NZDUSD: " +
                          str(probabilities))
                    currency, amount = decide(probabilities)
                    checkSpread(currency)
                    write("Currency: " + str(currency) + "  Amount: " + str(amount))
                    execute(currency, amount)

                time.sleep(1.1)

        except Exception as e:
            tb = sys.exc_info()[2]
            write("Exception at " + str(datetime.now(pytz.timezone('America/Chicago'))))
            write("Failed at Line %i \n" % tb.tb_lineno)
            write("Error: {}".format(str(e)))

            print("Exception at " + str(datetime.now(pytz.timezone('America/Chicago'))))
            print("Failed at Line %i \n" % tb.tb_lineno)
            print("Error: {}".format(str(e)))
            if not sentError:
                SMSsend("Program Crashed" + str(datetime.now(pytz.timezone('America/Chicago'))))
                sentError = True


        time.sleep(0.3)

