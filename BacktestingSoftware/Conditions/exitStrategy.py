
class condition:
    def __init__(self, currentCandle, TP, SL, backtestRef=None):
        self.closePrice = []
        self.stopLoss = [SL] # currentCandle.open - currentCandle.indicators['ATR(14)']
        self.takeProfit = [TP] # currentCandle.open + currentCandle.indicators['ATR(14)']
        self.closeCandle = []
        self.i = 0
        self.buyRecurtions = 2


    # continues to run until it returns false
    def run(self, currentCandle, candlesUpToCurrent):
        while self.i < self.buyRecurtions:
            if currentCandle.low <= self.stopLoss[self.i]:
                self.closePrice.append(self.stopLoss[self.i])
                self.closeCandle.append(currentCandle)
                self.i = 0
                return "break"

            elif currentCandle.high >= self.takeProfit[self.i]:
                self.closePrice.append(self.takeProfit[self.i])
                self.closeCandle.append(currentCandle)
                self.i+=1
                if self.i < self.buyRecurtions:
                    self.stopLoss.append(self.stopLoss[-1])
                    self.takeProfit.append(self.closePrice[-1] + currentCandle.indicators['ATR(14)'])
                return "update"
            else:
                return "continue"

        return "break"


