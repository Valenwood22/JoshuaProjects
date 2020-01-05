from Indicators.EMA import indicator as ema
from Support import candleStick
from HistoryAnalysis import backTest


class condition:

    def __init__(self, backtestRef=None):
        self.M5dataSet = []
        self.spreadPatternSell = 0
        self.spreadPatternBuy = 0

        self.TREND_PATTERN = 3
        self.backtest = backtestRef



    def run(self, currentCandle, candlesUpToCurrent):
        if len(candlesUpToCurrent) % 5 == 0:
            self.createM5Candle(candlesUpToCurrent)
            self.M5dataSet[-1].indicators['EMA(8)'] = ema().run(self.M5dataSet[-1], self.M5dataSet, 8)
            self.M5dataSet[-1].indicators['EMA(13)'] = ema().run(self.M5dataSet[-1], self.M5dataSet, 13)
            self.M5dataSet[-1].indicators['EMA(21)'] = ema().run(self.M5dataSet[-1], self.M5dataSet, 21)



            trigger = self.isSpreading(currentCandle)
            if trigger == 'long':
                self.spreadPatternSell = 0
                self.spreadPatternBuy += 1

            elif trigger == 'short':
                self.spreadPatternBuy = 0
                self.spreadPatternSell += 1


            elif trigger == 'Open Long':
                backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "RED")
                return 'long'

            elif trigger == 'Open Short':
                backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "RED")
                return 'short'

            else:

                self.spreadPatternSell = 0
                self.spreadPatternBuy = 0

        return False







    # The trigger happens when the candles touches above/below the EMA-M5 Granularity(8) line
    def touchTrigger(self, currentCandle):
        if self.spreadPatternBuy >= self.TREND_PATTERN and self.M5dataSet[-1].indicators['EMA(8)'] > currentCandle.low > self.M5dataSet[-1].indicators['EMA(21)']:
            return 'Open Long'
        elif self.spreadPatternSell >= self.TREND_PATTERN and self.M5dataSet[-1].indicators['EMA(8)'] < currentCandle.high < self.M5dataSet[-1].indicators['EMA(21)']:
            return 'Open Short'
        else:
            return False






    def createM5Candle(self, candlesUpToCurrent):
        o = candlesUpToCurrent[-5].open
        h = -1
        l = 100000000000000
        c = candlesUpToCurrent[-1].close
        v = 0
        datetime = candlesUpToCurrent[-1].datetime
        for i in range(-5, 0):
            if candlesUpToCurrent[i].high > h: h = candlesUpToCurrent[i].high
            if candlesUpToCurrent[i].low < l: l = candlesUpToCurrent[i].low
            v += candlesUpToCurrent[i].volume
        self.M5dataSet.append(candleStick.candle(0, datetime, o, h, l, c, v))







    def isSpreading(self, currentCandle):
        # see if the EMA are spreading out
        if abs(self.M5dataSet[-1].indicators['EMA(8)'] - self.M5dataSet[-1].indicators['EMA(13)']) > 0.00012 and \
        abs(self.M5dataSet[-1].indicators['EMA(13)'] - self.M5dataSet[-1].indicators['EMA(21)']) > 0.00012:
            # See if it's above the candlestick
            if currentCandle.high < self.M5dataSet[-1].indicators['EMA(8)'] < self.M5dataSet[-1].indicators['EMA(13)'] \
                    < self.M5dataSet[-1].indicators['EMA(21)']:
                backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "RED", text='')
                return 'short'

            # See of it's below the candlestick
            elif currentCandle.low > self.M5dataSet[-1].indicators['EMA(8)'] > self.M5dataSet[-1].indicators['EMA(13)'] \
                    > self.M5dataSet[-1].indicators['EMA(21)']:
                backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "BLUE",  text='')
                return 'long'

            else:
                return self.touchTrigger(currentCandle)

        else:
            return False





    def getM5DataSet(self):
        return self.M5dataSet