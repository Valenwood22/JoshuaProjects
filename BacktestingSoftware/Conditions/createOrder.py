
from HistoryAnalysis import backTest

class condition:
    def __init__(self, currentCandle, candlesUpToCurrent, position, backtestRef=None):

        self.backtest = backtestRef
        self.position = position
        self.sl = self.findSL(candlesUpToCurrent,currentCandle, position)
        self.openPrice = self.findopenPrice(candlesUpToCurrent,currentCandle, position)



    def findSL(self, candlesUpToCurrent, currentCandle, position):
        if position == 'long':
            saveIndex = -1
            l = 100000000
            for i in range(-5,0):
                if l > candlesUpToCurrent[i].low: l = candlesUpToCurrent[i].low; saveIndex = i
            backTest.addHorizontalLine(self.backtest, candlesUpToCurrent[saveIndex].datetime, "Simple Horizontal Below", pipOffset=3)
            return l - 0.0003
        if position == 'short':
            saveIndex = -1
            h = -1
            for i in range(-5,0):
                if h < candlesUpToCurrent[i].high: h = candlesUpToCurrent[i].high; saveIndex = i
            backTest.addHorizontalLine(self.backtest, candlesUpToCurrent[saveIndex].datetime, "Simple Horizontal Above", pipOffset=3)
            return h + 0.0003






    def findopenPrice(self, candlesUpToCurrent, currentCandle, position):
        if position == 'long':
            saveIndex = -1
            h = -1
            for i in range(-25,0):
                if h < candlesUpToCurrent[i].high: h = candlesUpToCurrent[i].high; saveIndex = i
            backTest.addHorizontalLine( self.backtest, candlesUpToCurrent[saveIndex].datetime, "Simple Horizontal Above", pipOffset=3)
            return h + 0.0003
        if position == 'short':
            saveIndex = -1
            l = 100000000
            for i in range(-25,0):
                if l > candlesUpToCurrent[i].low: l = candlesUpToCurrent[i].low; saveIndex = i
            backTest.addHorizontalLine(self.backtest, candlesUpToCurrent[saveIndex].datetime, "Simple Horizontal Below", pipOffset=3)
            return l - 0.0003