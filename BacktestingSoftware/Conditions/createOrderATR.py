
from HistoryAnalysis import backTest

class condition:
    def __init__(self, currentCandle, candlesUpToCurrent, position, backtestRef=None):

        self.backtest = backtestRef
        self.position = position
        self.sl = self.findSL(candlesUpToCurrent,currentCandle, position)
        self.openPrice = self.findopenPrice(candlesUpToCurrent,currentCandle, position)



    def findSL(self, candlesUpToCurrent, currentCandle, position):
        if position == 'long':
            sl = currentCandle.close - currentCandle.indicators['ATR(14)'] * 1.5
            backTest.addHorizontalLine(self.backtest, currentCandle.datetime, "Horizontal At Price", price=sl)
            return sl

        if position == 'short':
            sl = currentCandle.close + currentCandle.indicators['ATR(14)'] * 1.5
            backTest.addHorizontalLine(self.backtest, currentCandle.datetime, "Horizontal At Price", price=sl)
            return sl






    def findopenPrice(self, candlesUpToCurrent, currentCandle, position):
        if position == 'long':
            op = currentCandle.close + currentCandle.indicators['ATR(14)'] * 1.5
            backTest.addHorizontalLine(self.backtest, currentCandle.datetime, "Horizontal At Price", price=op)
            return op
        if position == 'short':
            op = currentCandle.close - currentCandle.indicators['ATR(14)'] * 1.5
            backTest.addHorizontalLine(self.backtest, currentCandle.datetime, "Horizontal At Price", price=op)
            return op