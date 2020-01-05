class condition:

    def __init__(self, backtestRef=None):
        self.backtest = backtestRef
        self.lastState = None


    def run(self, currentCandle, candlesUpToCurrent):
        if self.lastState is None:
            if currentCandle.indicators['Bears'] <= currentCandle.indicators['Bulls']:
                self.lastState = 'bulls'
            else:
                self.lastState = 'bears'
        if currentCandle.indicators['Bears'] <= currentCandle.indicators['Bulls'] and self.lastState == 'bears':
            # backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "BLUE")  # long
            self.lastState = 'bulls'
            return 'long'
        elif currentCandle.indicators['Bears'] > currentCandle.indicators['Bulls'] and self.lastState == 'bulls':
            # backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "RED")  # short
            self.lastState = 'bears'
            return 'short'
        else:
            return False
