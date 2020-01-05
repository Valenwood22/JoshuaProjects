class condition:

    def __init__(self, backtestRef=None):
        self.backtest = backtestRef


    def run(self, currentCandle, candlesUpToCurrent):
        if currentCandle.close < currentCandle.indicators['EMA(100)'] <= currentCandle.indicators['EMA(150)']:
            return "long"
        elif currentCandle.indicators['EMA(150)'] < currentCandle.indicators['EMA(100)'] <= currentCandle.close:

            return "short"
        else:
            return False
