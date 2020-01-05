from HistoryAnalysis import backTest


class condition:

    def __init__(self, backtestRef=None):
        self.backtest = backtestRef
        self.lastState = 0

    def run(self, currentCandle, candlesUpToCurrent):
        if 80 < currentCandle.indicators['STC(23, 50, 10)']:
            if self.lastState is None:
                if currentCandle.indicators['Bears'] <= currentCandle.indicators['Bulls']:
                    self.lastState = 'bulls'
                else:
                    self.lastState = 'bears'
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "BLUE")  # long
            # return True
            return 'long'
        elif 20 > currentCandle.indicators['STC(23, 50, 10)']:
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "RED")  # short
            # return True
            return 'short'
        else:
            return False
