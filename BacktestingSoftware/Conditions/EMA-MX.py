from Indicators.EMA import indicator as ema
from Support.Companion import sqlCompanion
from Support import candleStick


class condition:

    def __init__(self, backtestRef=None):
        self.M100EMASet = []
        # INCLUSIVE
        self.START_TREND_PATTERN = 1
        self.END_TREND_PATTERN = 100

    def run(self, currentCandle, candlesUpToCurrent):
        currentEMA = ema().run(currentCandle, candlesUpToCurrent, 500)
        self.M100EMASet.append(currentCandle)
        self.M100EMASet[-1].indicators['EMA(500)'] = currentEMA

        if currentEMA < currentCandle.open:
            return "long"
        else:
            return "short"




    def getEMASet(self):
        return self.M100EMASet