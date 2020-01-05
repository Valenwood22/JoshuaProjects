from HistoryAnalysis import backTest


class condition:

    def __init__(self, backtestRef=None):
        self.backtest = backtestRef

    def run(self, currentCandle, candlesUpToCurrent):
        if 80 < currentCandle.indicators['STC(23, 50, 10)']:
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "BLUE")  # long
            # return True
            return 'long'
        elif 20 > currentCandle.indicators['STC(23, 50, 10)']:
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "RED")  # short
            # return True
            return 'short'
        else:
            return False
