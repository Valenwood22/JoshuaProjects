
__author__ = "Timothy Alexander, Joshua Gisi"
__copyright__ = "Copyright 2019, Project Money Tree"
__version__ = "0.0.1"
__email__ = "TJEnterprises2019@gmail.com"
__status__ = "Development"

import os
from Support.Companion import sqlCompanion as companion
from Support.treasureMap import Map
from tkinter import *
import configparser



class backTest:

    def __init__(self, M1candles):
        """
        Initiate class specific data. Make sure to edit the config file as well.
        :param M1candles: An array of candle objects
        """
        self.M1Candles = M1candles
        self.markers = []
        self.purchases = []
        self.entryState = "No Order"
        self.riskPrice = -1
        self.sl = -1
        self.money = 100
        self.moneyInTrade = 0
        self.leverage = 20
        self.risk = 0.02

        self.configs = configparser.ConfigParser()
        config_file = os.path.join(os.path.dirname(__file__), 'HistoryAnalysisConfig.ini')
        self.configs.read(config_file)

        self.openConditionObj = []
        self.closeConditionObj = []
        self.initClasses(list(self.configs.get('conditions', 'openConditions').split(', ')),list(self.configs.get('conditions', 'closeConditions').split(', ')))

        self.delayCandles = self.configs.getint('control', 'delayCandles')
        self.run(M1candles)







    def run(self, M1candles):
        """
        A buying/selling simulator for back testing Forex strategies
        :param M1candles: An array of candle objects
        :return:
        """
        candlesUpToCurrent = []
        for curCandle in M1candles:
            candlesUpToCurrent.append(curCandle)


            checkConditions = self.openConditions(curCandle, candlesUpToCurrent)

            if self.entryState == "No Order" and (checkConditions == "long" or checkConditions == "short") and self.delayCandles <= 0:
                self.entryState = "Order Fulfilled"
                from Conditions.createOrder import condition as createOrder
                order = createOrder(curCandle, candlesUpToCurrent, checkConditions, backtestRef=self)
                self.sl = order.sl
                self.purchases.append({'openDT': curCandle.datetime, 'openPrice': curCandle.close, 'pos': checkConditions})
                for con in self.closeConditionObj:
                    con.setup(curCandle, candlesUpToCurrent, order.position)

            elif self.entryState == "Order Fulfilled" and self.closeConditions(curCandle, candlesUpToCurrent, order.position):
                self.entryState = "No Order"

            if self.delayCandles >= 0: self.delayCandles -= 1

        self.paintMap()







    def initClasses(self, openConditionList, closeConditionList):
        """
        Run the open/close condition classes specified in the config.ini to initiates their data
        :param openConditionList: A list of open condition classes that all must be met in order for a new positions to occur
        :param closeConditionList: A list of close condition classes that all must be met in order for a close position to occur
        :return:
        """
        for con in openConditionList:
            name = "condition"
            package = "Conditions."+con
            obj = getattr(__import__(package,fromlist=[name]), name)
            self.openConditionObj.append(obj(self))

        for con in closeConditionList:
            name = "condition"
            package = "Conditions." + con
            obj = getattr(__import__(package, fromlist=[name]), name)
            self.closeConditionObj.append(obj(self))







    def openConditions(self, curCandle, candlesUpToCurrent):
        """
        Check if the open conditions are met
        :param curCandle:
        :param candlesUpToCurrent:
        :return:
        """
        votesToBuy = 0
        votesToSell = 0
        for con in self.openConditionObj:
            checkConditions = con.run(curCandle, candlesUpToCurrent)
            if checkConditions == 'long':
                votesToBuy += 1
            elif checkConditions == 'short':
                votesToSell += 1
            elif checkConditions == 'NA':
                votesToSell += 0
                votesToBuy += 0
            else:
                votesToBuy = -10000
                votesToSell = -10000

        if votesToSell == 0 and votesToBuy == 0:
            return False
        elif votesToSell == 0 and votesToBuy > 0:
            return "long"
        elif votesToSell > 0 and votesToBuy == 0:
            return "short"

        return False







    def closeConditions(self, curCandle, candlesUpToCurrent, position):
        """
        Check if the close conditions are met
        :param curCandle:
        :param candlesUpToCurrent:
        :return:
        """
        for con in self.closeConditionObj:
            if not con.run(curCandle, candlesUpToCurrent, position):
                return False
        return True







    def addMarker(self, datetime, name, color, text=None):
        """
        Adds a marker to an array which will end up in the Treasure map class to be painted
        :param datetime:
        :param name: type of marker
        :param color:
        :param text:
        :return:
        """
        self.markers.append({'datetime':datetime, 'type':name, 'color':color, 'text':text})







    def addHorizontalLine(self, datetime, name, pipOffset=0, color="RED", price=0):
        """
        Adds a marker to an array which will end up in the Treasure map class to be painted
        :param datetime:
        :param name:
        :param pipOffset:
        :param color:
        :param price:
        :return:
        """
        self.markers.append({'datetime':datetime, 'type':name, 'pipOffset': pipOffset, 'color': color, 'price':price})







    def paintMap(self):
        """
        Create a tKinter canvas and populate it
        :return:
        """
        root = Tk()
        Map(root, self.M1Candles, self.purchases, markers=self.markers, indicators=[]) # {'name':'EMA(100)', 'color':'BLUE'}, {'name':'EMA(150)', 'color':'RED'}
        root.mainloop()





if __name__ == '__main__':
    Data = companion("C:\\Users\\treeb\\OneDrive\\Desktop\\BackTestData.db")
    dataSet = Data.getDataByDatetime("EUR_USD", printReturn=False, granularity='M1',
                                     startDatetime='2017-01-05 02:00:00', endDatetime='2018-04-06 02:05:00', indicators=[])


    backTest(dataSet)
    Data.closeConnection()