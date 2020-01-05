__authors__ = "Timothy Alexander, Joshua Gisi"
__copyright__ = "Copyright 2019, Project Money Tree"
__version__ = "1.0.3"
__email__ = "TJEnterprises2019@gmail.com"
__status__ = "Development"


import sqlite3
import Support.candleStick as candleStick
import sys
import ta
import pandas as pd
import numpy as np


class sqlCompanion:
    # Global column key that corresponds to each row of the sql data base
    columnKey = {'PID': 0, 'DATETIME': 1, 'OPEN': 2, 'HIGH': 3, 'LOW': 4, 'CLOSE': 5, 'VOLUME': 6, 'GENERATED': 7}

    def __init__(self, databasePath):
        """
        Initiate connection to the database
        :param databasePath: The file path to the database
        """
        self.databasePath = databasePath
        self.connection = sqlite3.connect(self.databasePath)
        self.cursor = self.connection.cursor()





    def getDataInRange(self, tableName, printReturn=False, granularity='M1', startPID=1, endPID=2, indicators=None):
        """
        Returns all the columns from the database in range of the specified PID's. Also used in other methods to
        get rows by datetime
        :param indicators:
        :param tableName: Which table to query from ie. EURUSD, EURGBP ect..
        :param printReturn: Whether or not to print the resulting rows
        :param columns: An array representing which columns to print ie. PID, OPEN, CLOSE, ect...
        :param granularity: The time frame of the candles ie. M1, M15
        :param startPID: The PID is the index of the table row 1 has a PID of 1
        :param endPID: The PID where the query stops
        :return: A matrix representing the chosen candlesticks in the database
        """
        dataset = []
        rowset = []
        if granularity == 'M1':  # Get M1 candles by executing a SQL Select command
            for rowPID in range(startPID,
                                endPID + 1):  # Only one row is selected at a time because of the limited memory on Digital Ocean
                self.cursor.execute(
                    'SELECT * FROM ' + tableName + ' WHERE PID=' + str(rowPID))
                row = self.cursor.fetchall()[0]
                rowset.append(row)


        # Get M15 candles by executing a SQL select command
        elif granularity == 'M15':
            i = 0
            o = -1
            h = -1
            l = 100000000
            c = -1
            v = 0
            pid = -1
            datetime = 'NULL'
            for rowPID in range(startPID, endPID + 1):  # Convert M1 candles to M15 candles
                i += 1
                self.cursor.execute('SELECT * FROM ' + tableName + ' WHERE PID=' + str(rowPID))
                row = self.cursor.fetchall()[0]

                if i == 1:
                    o = row[self.columnKey['OPEN']]
                    pid = row[self.columnKey['PID']]
                    datetime = row[self.columnKey['DATETIME']]
                if row[self.columnKey['HIGH']] > h: h = row[self.columnKey['HIGH']]
                if row[self.columnKey['LOW']] < l: l = row[self.columnKey['LOW']]
                if i == 15: c = row[self.columnKey['CLOSE']]
                v += row[self.columnKey['VOLUME']]

                if i >= 15:
                    rowM15 = [pid, datetime, o, h, l, c, v, 0]
                    rowset.append(rowM15)
                    i = 0
                    o = -1
                    h = -1
                    l = 100000000
                    c = -1
                    v = 0






        elif granularity == 'M5':  # Get M5 candles by executing a SQL select command
            i = 0
            o = -1
            h = -1
            l = 100000000
            c = -1
            v = 0
            pid = -1
            datetime = 'NULL'
            for rowPID in range(startPID, endPID + 1):  # Convert M1 candles to M5 candles
                i += 1
                self.cursor.execute('SELECT * FROM ' + tableName + ' WHERE PID=' + str(rowPID))
                row = self.cursor.fetchall()[0]

                if i == 1:
                    o = row[self.columnKey['OPEN']]
                    pid = row[self.columnKey['PID']]
                    datetime = row[self.columnKey['DATETIME']]
                if row[self.columnKey['HIGH']] > h: h = row[self.columnKey['HIGH']]
                if row[self.columnKey['LOW']] < l: l = row[self.columnKey['LOW']]
                if i == 5: c = row[self.columnKey['CLOSE']]
                v += row[self.columnKey['VOLUME']]

                if i >= 5:
                    rowM5 = [pid, datetime, o, h, l, c, v, 0]
                    rowset.append(rowM5)
                    i = 0
                    o = -1
                    h = -1
                    l = 100000000
                    c = -1
                    v = 0




        else:
            return "Invalid Granularity: Choose (M1, M5, M15)"

        # Add Indicators
        pandasDataSet = self.calculateIndicators(indicators, rowset)
        for index, row in pandasDataSet.iterrows():
            candle = candleStick.candle(row['Pid'], row['Datetime'], row['Open'], row['High'], row['Low'], row['Close'], row['Volume'],generated=row['Generated'], indicators=row['Indicators'])
            dataset.append(candle)
            if printReturn:
                print(str(candle))
        return dataset








    def getDataAll(self, tableName, granularity='M1', printReturn=False, columns=None, indicators=None):
        """
        Gets all the rows in a database table ie. EURUSD, EURGBP ect..
        :param indicators:
        :param tableName: Which table to query from
        :param granularity: The time frame of the candles ie. M1, M15
        :param printReturn: Whether or not to print the resulting rows
        :param columns: An array representing which columns to print ie. PID, OPEN, CLOSE, ect...
        :return: A matrix representing all candlesticks in the database
        """
        self.cursor.execute('SELECT MAX(PID) FROM ' + tableName)
        largestPID = self.cursor.fetchall()[0][0]
        return self.getDataInRange(tableName, printReturn=printReturn, granularity=granularity,
                                   endPID=largestPID, indicators=indicators)








    def getDataByDatetime(self, tableName, startDatetime, endDatetime, granularity='M1', columns=None,
                          printReturn=False, indicators = None):
        """
        Returns all the columns from the database in range of the specified datetime. the datetime parameter can either be a
        String or a datetime object
        :param tableName: Which table to query from ie. EURUSD, EURGBP ect..
        :param startDatetime: A string or a datetime object that specifies where the query should start
        :param endDatetime: A string or a datetime object that specifies where the query should end
        :param granularity: The time frame of the candles ie. M1, M15
        :param columns: An array representing which columns to print ie. PID, OPEN, CLOSE, ect...
        :param printReturn: Whether or not to print the resulting rows
        :return:
        """
        # checks if a datetime object was passed as a parameter if so converts to a string
        startDatetime, endDatetime = self.__formatDatetimeType(startDatetime, endDatetime)
        # Find the start datetime with the corresponding PID
        self.cursor.execute('SELECT PID FROM ' + tableName + ' WHERE DATETIME= "' + startDatetime + '"')
        startPID = self.cursor.fetchall()[0][0]
        # Find the end datetime with the corresponding PID
        self.cursor.execute('SELECT PID FROM ' + tableName + ' WHERE DATETIME= "' + endDatetime + '"')
        endPID = self.cursor.fetchall()[0][0]
        return self.getDataInRange(tableName, printReturn=printReturn, granularity=granularity,
                                   startPID=startPID, endPID=endPID, indicators=indicators)









    def calculateIndicators(self, indicators, rowset):
        """
        Add calculat and add indicator data to the candle
        :param indicators: An array of indicator names to add to the candles
        :param rowset: An array of candle objects
        :return: An array of candle objects with indicator data
        """

        dataset = pd.DataFrame(rowset)
        dataset.columns = ['Pid', 'Datetime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Generated']

        if not indicators:
            dataset['Indicators'] = [{}] * len(dataset)
            return dataset

        indiDataframe = pd.DataFrame()
        for indicator in indicators:
            name = indicator.replace(indicator[indicator.find("(")+1:indicator.find(")")],'')
            try: indiParam = [int(i) for i in indicator[indicator.find("(")+1:indicator.find(")")].split(',')]
            except: indiParam = None

            if name == 'BvsB()':
                indiDataframe['TempEMA'] = dataset['Close'].ewm(span=indiParam[0], min_periods=0, adjust=False, ignore_na=False).mean()
                indiDataframe['Bears'] = round((indiDataframe['TempEMA'] - dataset['Low']) / 0.00001)
                indiDataframe['Bulls'] = round((dataset['High'] - indiDataframe['TempEMA']) / 0.00001)
                # del(indiDataframe['TempEMA'])

            elif name == 'CCI()':                                                                                           # n=14
                indiDataframe[f'CCI({indiParam[0]}, {indiParam[1]})'] = ta.trend.cci(dataset['High'], dataset['Low'], dataset['Close'], n=indiParam[0], c=0.015, fillna=False)
                # indiDataframe['CCIPast1'] = indiDataframe['CCI'].shift(1)
                # indiDataframe['CCIPast3'] = indiDataframe['CCI'].shift(3)
                # indiDataframe['CCIPast5'] = indiDataframe['CCI'].shift(5)

            elif name == 'DPO()':                                               # n=20
                indiDataframe[f'DPO({indiParam[0]})'] = ta.trend.dpo(dataset['Close'], n=indiParam[0], fillna=False)
                # indiDataframe['DPOPast1'] = indiDataframe['DPO'].shift(1)
                # indiDataframe['DPOPast3'] = indiDataframe['DPO'].shift(3)
                # indiDataframe['DPOPast5'] = indiDataframe['DPO'].shift(5)

            elif name == 'EMA()':
                # from Indicators.EMA import indicator as ema
                # indiDataframe[f'EMA({indiParam[0]})'] = ema().calculateAll(dataset['Close'],indiParam[0])
                indiDataframe[f'EMA({indiParam[0]})'] = dataset['Close'].ewm(span=indiParam[0], min_periods=0, adjust=False, ignore_na=False).mean()

            elif name == 'MI()':                                                                                # n=14       n2=25
                indiDataframe[f'MI({indiParam[0]}, {indiParam[1]})'] = ta.trend.mass_index(dataset['High'], dataset['Low'], n=indiParam[0], n2=indiParam[1], fillna=False)
                # indiDataframe['MIPast1'] = indiDataframe['MI'].shift(1)
                # indiDataframe['MIPast3'] = indiDataframe['MI'].shift(3)
                # indiDataframe['MIPast5'] = indiDataframe['MI'].shift(5)

            elif name == '%R()':                                                                                  # 1bp=14
                indiDataframe[f'%R({indiParam[0]})'] = ta.momentum.wr(dataset['High'], dataset['Low'], dataset['Close'], lbp=indiParam[0], fillna=False)
                # indiDataframe['%RPast1'] = indiDataframe['%R'].shift(1)
                # indiDataframe['%RPast3'] = indiDataframe['%R'].shift(3)
                # indiDataframe['%RPast5'] = indiDataframe['%R'].shift(5)

            elif name == 'RSI()':                                                    # n=14
                indiDataframe[f'RSI({indiParam[0]})'] = ta.momentum.rsi(dataset['Close'], n=indiParam[0], fillna=False)
                # indiDataframe['RSIPast1'] = indiDataframe['RSI'].shift(1)
                # indiDataframe['RSIPast3'] = indiDataframe['RSI'].shift(3)
                # indiDataframe['RSIPast5'] = indiDataframe['RSI'].shift(5)

            elif name == 'STC()':
                indiDataframe['TempEMAShort'] = dataset['Close'].ewm(span=indiParam[0], min_periods=0,adjust=False, ignore_na=False).mean()
                indiDataframe['TempEMALong'] = dataset['Close'].ewm(span=indiParam[1], min_periods=0, adjust=False, ignore_na=False).mean()
                indiDataframe['TempMACD'] = indiDataframe['TempEMAShort'] - indiDataframe['TempEMALong']
                del(indiDataframe['TempEMAShort'])
                del(indiDataframe['TempEMALong'])
                indiDataframe['TempLow'] = indiDataframe['TempMACD'].rolling(window=indiParam[2]).min()
                indiDataframe['TempHigh'] = indiDataframe['TempMACD'].rolling(window=indiParam[2]).max()
                indiDataframe['TempSTOCH'] = 100 * ((indiDataframe['TempMACD'] - indiDataframe['TempLow']) / (indiDataframe['TempHigh'] - indiDataframe['TempLow']))
                del indiDataframe['TempLow']
                del indiDataframe['TempHigh']
                indiDataframe.loc[indiParam[2]-1, f'STC({indiParam[0]}, {indiParam[1]}, {indiParam[2]})'] = indiDataframe.loc[indiParam[2], 'TempSTOCH']
                for i in range(indiParam[2],len(indiDataframe['TempSTOCH'])):
                    indiDataframe.loc[i, f'STC({indiParam[0]}, {indiParam[1]}, {indiParam[2]})'] = indiDataframe.loc[i-1, f'STC({indiParam[0]}, {indiParam[1]}, {indiParam[2]})'] + (0.5 * (indiDataframe.loc[i, 'TempSTOCH'] - indiDataframe.loc[i-1, f'STC({indiParam[0]}, {indiParam[1]}, {indiParam[2]})'] ))
                del indiDataframe['TempSTOCH']
                del indiDataframe['TempMACD']

            elif name == 'TRIX()':                                                # n=14
                indiDataframe[f'TRIX({indiParam[0]})'] = ta.trend.trix(dataset['Close'], n=indiParam[0], fillna=False)
                # indiDataframe['TRIXPast1'] = indiDataframe['TRIX'].shift(1)
                # indiDataframe['TRIXPast3'] = indiDataframe['TRIX'].shift(3)
                # indiDataframe['TRIXPast5'] = indiDataframe['TRIX'].shift(5)

            elif name == 'UO()':                                                                                                                                         # s=7        m=14       len=28       ws=     wm=     wl=
                indiDataframe[f'UO({indiParam[0]}, {indiParam[1]}, {indiParam[2]}, {indiParam[3]}, {indiParam[4]}, {indiParam[5]})'] = ta.momentum.uo(dataset['High'], dataset['Low'], dataset['Close'], s=indiParam[0], m=indiParam[1], len=indiParam[2], ws=4.0, wm=2.0, wl=1.0, fillna=False)
                # indiDataframe['UOPast1'] = indiDataframe['UO'].shift(1)
                # indiDataframe['UOPast3'] = indiDataframe['UO'].shift(3)
                # indiDataframe['UOPast5'] = indiDataframe['UO'].shift(5)

            elif name == 'VORTEX()':                                                                                                 # n=14
                indiDataframe[f'VORTEX({indiParam[0]})'] = ta.trend.vortex_indicator_neg(dataset['High'], dataset['Low'], dataset['Close'], n=indiParam[0], fillna=False)
                # indiDataframe['VORTEXPast1'] = indiDataframe['VORTEX'].shift(1)
                # indiDataframe['VORTEXPast3'] = indiDataframe['VORTEX'].shift(3)
                # indiDataframe['VORTEXPast5'] = indiDataframe['VORTEX'].shift(5)



            # Oscillators
            elif name == 'STOCH()':
                indiDataframe[f'Low({indiParam[0]})'] = dataset['Low'].rolling(window=indiParam[0]).min()
                indiDataframe[f'High({indiParam[0]})'] = dataset['High'].rolling(window=indiParam[0]).max()
                indiDataframe[f'STOCH({indiParam[0]}, {indiParam[1]})'] = 100*((dataset['Close'] - indiDataframe[f'Low({indiParam[0]})']) / (indiDataframe[f'High({indiParam[0]})'] - indiDataframe[f'Low({indiParam[0]})']))
                indiDataframe['%D'] = indiDataframe[f'STOCH({indiParam[0]}, {indiParam[1]})'].rolling(window=indiParam[1]).mean()
                del indiDataframe[f'Low({indiParam[0]})']
                del indiDataframe[f'High({indiParam[0]})']

            elif name == 'ABSSTR()':    # Default 10 2
                indiDataframe['tempBulls'] = 0.5 * abs(dataset['Close'] - dataset['Close'].shift(1)) + dataset['Close'] - dataset['Close'].shift(1)
                indiDataframe['tempBears'] = 0.5 * abs(dataset['Close'] - dataset['Close'].shift(1)) - dataset['Close'] + dataset['Close'].shift(1)
                indiDataframe['tempAvgBulls'] = indiDataframe['tempBulls'].rolling(window=indiParam[0]).mean()
                indiDataframe['tempAvgBears'] = indiDataframe['tempBears'].rolling(window=indiParam[0]).mean()
                del(indiDataframe['tempBulls'])
                del(indiDataframe['tempBears'])
                indiDataframe[f'BullSTR'] = (indiDataframe['tempAvgBulls'] / 0.00001).rolling(window=indiParam[1]).mean()
                indiDataframe[f'BearSTR'] = (indiDataframe['tempAvgBears'] / 0.00001).rolling(window=indiParam[1]).mean()
                del (indiDataframe['tempAvgBulls'])
                del (indiDataframe['tempAvgBears'])

                # Momentum
            elif name == 'ADX()':                                                                                # n=14
                indiDataframe[f'ADX({indiParam[0]})'] = ta.trend.adx(dataset['High'], dataset['Low'], dataset['Close'], n=indiParam[0], fillna=True)
                # indiDataframe['ADXPast1'] = indiDataframe['ADX'].shift(1)
                # indiDataframe['ADXPast3'] = indiDataframe['ADX'].shift(3)
                # indiDataframe['ADXPast5'] = indiDataframe['ADX'].shift(5)

            elif name == 'ATR()':                                                                                                    # n=14
                indiDataframe[f'ATR({indiParam[0]})'] = ta.volatility.average_true_range(dataset['High'], dataset['Low'], dataset['Close'], n=indiParam[0], fillna=False)
                # indiDataframe['ATRPast1'] = indiDataframe['ATR'].shift(1)
                # indiDataframe['ATRPast3'] = indiDataframe['ATR'].shift(3)
                # indiDataframe['ATRPast5'] = indiDataframe['ATR'].shift(5)

            elif name == 'MFI()':
                indiDataframe[f'MFI({indiParam[0]})'] = ta.momentum.money_flow_index(dataset['High'], dataset['Low'], dataset['Close'], dataset['Volume'], n=indiParam[0], fillna=False)
                # indiDataframe['MFIPast1'] = indiDataframe['MFI'].shift(1)
                # indiDataframe['MFIPast3'] = indiDataframe['MFI'].shift(3)
                # indiDataframe['MFIPast5'] = indiDataframe['MFI'].shift(5)

            elif name == 'STDEV()':
                indiDataframe['STDEV()'] = dataset['Close'].rolling(20).std()
                # indiDataframe['STDEVPast1'] = indiDataframe['STDEV'].shift(1)
                # indiDataframe['STDEVPast3'] = indiDataframe['STDEV'].shift(3)
                # indiDataframe['STDEVPast5'] = indiDataframe['STDEV'].shift(5)

            elif name == 'TSI()':                                                                                #r = 25, s = 13
                indiDataframe[f'TSI({indiParam[0], indiParam[1]})'] = ta.momentum.tsi(dataset['Close'], r=indiParam[0], s=indiParam[1], fillna=False)
                # indiDataframe['TSIPast1'] = indiDataframe['TSI'].shift(1)
                # indiDataframe['TSIPast3'] = indiDataframe['TSI'].shift(3)
                # indiDataframe['TSIPast5'] = indiDataframe['TSI'].shift(5)


            # Volume
            elif name == '2CANDLEVOLUME()':
                indiDataframe['2CANDLEVOLUME()'] = (dataset['Volume'] + dataset['Volume'].shift(1))
                # indiDataframe['2CANDLEVOLUMEPast1'] = indiDataframe['2CANDLEVOLUME'].shift(1)
                # indiDataframe['2CANDLEVOLUMEPast3'] = indiDataframe['2CANDLEVOLUME'].shift(3)
                # indiDataframe['2CANDLEVOLUMEPast5'] = indiDataframe['2CANDLEVOLUME'].shift(5)

            elif name == 'VOLMADIF()':
                indiDataframe['VOLMADIF()'] = dataset['Volume'].rolling(2).mean() - dataset['Volume'].rolling(7).mean()
                # indiDataframe['VOLMADIFPast1'] = indiDataframe['VOLMADIF'].shift(1)
                # indiDataframe['VOLMADIFPast3'] = indiDataframe['VOLMADIF'].shift(3)
                # indiDataframe['VOLMADIFPast5'] = indiDataframe['VOLMADIF'].shift(5)

            elif name == 'CMV()':                                                                                                                   # n=14
                indiDataframe[f'CMV({indiParam[0]})'] = ta.volume.chaikin_money_flow(dataset['High'], dataset['Low'], dataset['Close'], dataset['Volume'], n=indiParam[0], fillna=False)
                # indiDataframe['CMVPast1'] = indiDataframe['CMV'].shift(1)
                # indiDataframe['CMVPast3'] = indiDataframe['CMV'].shift(3)
                # indiDataframe['CMVPast5'] = indiDataframe['CMV'].shift(5)

            elif name == 'EoM()':                                                                                                                   # n=14
                indiDataframe[f'EoM({indiParam[0]})'] = ta.volume.ease_of_movement(dataset['High'], dataset['Low'], dataset['Close'], dataset['Volume'], n=indiParam[0], fillna=False)
                # indiDataframe['EoMPast1'] = indiDataframe['EoM'].shift(1)
                # indiDataframe['EoMPast3'] = indiDataframe['EoM'].shift(3)
                # indiDataframe['EoMPast5'] = indiDataframe['EoM'].shift(5)

            else:
                print(" === Invalid Indicator === ")
                sys.exit(1)

        indiDict = indiDataframe.to_dict('index')
        dataset['Indicators'] = [v for v in indiDict.values()]
        return dataset







    @staticmethod
    def __formatDatetimeType(start, end):
        """
        A private method to convert a datetime object to a string
        :param start: Start datetime
        :param end: End datetime
        :return: A start and end datetime string
        """
        if not isinstance(start, str):
            startStr = start.strftime("%Y-%m-%d %H:%M:%S")
        else:
            startStr = start
        if not isinstance(end, str):
            endStr = end.strftime("%Y-%m-%d %H:%M:%S")
        else:
            endStr = end

        return startStr, endStr







    def closeConnection(self):
        """
        Closes the connection to the database
        :return:
        """
        self.connection.close()



if __name__ == '__main__':
    Data = sqlCompanion("C:\\Users\\Administrator\\Desktop\\BackTestData.db")
    # Get M1 candles within datetime range
    dataSet = Data.getDataByDatetime("EUR_USD", printReturn=True, startDatetime='2007-01-03 02:00:00',
                                     granularity="M1", endDatetime='2007-01-05 04:00:00', indicators=[])
    print("Done")

'''
=============================================================================
Examples of how to implement companion in another class
=============================================================================

import Companion

# Initiate companion object
Data = Companion.Companion("C:\\Users\\Administrator\\Desktop\\BackTestData.db")

# Get M1 candles within datetime range
dataSet = Data.getDataByDatetime("EUR_USD",printReturn=True, startDatetime='2007-01-03 02:00:00', endDatetime='2007-01-03 04:00:00', 
                                    columns=['DATETIME','OPEN','HIGH','LOW','CLOSE'])

# Get M15 candles within datetime range
dataSet2 = Data.getDataByDatetime("EUR_USD",printReturn=True, granularity='M15', startDatetime='2006-01-03 02:00:00', 
                                    endDatetime='2006-01-03 02:29:00')

# Gets all candles from database
Data.getDataAll('EUR_USD', granularity='M15', printReturn=True)

# Gets data in PID range
Dataset = Data.getDataInRange("EUR_USD", startPID=200, endPID=250, printReturn=True, granularity='M15')

# Close connection
Data.closeConnection()
'''
