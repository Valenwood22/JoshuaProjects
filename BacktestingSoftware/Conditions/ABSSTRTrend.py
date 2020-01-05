from HistoryAnalysis import backTest


class condition:

    def __init__(self, backtestRef=None):
        self.backtest = backtestRef

    def run(self, currentCandle, candlesUpToCurrent):
        if currentCandle.indicators['BullSTR'] >= currentCandle.indicators['BearSTR']:
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "BLUE")  # long
            # return True
            return 'NA'
        elif currentCandle.indicators['BullSTR'] < currentCandle.indicators['BearSTR']:
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "RED")  # short
            # return True
            return 'NA'
        else:
            return False
