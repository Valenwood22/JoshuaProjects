from Indicators.EMA import indicator as ema
from Support.Companion import sqlCompanion
from Support import candleStick


class condition:

    def __init__(self, backtestRef=None):
        self.H1dataSet = []
        self.spreadPatternSell = 0
        self.spreadPatternBuy = 0
        self.isSpreadOut = False

        self.TREND_PATTERN = 3

    def run(self, currentCandle, candlesUpToCurrent):
        if len(candlesUpToCurrent) % 60 == 0 and len(candlesUpToCurrent) != 0:
            self.createH1Candle(candlesUpToCurrent, currentCandle)

            self.H1dataSet[-1].indicators['EMA(8)'] = ema().run(self.H1dataSet[-1], self.H1dataSet, 8)
            self.H1dataSet[-1].indicators['EMA(21)'] = ema().run(self.H1dataSet[-1], self.H1dataSet, 21)


            if abs(self.H1dataSet[-1].indicators['EMA(8)'] - self.H1dataSet[-1].indicators['EMA(21)']) > 0.0018 and \
                (currentCandle.high < self.H1dataSet[-1].indicators['EMA(8)'] < self.H1dataSet[-1].indicators['EMA(21)'] or
                 currentCandle.low > self.H1dataSet[-1].indicators['EMA(8)'] > self.H1dataSet[-1].indicators['EMA(21)']):
                if self.H1dataSet[-1].indicators['EMA(8)'] - self.H1dataSet[-1].indicators['EMA(21)'] > 0:
                    self.spreadPatternSell = 0
                    self.spreadPatternBuy += 1
                    diff = self.H1dataSet[-1].indicators['EMA(8)'] - self.H1dataSet[-1].indicators['EMA(21)']
                    self.H1dataSet[-1].indicators['info'] = f'Long {self.spreadPatternBuy}'
                else:
                    self.spreadPatternBuy = 0
                    self.spreadPatternSell += 1
                    diff = self.H1dataSet[-1].indicators['EMA(8)'] - self.H1dataSet[-1].indicators['EMA(21)']
                    self.H1dataSet[-1].indicators['info'] = f'Short {self.spreadPatternSell}'
            else:
                self.spreadPatternSell = 0
                self.spreadPatternBuy = 0
                diff = self.H1dataSet[-1].indicators['EMA(8)'] - self.H1dataSet[-1].indicators['EMA(21)']
                self.H1dataSet[-1].indicators['info'] = f'False'
                #self.H1dataSet[-1].indicators['info'] = f'False {round(diff, 6)}'



            if self.spreadPatternBuy >= self.TREND_PATTERN:
                self.isSpreadOut = 'long'
                return 'long'

            elif self.spreadPatternSell >= self.TREND_PATTERN:
                self.isSpreadOut = 'short'
                return 'short'
            else:
                self.isSpreadOut = False

        return self.isSpreadOut







    def createH1Candle(self, candlesUpToCurrent, currentCandle):
        o = candlesUpToCurrent[-60].open
        h = -1
        l = 100000000000000
        c = currentCandle.close
        v = 0
        datetime = candlesUpToCurrent[-1].datetime
        for i in range(-60, 0):
            if candlesUpToCurrent[i].high > h: h = candlesUpToCurrent[i].high
            if candlesUpToCurrent[i].low < l: l = candlesUpToCurrent[i].low
            v += candlesUpToCurrent[i].volume
        self.H1dataSet.append(candleStick.candle(0, datetime, o, h, l, c, v))






    def getH1DataSet(self):
        return self.H1dataSet
