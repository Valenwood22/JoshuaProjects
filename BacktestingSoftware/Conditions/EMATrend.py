class condition:

    def __init__(self, backtestRef=None):
        self.backtest = backtestRef

    def run(self, currentCandle, candlesUpToCurrent):
        if currentCandle.indicators['EMA(50)'] >= currentCandle.close:
            # backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "BLUE")  # long
            return "long"
        elif currentCandle.indicators['EMA(50)'] < currentCandle.close:
            # backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "RED")  # short
            return "short"
        else:
            return False
