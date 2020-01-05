from HistoryAnalysis import backTest

class condition:
    def __init__(self, backtestRef=None):
        self.backtest = backtestRef
        self.state = "part1"
        self.varSl = -1



    def run(self, currentCandle, candlesUpToCurrent, position):
        riskPrice = self.backtest.riskPrice
        self.sl = self.backtest.sl
        if position == 'long' and self.state == "part1":
            if currentCandle.open >= riskPrice:
                self.varSl = self.sl
                self.findNewSL(candlesUpToCurrent, position, currentCandle)
                backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "CYAN", text=f"\n\n\n\nTP Exit 50%\nNew SL: {self.varSl}")
                self.state = "part2"
                self.updateMoney(currentCandle,position,self.backtest.money, self.backtest.openPrice)
                self.newStart = currentCandle.open
                return False
            elif currentCandle.open < self.sl:
                backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "CYAN", text="Stop loss")
                self.updateMoney(currentCandle, position,self.backtest.money, self.backtest.openPrice)
                self.newStart = currentCandle.open
                return True
        elif position == 'short' and self.state == "part1":
            if currentCandle.open <= riskPrice:
                self.varSl = self.sl
                self.findNewSL(candlesUpToCurrent, position, currentCandle)
                backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "CYAN", text=f"\n\n\n\nTP Exit 50%\nNew SL: {self.varSl}")
                self.state = "part2"
                self.updateMoney(currentCandle, position,self.backtest.money, self.backtest.openPrice)
                self.newStart = currentCandle.open
                return False
            elif currentCandle.open > self.sl:
                backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "CYAN", text="Stop Loss")
                self.updateMoney(currentCandle, position,self.backtest.money, self.backtest.openPrice)
                self.newStart = currentCandle.open
                return True


        # PART 2
        if self.state == "part2":
            self.findNewSL(candlesUpToCurrent, position, currentCandle)
            if position == 'long' and currentCandle.open < self.varSl:
                backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "CYAN", text="\nEND TRADE")
                self.state = "part1"
                self.updateMoney(currentCandle, position, self.backtest.money/2, self.newStart)
                return True


            elif position == 'short' and currentCandle.open > self.varSl:
                backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "CYAN", text="\nEND TRADE")
                self.state = "part1"
                self.updateMoney(currentCandle, position, self.backtest.money/2, self.newStart)
                return True

        return False




    def findNewSL(self, candlesUpToCurrent, position, currentCandle):
        l = 1000000000000
        h = -1
        for i in range(-15,0):
            if candlesUpToCurrent[i].high > h: h = candlesUpToCurrent[i].high
            if candlesUpToCurrent[i].low < l: l = candlesUpToCurrent[i].low
        if position == 'long':
            slTemp = round(l - 0.0003,5)
            if slTemp > self.varSl:
                if slTemp != self.varSl:
                    backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "CYAN", text=f"New SL:\n{round(slTemp,5)}")
                self.varSl = slTemp

        elif position == 'short':
            slTemp = round(h + 0.0003,5)

            if slTemp < self.varSl:
                if slTemp != self.varSl:
                    backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "CYAN", text=f"New SL:\n{round(slTemp,5)}")
                self.varSl = slTemp





    def updateMoney(self, currentCandle, position, amountMoney, startPrice):
        if position == 'long':
            moneyChange = (currentCandle.open - startPrice - 0.00015) * amountMoney * self.backtest.leverage / startPrice
            self.backtest.money += moneyChange

        else:
            moneyChange = (startPrice - currentCandle.open - 0.00015) * amountMoney * self.backtest.leverage / startPrice
            self.backtest.money += moneyChange
        print(f"Total {self.backtest.money}\t  Start Price{startPrice}\t  End Price{currentCandle.open}")