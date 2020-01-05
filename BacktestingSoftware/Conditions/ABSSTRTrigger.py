from HistoryAnalysis import backTest


class condition:

    def __init__(self, backtestRef=None):
        self.backtest = backtestRef
        self.lastState = None

    def run(self, currentCandle, candlesUpToCurrent):
        if self.lastState is None:
            if currentCandle.indicators['BullSTR'] >= currentCandle.indicators['BearSTR']:
                self.lastState = 'bulls'
            else:
                self.lastState = 'bears'
        if currentCandle.indicators['BullSTR'] >= currentCandle.indicators['BearSTR'] and self.lastState == 'bears':
            self.lastState = 'bulls'
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "BLUE")  # long
            return 'long'
        elif currentCandle.indicators['BullSTR'] < currentCandle.indicators['BearSTR']and self.lastState == 'bulls':
            self.lastState = 'bears'
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "RED")  # short
            return 'short'
        else:
            return False
