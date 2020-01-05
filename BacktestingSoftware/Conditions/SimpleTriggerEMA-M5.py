class condition:
    def __init__(self, backtestRef=None):
        self.backtest = backtestRef
        pass


    def run(self, currentCandle, candlesUpToCurrent):
        if currentCandle.datetime == '2009-01-05 19:32:00':
            from HistoryAnalysis import backTest
            backTest.addMarker(self.backtest, '2009-01-05 19:32:00', "Simple Mark Above")

            return True
        return False