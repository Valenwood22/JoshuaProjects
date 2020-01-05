class condition:

    def __init__(self, backtestRef=None):
        self.backtest = backtestRef

    def run(self, currentCandle, candlesUpToCurrent):
        if 80 < currentCandle.indicators['STOCH(5, 3)'] <= currentCandle.indicators['%D']:
            # backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "BLUE")  # long
            return "short"
        elif 20 > currentCandle.indicators['STOCH(5, 3)'] >= currentCandle.indicators['%D']:
            # backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "RED")  # short
            return "long"
        else:
            return False
