__authors__ = "Timothy Alexander, Joshua Gisi"
__copyright__ = "Copyright 2019, Project Money Tree"
__version__ = "1.0.0"
__email__ = "TJEnterprises2019@gmail.com"
__status__ = "Development"

import operator
import datetime
from math import floor
from Support.candleStickExt import candleExt
from Support import Companion


class Val:

    def makePredictions(self, dataset_M15_init, dataset_M1_Close, startDate, endDate, timeScales = [3, 7, 14, 30], datapointsSearched = 2000, sampleSize = 100, candleSize = 15, stepSize = 5):

        def findIndex(dataset, time):
            i = floor(len(dataset) / 2)
            lowerBound = 0
            upperBound = len(dataset)
            while (datetime.datetime.strptime(dataset[i].datetime,
                                              '%Y-%m-%d %H:%M:%S') != datetime.datetime.strptime(time,
                                                                                                 '%Y-%m-%d %H:%M:%S')):
                if (datetime.datetime.strptime(dataset[i].datetime,
                                               '%Y-%m-%d %H:%M:%S') > datetime.datetime.strptime(time,
                                                                                                 '%Y-%m-%d %H:%M:%S')):
                    upperBound = i
                elif (datetime.datetime.strptime(dataset[i].datetime,
                                                 '%Y-%m-%d %H:%M:%S') < datetime.datetime.strptime(time,
                                                                                                   '%Y-%m-%d %H:%M:%S')):
                    lowerBound = i
                i = floor((upperBound + lowerBound) / 2)

            return (i)

        def outcome(time, s):
            nStart = findIndex(dataset_M1_Close, time) + candleSize
            if ((nStart + (s * candleSize) + 1) < len(dataset_M1_Close)):
                posCandles = 0
                allCandles = 0
                j = nStart
                while (j < nStart + (s * candleSize)):
                    tempDiff = float(dataset_M1_Close[j + stepSize].close) - float(dataset_M1_Close[j].close)
                    allCandles += abs(tempDiff)
                    if (tempDiff > 0):
                        posCandles += tempDiff

                    j += stepSize

                return posCandles / allCandles if allCandles != 0 else 0.5

            else:
                return (0.5)

        dataset_M15 = []
        for c in dataset_M15_init:
            dataset_M15.append(candleExt(c, None, None, None))
        del (dataset_M15_init)

        #write("Loaded Database")


        # <editor-fold desc="Backtest algorithm">
        for i in range(0, len(dataset_M15)):
            if (datetime.datetime.strptime(dataset_M15[i].candle.datetime,
                                           '%Y-%m-%d %H:%M:%S') <= startDate or datetime.datetime.strptime(
                    dataset_M15[i].candle.datetime, '%Y-%m-%d %H:%M:%S') >= endDate):
                continue

            candles_past = dataset_M15[i - datapointsSearched:i]
            currentCandle = dataset_M15[i]
            print(currentCandle.candle.datetime, i)

            scalingFactor = currentCandle.calculateScalingFactor(candles_past)

            for candle in dataset_M15:
                candle.marker = 0
                candle.cost = 0

            # <editor-fold desc="Calculate costs and markers">
            for candle in candles_past:
                candle.calculateCost(currentCandle, scalingFactor)

            candles_past.sort(key=operator.attrgetter('cost'))
            candles_past.reverse()
            count = 0
            for j in range(len(candles_past)):
                candles_past[j].marker = 1
                count += 1
                for k in range(0, j):
                    if (abs(candles_past[j].candle.pid - candles_past[k].candle.pid) <= 8 * candleSize and candles_past[
                        j].marker == 1):
                        candles_past[j].marker = 0
                        count -= 1
                        break
                if count == sampleSize: break
            # </editor-fold

            # <editor-fold desc="Make/Store Predictions">
            predictions = {}
            actuals = {}
            for scale in timeScales:
                predictions[scale] = 0
                actuals[scale] = 0

            for scale in timeScales:
                for candle in candles_past:
                    if (candle.marker == 1):
                        predictions[scale] += outcome(candle.candle.datetime, scale)
                predictions[scale] /= sampleSize
                actuals[scale] = outcome(currentCandle.candle.datetime, scale)

            currentCandle.predictions = predictions

            # </editor-fold

        # </editor-fold

        return(dataset_M15)



    def debugDecision(self, dataset_M15_init, dataset_M1_Close, time, timeScales = [3, 7, 14, 30], datapointsSearched = 2000, sampleSize = 100, candleSize = 15, stepSize = 5):
        if(type(time) == datetime.datetime): time = time.strftime('%Y-%m-%d %H:%M:%S')

        def findIndex(dataset, time):
            i = floor(len(dataset) / 2)
            lowerBound = 0
            upperBound = len(dataset)
            while (datetime.datetime.strptime(dataset[i].datetime,
                                              '%Y-%m-%d %H:%M:%S') != datetime.datetime.strptime(time,
                                                                                                 '%Y-%m-%d %H:%M:%S')):
                if (datetime.datetime.strptime(dataset[i].datetime,
                                               '%Y-%m-%d %H:%M:%S') > datetime.datetime.strptime(time,
                                                                                                 '%Y-%m-%d %H:%M:%S')):
                    upperBound = i
                elif (datetime.datetime.strptime(dataset[i].datetime,
                                                 '%Y-%m-%d %H:%M:%S') < datetime.datetime.strptime(time,
                                                                                                   '%Y-%m-%d %H:%M:%S')):
                    lowerBound = i
                i = floor((upperBound + lowerBound) / 2)

            return (i)

        def outcome(time, s):
            nStart = findIndex(dataset_M1_Close, time) + candleSize
            if ((nStart + (s * candleSize) + 1) < len(dataset_M1_Close)):
                posCandles = 0
                allCandles = 0
                j = nStart
                while (j < nStart + (s * candleSize)):
                    tempDiff = float(dataset_M1_Close[j + stepSize].close) - float(dataset_M1_Close[j].close)
                    allCandles += abs(tempDiff)
                    if (tempDiff > 0):
                        posCandles += tempDiff

                    j += stepSize

                return posCandles / allCandles if allCandles != 0 else 0.5

            else:
                return (0.5)

        dataset_M15 = []
        for c in dataset_M15_init:
            dataset_M15.append(candleExt(c, None, None, None))

        #write("Loaded Database")



        # <editor-fold desc="Backtest algorithm">
        i = findIndex(dataset_M15_init, time)

        timeList = []

        candles_past = dataset_M15[i - datapointsSearched:i]
        currentCandle = dataset_M15[i]

        scalingFactor = currentCandle.calculateScalingFactor(candles_past)

        for candle in dataset_M15:
            candle.marker = 0
            candle.cost = 0

        # <editor-fold desc="Calculate costs and markers">
        for candle in candles_past:
            candle.calculateCost(currentCandle, scalingFactor)

        candles_past.sort(key=operator.attrgetter('cost'))
        candles_past.reverse()
        count = 0
        for j in range(len(candles_past)):
            candles_past[j].marker = 1
            count += 1
            for k in range(0, j):
                if (abs(candles_past[j].candle.pid - candles_past[k].candle.pid) <= 8 * candleSize and candles_past[
                    j].marker == 1):
                    candles_past[j].marker = 0
                    count -= 1
                    break
            if count == sampleSize: break
        # </editor-fold

        # <editor-fold desc="Make/Store Predictions">
        predictions = {}
        actuals = {}
        for scale in timeScales:
            predictions[scale] = 0
            actuals[scale] = 0

        for scale in timeScales:
            for candle in candles_past:
                if (candle.marker == 1):
                    predictions[scale] += outcome(candle.candle.datetime, scale)
                    timeList.append(candle.candle.datetime)
            predictions[scale] /= sampleSize
            actuals[scale] = outcome(currentCandle.candle.datetime, scale)

        # </editor-fold


        return(predictions, timeList)


if __name__ == '__main__':
    filePath = "C:/Python/Python36/BackTestData.db"
    startDate = datetime.datetime(2009, 1, 6, 1, 0, 0)
    endDate = datetime.datetime(2009, 1, 8, 1, 0, 0)

    loadCandlesFrom = startDate - datetime.timedelta(days=42)
    loadCandlesUntil = endDate + datetime.timedelta(days=14)
    numberOfRawData = 7
    numberOfExtraColumns = 0

    Data = Companion.sqlCompanion(filePath)  # File path on ALEXANDERT
    # Data = Companion.sqlCompanion("C:\\Users\\Administrator\\Desktop\\BackTestData.db")  # File path on GISIJ Laptop

    dataset_M15_init = Data.getDataByDatetime("EUR_USD", printReturn=False, granularity='M15',
                                              startDatetime=loadCandlesFrom,
                                              endDatetime=loadCandlesUntil, indicators=['TRIX(14)', 'CMV(14)'])
    dataset_M1_Close = Data.getDataByDatetime("EUR_USD", printReturn=False, granularity='M1',
                                              startDatetime=loadCandlesFrom,
                                              endDatetime=loadCandlesUntil)
    print("Loaded database")
    predictor = Val()
    dataset_M15 = predictor.makePredictions(dataset_M15_init, dataset_M1_Close, startDate, endDate)
    print("Finished predictions")
    for i in range(len(dataset_M15)):
        if(dataset_M15[i].predictions != None):
            print(dataset_M15[i])


    predictions, timeList = predictor.debugDecision(dataset_M15_init, dataset_M1_Close, datetime.datetime(2009, 1, 7, 23, 42, 0))
    print("Predictions: ", predictions)
    print("Time List: ", timeList)

    print("Done")

