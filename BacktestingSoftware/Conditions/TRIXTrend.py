from HistoryAnalysis import backTest


class condition:

    def __init__(self, backtestRef=None):
        self.backtest = backtestRef
        self.lastState = None


    def run(self, currentCandle, candlesUpToCurrent):
        if currentCandle.indicators['TRIX(14)'] >= 0:
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "BLUE")  # long
            return 'long'
        elif currentCandle.indicators['TRIX(14)'] < 0:
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "RED")  # short
            return 'short'
        else:
            return False
