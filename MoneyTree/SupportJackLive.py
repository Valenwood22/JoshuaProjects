__author__ = "Timothy Alexander, Joshua Gisi"
__copyright__ = "Copyright 2018, Project Money Tree"
__version__ = "SupportJack1.2Alpha"
__email__ = "TJEnterprises2019@gmail.com"
__status__ = "pre-Alpha"
__DataBaseFilePath__ = "/root/Tyler+Jack/Database/currenciesDB"  # "Database/currenciesDB"

# <editor-fold desc="Imports">
import time
import datetime
from datetime import timedelta
from datetime import datetime
import pytz
import sqlite3

import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.instruments as instruments
from oandapyV20 import API
# </editor-fold>


#<editor-fold desc="Credentials">
accountID = "xxx-xxx-xxxxxxx-xxx"
api = API(access_token="xxxxxxxxxxxxxxxxxxxxxxxx", environment="live", headers=None)
#</editor-fold>

currencies = ["AUDCAD", "EURCHF", "EURGBP", "NZDCAD", "USDCAD", "USDCHF", "NZDUSD", "EURUSD", "GBPUSD", "AUDUSD" ]


def exeSqlSelect(command):
    # Create a database if not exists and get a connection to it
    connection = sqlite3.connect(__DataBaseFilePath__)
    # Get a cursor to execute sql statements
    cursor = connection.cursor()
    cursor.execute(command)
    rows = cursor.fetchall()
    connection.close()
    return rows


def exeSqlInsert(command):
    write(command)
    # Create a database if not exists and get a connection to it

    connection = sqlite3.connect(__DataBaseFilePath__)
    # Get a cursor to execute sql statements
    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()
    connection.close()


def write(text):
    text_file = open(__version__+"Output.txt", "a")
    text_file.write(str(text) + "\n\n\n")
    text_file.close()


def getCandleStick(currency):
    pair = currency[:3] + "_" + currency[3:]
    client = api
    paramsV = {"count": 2, "granularity": "M15"}
    v = instruments.InstrumentsCandles(instrument=pair, params=paramsV)
    client.request(v)

    candle = v.response['candles']
    candle = (sorted(candle, key=lambda i: i['time']))
    index = 0

    # Format Time
    candleTimeTemp = candle[0]['time'].replace("T", " ")
    candleTimeTemp = candleTimeTemp.split(".")[0]

    nowMinus15 = datetime.now() + timedelta(minutes=-15)
    nowMinus15 = str(nowMinus15)
    nowMinus15 = nowMinus15.split(".")[0]

    if int(candleTimeTemp[14:-3]) != int(nowMinus15[14:-3]):
        index+=1

    candleTime = candle[index]['time'].replace("T", " ")
    candleTime = candleTime.split(".")[0]
    candleTime = zuluToCenteral(candleTime, "Zulu")

    print(str(candle[index]) + "  ::  " + str(candleTime))
    write("\n\nCandles Retrieved: " + str(candle))
    return candle[index], '"' + str(candleTime) + '"'


def zuluToCenteral(time, timezone):
    time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    zuluTime = pytz.timezone(timezone)
    centeralTime = pytz.timezone("America/Chicago")

    # returns datetime in the new timezone
    return zuluTime.localize(time).astimezone(centeralTime)


def flowGate():
    if (datetime.now().minute % 15 == 0 and datetime.now().second >= 5):
        return True
    else:
        return False


def marketOpen():
    params = {"instruments": "EUR_USD"}
    r = pricing.PricingInfo(accountID=accountID, params=params)
    try:
        rv = api.request(r)
        r = r.response["prices"][0]["tradeable"]
        r = bool(r)
    except ConnectionError as e:
        write("\n\nConnection Exception")
        write(e)
        r = True
    except:
        write("\n\nUnknown Error")
        r = True

    return r


def getRSImod(currency):
    temp = exeSqlSelect("SELECT close FROM " + str(currency) + "_Candles ORDER BY PID desc limit 100")

    prices = []

    for i in range(len(temp)):
        prices.append(temp[-1 - i][0])

    # RSI edited i+1=len(prices)
    RSI = []
    currGain = 0
    currLoss = 0
    avgGain = 0
    avgLoss = 0

    for i in range(len(prices)):

        if (i < 14):
            RSI.append(50)

        if (i == 14):
            avgGain = 0
            avgLoss = 0

            j = 0
            while (j < 14):
                if ((prices[j + 1] - prices[j]) > 0):
                    avgGain += (prices[j + 1] - prices[j])
                else:
                    avgLoss += (prices[j] - prices[j + 1])
                j += 1

            avgGain = avgGain / 14
            avgLoss = avgLoss / 14
            RS = avgGain / avgLoss
            RSI.append(100 - (100 / (1 + RS)))

        if i > 14:
            if (prices[i] - prices[i - 1]) > 0:
                currGain = (prices[i] - prices[i - 1])
            else:
                currLoss = (prices[i - 1] - prices[i])
            avgGain = (avgGain * 13 + currGain) / 14
            avgLoss = (avgLoss * 13 + currLoss) / 14
            RS = avgGain / avgLoss
            RSI.append(100 - (100 / (1 + RS)))

    return RSI[len(RSI) - 1]


def getD(currency):
    temp = exeSqlSelect("SELECT high, low, close FROM " + str(currency) + "_Candles ORDER BY PID desc limit 100")

    highs = []
    lows = []
    prices = []

    for i in range(len(temp)):
        highs.append(temp[-1 - i][0])

    for i in range(len(temp)):
        lows.append(temp[-1 - i][1])

    for i in range(len(temp)):
        prices.append(temp[-1 - i][2])

    # stochastic i + 1 = len(prices)
    D = []
    K = []
    for i in range(len(prices)):
        high = 0
        low = 2
        if i > 14:
            j = 1
            while j < (14 + 1):
                if lows[i + 1 - j] < low:
                    low = lows[i + 1 - j]
                if highs[i + 1 - j] > high:
                    high = highs[i + 1 - j]

                j += 1
            if (high - low) == 0:
                K.append(50)
            else:
                K.append(100 * (prices[i] - low) / (high - low))
        else:
            K.append(50)

        if i < 2:
            D.append(K[i])
        else:
            D.append((K[i] + K[i - 1] + K[i - 2]) / 3)

    return D[len(D) - 1]


def getADXmod(currency):
    temp = exeSqlSelect("SELECT high, low, close FROM " + str(currency) + "_Candles ORDER BY PID desc limit 100")

    highs = []
    lows = []
    prices = []

    for i in range(len(temp)):
        highs.append(temp[-1 - i][0])

    for i in range(len(temp)):
        lows.append(temp[-1 - i][1])

    for i in range(len(temp)):
        prices.append(temp[-1 - i][2])

        # ADX

    UpMove = 0
    DownMove = 0

    PosDM = 0
    NegDM = 0

    PosDMs = []
    NegDMs = []

    PosDMs_int = []
    NegDMs_int = []

    TR = []
    ATR = []

    PosDI = []
    NegDI = []

    ADX = []
    for i in range(len(prices)):
        UpMove = highs[i] - highs[i - 1]
        DownMove = lows[i - 1] - lows[i]

        if (UpMove > DownMove and UpMove > 0):
            PosDM = UpMove
        else:
            PosDM = 0

        if (DownMove > UpMove and DownMove > 0):
            NegDM = DownMove
        else:
            NegDM = 0

        PosDMs_int.append(PosDM)
        NegDMs_int.append(NegDM)

        if (i < 14):
            PosDMs.append(PosDM)
            NegDMs.append(NegDM)

        if (i == 14):
            total = 0
            j = 1
            while (j < 15):
                total += PosDMs_int[len(PosDMs_int) - j]
                j += 1
            PosDMs.append(total / 14)

            total = 0
            j = 1
            while (j < 15):
                total += NegDMs_int[len(NegDMs_int) - j]
                j += 1
            NegDMs.append(total / 14)

        if (i > 14):
            PosDMs.append((13 * PosDMs[len(PosDMs) - 1] + PosDMs_int[len(PosDMs_int) - 1]) / 14)
            NegDMs.append((13 * NegDMs[len(NegDMs) - 1] + NegDMs_int[len(NegDMs_int) - 1]) / 14)

        if (i > 0):
            TR.append(max((highs[i] - lows[i]), (highs[i] - prices[i]),
                          (prices[i] - lows[i])))
        else:
            TR.append(0)

        if (i < 14):
            ATR.append(0.01)
        if (i == 14):
            total = 0
            j = 1
            while (j < 15):
                total += TR[i + 1 - j]
                j += 1
            ATR.append(total / 14)
        if (i > 14):
            ATR.append((ATR[len(ATR) - 1] * 13 + TR[len(TR) - 1]) / 14)

        if (i < 14):
            PosDI.append(PosDMs[len(PosDMs) - 1] / ATR[len(ATR) - 1])
            NegDI.append(NegDMs[len(NegDMs) - 1] / ATR[len(ATR) - 1])

        if (i == 14):
            total = 0
            j = 1
            while (j < 15):
                total += NegDMs[len(NegDMs) - j] / ATR[len(ATR) - j]
                j += 1
                NegDI.append(total / 14)

            total = 0
            j = 1
            while (j < 15):
                total += NegDMs[len(NegDMs) - j] / ATR[len(ATR) - j]
                j += 1
                NegDI.append(total / 14)

        if (i > 14):
            PosDI.append(
                ((PosDMs[len(PosDMs) - 1] / ATR[len(ATR) - 1]) - PosDI[len(PosDI) - 1]) * (2 / 15) + PosDI[
                    len(PosDI) - 1])
            NegDI.append(
                ((NegDMs[len(NegDMs) - 1] / ATR[len(ATR) - 1]) - NegDI[len(NegDI) - 1]) * (2 / 15) + NegDI[
                    len(NegDI) - 1])

        if (i > 14):
            ADX.append(
                100 * abs(
                    (PosDI[len(PosDI) - 1] - NegDI[len(NegDI) - 1]) / (PosDI[len(PosDI) - 1] + NegDI[len(NegDI) - 1])))
        else:
            ADX.append(10)

    return ADX[len(ADX) - 1]


def getMACD(currency):
    temp = exeSqlSelect("SELECT close FROM " + str(currency) + "_Candles ORDER BY PID desc limit 100")

    prices = []
    for i in range(len(temp)):
        prices.append(temp[-1 - i][0])

    # MACD i + 1 = len(prices)
    long = []
    short = []
    signal = []
    MACD = []
    MACD_diff = []
    MACD_mag = []
    MACD_dir = []

    for i in range(len(prices)):
        if (i < 26):
            short.append(prices[i])
            long.append(prices[i])
            signal.append(prices[i])

        if (i == 26):
            total = 0
            j = 1
            while (j < 13):
                total += prices[i + 1 - j]
                j += 1
            short.append(total / 12)

            total = 0
            j = 1
            while (j < 27):
                total += prices[i + 1 - j]
                j += 1
            long.append(total / 26)

            total = 0
            j = 1
            while (j < 9):
                total += MACD[len(MACD) - j]
                j += 1
            signal.append(total / 9)

        if (i > 26):
            short.append((prices[i] - short[len(short) - 1]) * (2 / 13) + short[len(short) - 1])
            long.append((prices[i] - long[len(long) - 1]) * (2 / 27) + long[len(long) - 1])
            MACD.append(short[len(short) - 1] - long[len(long) - 1])

            signal.append((signal[len(signal) - 1] - MACD[len(MACD) - 1]) * (2 / 10) + MACD[len(MACD) - 1])
            MACD_diff.append(MACD[len(MACD) - 1] - signal[len(signal) - 1])

        else:
            MACD.append(short[len(short) - 1] - long[len(long) - 1])
            MACD_diff.append(0)

        # Split MACD into magnitude and direction
        MACD_mag.append(abs(MACD_diff[len(MACD_diff) - 1]))
        if (MACD_diff[len(MACD_diff) - 1] > 0):
            MACD_dir.append(1)
        elif (MACD_diff[len(MACD_diff) - 1] < 0):
            MACD_dir.append(-1)
        else:
            MACD_dir.append(0)
    return MACD_mag[len(MACD_mag) - 1], MACD_dir[len(MACD_dir) - 1]


def getOBV(currency):
    temp = exeSqlSelect("SELECT close, volume FROM " + str(currency) + "_Candles ORDER BY PID desc limit 100")

    prices = []
    for i in range(len(temp)):
        prices.append(temp[-1 - i][0])

    volume = []
    for i in range(len(temp)):
        volume.append(temp[-1 - i][1])

    # On-balance volume indicator
    obv = 0
    OBV = []
    OBV_mov = []
    OBV_pred = []
    for i in range(len(prices)):
        if (i > 0):
            if ((prices[i] - prices[i - 1]) > 0):
                obv += volume[i]
            if ((prices[i] - prices[i - 1]) < 0):
                obv -= volume[i]

        OBV.append(obv)

        if (i < 14):
            OBV_mov.append(OBV[len(OBV) - 1])

        if (i == 14):
            total = 0
            j = 1
            while (j < 15):
                total += OBV[len(OBV) - j]
                j += 1
            OBV_mov.append(total / 14)

        if (i > 14):
            OBV_mov.append((OBV[len(OBV) - 1] - OBV_mov[len(OBV_mov) - 1]) * (2 / 15) + OBV_mov[len(OBV_mov) - 1])

        if (OBV[len(OBV) - 1] > OBV_mov[len(OBV_mov) - 1]):
            OBV_pred.append(1)
        else:
            OBV_pred.append(-1)
    return OBV_pred[len(OBV_pred) - 1]


if __name__ == '__main__':
    write("\n\nRunning: " + __version__)
    print("\n\nRunning*** " + __version__)
    while (True):
        try:
            if (marketOpen()):
                if (flowGate()):

                    for i in range(len(currencies)):
                        candle, candleTime = getCandleStick(currencies[i])

                        write("\n\n" + str(datetime.now()))

                        exeSqlInsert("INSERT INTO " + str(currencies[i]) + "_Candles "
                                                                           "(TIME, OPEN, HIGH, LOW, CLOSE, VOLUME) "
                                                                           "VALUES ( " + str(candleTime) + ", " +
                                     str(candle['mid']['o']) + ", " +
                                     str(candle['mid']['h']) + ", " +
                                     str(candle['mid']['l']) + ", " +
                                     str(candle['mid']['c']) + ", " +
                                     str(candle['volume']) + " )")


                        mag, dir = getMACD(currencies[i])
                        exeSqlInsert("INSERT INTO " + str(currencies[i]) + "_Indicators "
                                                                           "(TIME, RSI, D, ADX, MACDmag, MACDdir, OBV) "
                                                                           "VALUES ( " + str(candleTime) + ", " +
                                     str(getRSImod(currencies[i])) + ", " +
                                     str(getD(currencies[i])) + ", " +
                                     str(getADXmod(currencies[i])) + ", " +
                                     str(mag) + ", " +
                                     str(dir) + ", " +
                                     str(getOBV(currencies[i])) +
                                     " )")


                    time.sleep(870)

                else:
                    time.sleep(1)
            else:
                time.sleep(600)
        except:
            print("Exception!!!!")

