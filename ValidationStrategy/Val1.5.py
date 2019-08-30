
__author__ = "Timothy Alexander, Joshua Gisi"
__copyright__ = "Copyright 2019, Project Money Tree"
__version__ = "ValExperimenting1.5"
__email__ = "TJEnterprises2019@gmail.com"
__status__ = "Demo"
__description__ = "This is the program that evaluates the performance of potential indicators" \
                  "Time Intervals are fixed instead of TP and SL being fixed" \
                  "From Database with Companion"



# <editor-fold desc="Imports">
from random import *
from math import floor
import pandas as pd
import ta
import Companion
# </editor-fold



flag = True



# TODO: Transfer globals to a config.ini
allIndicators = ['RSI', 'TRIX', 'VORTEX', 'CCI', 'DPO', '%R', 'ATR', 'MFI', 'STDEV', '2CANDLEVOLUME', 'VOLMADIF']
trendIndicators = ('RSI', 'TRIX', 'VORTEX', 'CCI', 'DPO', '%R')
momentumIndicators = ('ATR', 'MFI', 'STDEV')
volumeIndicators = ('VOLMADIF', '2CANDLEVOLUME')
chosenIndicators = set(allIndicators)
defaultSets = [('ATR', 'TRIX', 'VOLMADIF'), ('ATR', 'VORTEX', 'VOLMADIF'), ('ATR', 'CCI', 'VOLMADIF'),
               ('STDEV', 'TRIX', 'VOLMADIF'), ('STDEV', 'VORTEX', 'VOLMADIF'), ('STDEV', 'CCI', 'VOLMADIF')]
testIndicators = ['%R', '2CANDLEVOLUME']
testedSets = {}

loadCandlesFrom = '2009-10-21 19:00:00'
loadCandlesUntil = '2011-02-21 19:00:00'
startDate = '2010-10-21 19:00:00'
endDate = '2011-01-02 12:30:00'

sampleSize = 100
datapointsSearched = 20000
pipScaling = 5000
candleSize = 15
stepSize = 1

numberOfRawData = 7
numberOfExtraColumns = 3







def outcome(nStart, t):
    """
    Find if the trade was a winning or losing trade
    :param nStart: The time the order was created
    :param t: the time frame ie. for t=7 wait 7 candles
    :return: whether it won or lost the trade
    """
    j = nStart
    if len(dataset_null) > (j + (t * candleSize) + 1):
        posCandles = 0
        allCandles = 0
        while j < nStart + (t * candleSize):
            tempDiff = float(dataset_null[j + stepSize][3]) - float(dataset_null[j][3])
            allCandles += abs(tempDiff)
            if tempDiff > 0:
                posCandles += tempDiff

            j += stepSize
        if allCandles != 0:
            return posCandles / allCandles
        else:
            return 0.5
    else:
        return 0.5







def findIndex(time):
    """
    Find the index for the given time
    :param time: The datetime of the index
    :return: index
    """
    i = floor(len(dataset_M1_Close) / 2)
    while dataset_M1_Close[i][1] != time:
        if dataset_M1_Close[i][1] > time:
            i = floor(i / 2)
        elif dataset_M1_Close[i][1] < time:
            i = floor((len(dataset_M1_Close) + i) / 2)

    return i







def cost(conditionOne, conditionTwo, avgDiffArray):
    """
    Calculates the similarity of a situation
    :param conditionOne: Current indicator value
    :param conditionTwo: Historic indicator value
    :param avgDiffArray: Scale factor
    :return:
    """
    c = 0
    for i in range(1, numberOfFeatures + 1):
        temp = (conditionOne[i] - conditionTwo[i]) / (avgDiffArray[i])
        c += (temp * temp)
    if c != 0:
        return 1 / c
    else:
        return (0)







def choose_indicators(chosenIndicators):
    """
    Finds all combinations of a given list of indicators
    :param chosenIndicators: A list of indicators to be tested
    :return:
    """
    if len(chosenIndicators) == 0:

        if {testIndicators[0]}.intersection(trendIndicators) != set([]):
            return (defaultSets[0].intersection(momentumIndicators.union(volumeIndicators)).union(
                {testIndicators[0]}))

        elif {testIndicators[0]}.intersection(momentumIndicators) != set([]):
            return (defaultSets[0].intersection(trendIndicators.union(volumeIndicators)).union(
                {testIndicators[0]}))


        elif {testIndicators[0]}.intersection(volumeIndicators) != set([]):
            return (defaultSets[0].intersection(trendIndicators.union(momentumIndicators)).union(
                {testIndicators[0]}))

    for i in range(0, len(defaultSets) - 1):

        if 2 == len(defaultSets[i].intersection(chosenIndicators)):
            if chosenIndicators.intersection(set(testIndicators)).intersection(trendIndicators) != set([]):
                nextSet = defaultSets[i + 1].intersection(momentumIndicators.union(volumeIndicators)).union(
                    chosenIndicators.intersection(set(testIndicators)))

            elif set([]) != chosenIndicators.intersection(set(testIndicators)).intersection(momentumIndicators):
                nextSet = defaultSets[i + 1].intersection(trendIndicators.union(volumeIndicators)).union(
                    chosenIndicators.intersection(set(testIndicators)))

            elif chosenIndicators.intersection(set(testIndicators)).intersection(volumeIndicators) != set([]):
                nextSet = defaultSets[i + 1].intersection(trendIndicators.union(momentumIndicators)).union(
                    chosenIndicators.intersection(set(testIndicators)))

            if not tuple(nextSet) in testedSets:
                return nextSet

    if len(defaultSets[-1].intersection(chosenIndicators)) == 2:
        for i in range(len(testIndicators) - 1):
            if {testIndicators[i]} == chosenIndicators.intersection(set(testIndicators)):

                if {testIndicators[i + 1]}.intersection(trendIndicators) != set([]):
                    nextSet = defaultSets[0].intersection(momentumIndicators.union(volumeIndicators)).union(
                        {testIndicators[i + 1]})

                elif {testIndicators[i + 1]}.intersection(momentumIndicators) != set([]):
                    nextSet = defaultSets[0].intersection(trendIndicators.union(volumeIndicators)).union(
                        {testIndicators[i + 1]})


                elif set([]) != set([testIndicators[i + 1]]).intersection(volumeIndicators):
                    nextSet = defaultSets[0].intersection(trendIndicators.union(momentumIndicators)).union(
                        set([testIndicators[i + 1]]))

                if not tuple(nextSet) in testedSets:
                    return nextSet

    return set(())


def write(text):
    print(text)
    text_file = open(__version__ + "Output.txt", "a")
    text_file.write(str(text) + "\n\n")
    text_file.close()


if __name__ == '__main__':

    # <editor-fold desc="Load dataset">

    Data = Companion.Companion("C:\\Python\\Python36\\BackTestData.db")

    dataset_M15 = Data.getDataByDatetime("EUR_USD", printReturn=False, granularity='M15', startDatetime=loadCandlesFrom,
                                         endDatetime=loadCandlesUntil,
                                         columns=['PID', 'DATETIME', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME'])
    dataset_M1_Close = Data.getDataByDatetime("EUR_USD", printReturn=False, granularity='M1',
                                              startDatetime=loadCandlesFrom,
                                              endDatetime=loadCandlesUntil, columns=['PID', 'DATETIME', 'CLOSE'])

    print(dataset_M15[:10])
    print(dataset_M1_Close[:100])

    print("Loaded Database")
    # </editor-fold

    while flag:

        # <editor-fold desc="Reset Variables">
        features_all = []
        actual_all = []
        pred_all = []
        cost_all = []
        # </editor-fold

        # <editor-fold desc="Calculate Indicators">
        chosenIndicators = choose_indicators(chosenIndicators)
        dataset = pd.DataFrame(dataset_M15)
        dataset.columns = ['Pid', 'Datetime', 'Open', 'High', 'Low', 'Close', 'Volume']

        # Direction / Trend
        if 'RSI' in chosenIndicators:
            dataset['RSI'] = ta.momentum.rsi(dataset['Close'], n=14, fillna=False)
        if 'TRIX' in chosenIndicators:
            dataset['TRIX'] = ta.trend.trix(dataset['Close'], n=15, fillna=False)
        if 'TRIXDER' in chosenIndicators:
            dataset['TRIXDER'] = dataset['TRIX'] - dataset['TRIX'].rolling(3).mean()

        if 'VORTEX' in chosenIndicators:
            dataset['VORTEX'] = ta.trend.vortex_indicator_neg(dataset['High'], dataset['Low'], dataset['Close'], n=14,
                                                              fillna=False)
        if 'CCI' in chosenIndicators:
            dataset['CCI'] = ta.trend.cci(dataset['High'], dataset['Low'], dataset['Close'], n=20, c=0.015,
                                          fillna=False)
        if 'DPO' in chosenIndicators:
            dataset['DPO'] = ta.trend.dpo(dataset['Close'], n=20, fillna=False)
        if '%R' in chosenIndicators:
            dataset['%R'] = ta.momentum.wr(dataset['High'], dataset['Low'], dataset['Close'], lbp=14, fillna=False)

        # Momentum
        if 'ADX' in chosenIndicators:
            dataset['ADX'] = ta.trend.adx(dataset['High'], dataset['Low'], dataset['Close'], n=14, fillna=True)
        if 'ATR' in chosenIndicators:
            dataset['ATR'] = ta.volatility.average_true_range(dataset['High'], dataset['Low'], dataset['Close'], n=14,
                                                              fillna=False)
        if 'MFI' in chosenIndicators:
            dataset['MFI'] = ta.momentum.money_flow_index(dataset['High'], dataset['Low'], dataset['Close'],
                                                          dataset['Volume'], n=14, fillna=False)
        if 'STDEV' in chosenIndicators:
            dataset['STDEV'] = dataset['Close'].rolling(20).std()

        # Volume
        if '2CANDLEVOLUME' in chosenIndicators:
            dataset['2CANDLEVOLUME'] = (dataset['Volume'] + dataset['Volume'].shift(1))

        if 'VOLMADIF' in chosenIndicators:
            dataset['VOLMADIF'] = dataset['Volume'].rolling(2).mean() - dataset['Volume'].rolling(7).mean()

        dataset = dataset.dropna()
        data = dataset.values
        numberOfFeatures = len(data[0]) - numberOfRawData - numberOfExtraColumns
        # </editor-fold

        print("First line of dataset: ", dataset_M15[0])
        # <editor-fold desc="Backtest algorithm">
        i = 0
        while i < len(dataset_M15):
            if dataset_M15[i][1] <= startDate or dataset_M15[i][1] >= endDate:
                continue
            print("Here")

            features_past = data[i - datapointsSearched:i]
            currentFeature = data[i]

            # <editor-fold desc="Calculate Costs">
            if len(chosenIndicators) != 0:
                avgDiffArray = [0] * len(currentFeature)
                k = 0
                while k < len(features_past):
                    for j in range(1, numberOfFeatures + 1):
                        avgDiffArray[j] += abs(currentFeature[j] - features_past[k][j])
                    k += 10

                for j in range(len(currentFeature)):
                    avgDiffArray[j] /= (len(features_past) / 10)

                costsPast = []
                for feature in features_past:
                    costsPast.append(cost(currentFeature, feature, avgDiffArray))
            else:
                costsPast = []
                for feature in features_past:
                    costsPast.append(random())

            # </editor-fold

            # <editor-fold desc="Calculate Cost Markers">
            costsPastSorted = sorted(costsPast)
            costMarkers = [0] * len(costsPast)
            cutoffIndex = sampleSize

            while sum(costMarkers) != sampleSize:
                if sum(costMarkers) < sampleSize:
                    cutoffIndex += 10
                    cutoff = costsPastSorted[-cutoffIndex]
                    for p in range(len(features_past)):
                        if (costsPast[p] >= cutoff > costsPast[
                                                    p - 2] > p >= 8 and
                                costsPast[p - 3] < cutoff and costsPast[p - 4] < cutoff and costsPast[
                                    p - 5] < cutoff and
                                costsPast[p - 6] < cutoff and costsPast[p - 7] < cutoff and costsPast[p - 8] < cutoff):
                            if cutoff > costsPast[p - 1]:
                                costMarkers[p] = 1
                            elif costsPast[p - 1] < costsPast[p]:
                                costMarkers[p - 1] = 0
                                costMarkers[p] = 1
                            else:
                                costMarkers[p] = 0

                        else:
                            costMarkers[p] = 0

                else:
                    cutoffIndex -= 1
                    cutoff = costsPastSorted[-cutoffIndex]
                    for p in range(len(features_past)):
                        if (costsPast[p - 3] < cutoff <= costsPast[p] > costsPast[
                            p - 2] > p >= 8 and costsPast[p - 4] < cutoff and costsPast[
                                    p - 5] < cutoff and
                                costsPast[p - 6] < cutoff and costsPast[p - 7] < cutoff and costsPast[p - 8] < cutoff):
                            if costsPast[p - 1] < cutoff:
                                costMarkers[p] = 1
                            elif costsPast[p - 1] < costsPast[p]:
                                costMarkers[p - 1] = 0
                                costMarkers[p] = 1
                            else:
                                costMarkers[p] = 0

                        else:
                            costMarkers[p] = 0

            # </editor-fold

            # <editor-fold desc="Make/Store Predictions">
            timeScales = [3, 7, 14, 30]  # Predict 3, 7, 14, 30 candles ahead
            predictions = {}
            actuals = {}
            for scale in timeScales:
                predictions[scale] = 0
                actuals[scale] = 0

            averageCost = 0
            print("\n\n\n\n\nCurrent: ", currentFeature)
            for p in range(len(features_past)):
                if costMarkers[p] == 1:
                    for scale in timeScales:
                        predictions[scale] += outcome(features_past[p][1], scale)
                        print("\n", features_past[p])

                    averageCost += costsPast[p]

            for scale in timeScales:
                predictions[scale] /= sampleSize
            averageCost /= sampleSize

            for scale in timeScales:
                actuals[scale] = outcome(currentFeature[1], scale)

            features_all.append(currentFeature)
            actual_all.append(actuals)
            pred_all.append(predictions)
            cost_all.append(averageCost)

            # </editor-fold

            i += 1

        # </editor-fold

        # <editor-fold desc="Analysis">
        write("\n\nIndicators Chosen: " + str(chosenIndicators))

        predictionResults = {}
        for i in range(predictions):
            for scale in timeScales:
                predictionResults[scale] += abs(pred_all[i][scale] - actual_all[i][scale])
        for scale in timeScales:
            predictionResults[scale] /= len(pred_all)
        testedSets[tuple(chosenIndicators)] = predictionResults

        write("\nPrediction Results: " + str(predictionResults))
        total = 0
        for scale in timeScales:
            total += predictionResults[scale]
        write("\nOverall Rating: " + str(total))

        # </editor-fold

# <editor-fold desc="Final Output">
write("\n\nThe program is done\n The results are: " + str(testedSets))
# </editor-fold
