from HistoryAnalysis import backTest

class condition:
    def __init__(self, backtestRef=None):
        self.backtest = backtestRef
        self.sl = -1
        self.breakEven = -1
        self.openPrice = -1
        self.buyOrders = []
        self.state = "Part1"
        self.moneyInTrade = 0



    def run(self, currentCandle, candlesUpToCurrent, position):
        # STATE 1
        if position == 'long' and self.state == 'Part1':
            if currentCandle.high >= self.breakEven:
                self.moneyInTrade = self.getMoneyToRisk()
                self.updateMoney(self.breakEven, position, self.moneyInTrade, self.openPrice, self.state, currentCandle)
                self.state = 'Part1'
                self.sl = self.openPrice + 0.0001
                self.openPrice = self.breakEven
                self.tp = self.openPrice + (2*self.risk)
                backTest.addHorizontalLine(self.backtest, currentCandle.datetime, "Horizontal At Price", price=self.tp)
                backTest.addHorizontalLine(self.backtest, currentCandle.datetime, "Horizontal At Price", price=self.sl)
                return True

            elif currentCandle.low <= self.sl:
                self.moneyInTrade = self.getMoneyToRisk()
                self.updateMoney(self.sl, position, self.moneyInTrade, self.openPrice, self.state, currentCandle)
                return True

        elif position == 'short' and self.state == 'Part1':
            if currentCandle.low <= self.breakEven:
                self.moneyInTrade = self.getMoneyToRisk()
                self.updateMoney(self.breakEven, position, self.moneyInTrade, self.openPrice, self.state, currentCandle)
                self.state = 'Part1'
                self.sl = self.openPrice - 0.0001
                self.openPrice = self.breakEven
                self.tp = self.openPrice - (2*self.risk)
                backTest.addHorizontalLine(self.backtest, currentCandle.datetime, "Horizontal At Price", price=self.tp)
                backTest.addHorizontalLine(self.backtest, currentCandle.datetime, "Horizontal At Price", price=self.sl)
                return True

            elif currentCandle.high >= self.sl:
                self.moneyInTrade = self.getMoneyToRisk()
                self.updateMoney(self.sl, position, self.moneyInTrade, self.openPrice, self.state, currentCandle)
                return True







        # STATE 2
        if position == 'long' and self.state == 'Part2':
            if currentCandle.high >= self.tp:
                self.updateMoney(self.tp, position, self.moneyInTrade/2, self.openPrice, self.state, currentCandle, fee=False)
                self.state = 'Part1'
                return True

            elif currentCandle.low <= self.sl:
                self.updateMoney(self.sl, position, self.moneyInTrade/2, self.openPrice, self.state, currentCandle, fee=False)
                self.state = 'Part1'
                return True

        elif position == 'short' and self.state == 'Part2':
            if currentCandle.low <= self.tp:
                self.updateMoney(self.tp, position, self.moneyInTrade/2, self.openPrice, self.state, currentCandle, fee=False)
                self.state = 'Part1'
                return True

            elif currentCandle.high >= self.sl:
                self.updateMoney(self.sl, position, self.moneyInTrade/2, self.openPrice, self.state, currentCandle, fee=False)
                self.state = 'Part1'
                return True







    def setup(self, currentCandle, candlesUpToCurrent,  position):
        print('================================================================================')
        self.risk = (currentCandle.indicators['ATR(14)'] * 1.5)
        if position == 'long':
            self.sl = currentCandle.close - self.risk
            backTest.addHorizontalLine(self.backtest, currentCandle.datetime, "Horizontal At Price", price=self.sl)
            self.breakEven = currentCandle.close + self.risk
            self.openPrice = currentCandle.close
            backTest.addHorizontalLine(self.backtest, currentCandle.datetime, "Horizontal At Price", price=self.breakEven)
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "magenta", text=f"BE{round(self.breakEven,6)}\nSl{round(self.sl,6)}")



        elif position == 'short':
            self.sl = currentCandle.close + self.risk
            backTest.addHorizontalLine(self.backtest, currentCandle.datetime, "Horizontal At Price", price=self.sl)
            self.breakEven = currentCandle.close - self.risk
            self.openPrice = currentCandle.close
            backTest.addHorizontalLine(self.backtest, currentCandle.datetime, "Horizontal At Price", price=self.breakEven)
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", "magenta", text=f"BE{round(self.breakEven, 6)}\nSl{round(self.sl, 6)}")




    def findNewSL(self, candlesUpToCurrent, position, currentCandle):
        if position == 'long':
            pass

        elif position == 'short':
            pass







    def getMoneyToRisk(self):
        maxMoney = self.backtest.money * self.backtest.leverage
        # print(f"Max Risk {(maxMoney / self.backtest.leverage) * self.backtest.risk} Max gain/loss {abs(((self.sl - self.openPrice) * maxMoney) / self.openPrice)}")
        if ((maxMoney / self.backtest.leverage) * self.backtest.risk) < abs(((self.sl - self.openPrice) * maxMoney) / self.openPrice):
            return abs((((maxMoney / self.backtest.leverage) * self.backtest.risk) * self.openPrice) / (self.sl - self.openPrice))

        else:
            return self.backtest.money * self.backtest.leverage




    def updateMoney(self, closePrice, position, amountMoney, openPrice, state, curCandle, fee=True):
        self.backtest.purchases[-1]['closePrice'] = closePrice
        self.backtest.purchases[-1]['closeDT'] = curCandle.datetime
        self.moneyInTrade = amountMoney
        if position == 'long':
            if fee:
                moneyChange = (closePrice - openPrice - 0.0001) * amountMoney / openPrice
                self.backtest.money += moneyChange
                print(
                   f"Total {self.backtest.money: <8.3f} Change in pips {(closePrice - openPrice - 0.0001) * 10000: <12.7f} Open Price {openPrice: <9.7} Close Price {closePrice: <9.7} Percent being riksed {round(((amountMoney/self.backtest.leverage) / self.backtest.money),4)} {amountMoney}")
            else:
                moneyChange = (closePrice - openPrice) * amountMoney / openPrice
                self.backtest.money += moneyChange
                print(
                   f"Total {self.backtest.money: <8.3f} Change in pips {(closePrice - openPrice) * 10000: <12.7f} Open Price {openPrice: <9.7} Close Price {closePrice: <9.7} Percent being riksed {round(((amountMoney/self.backtest.leverage) / self.backtest.money),4)} {amountMoney}")

            self.buyOrders.append(closePrice - openPrice - 0.0001)


        else:
            if fee:
                moneyChange = (openPrice - closePrice - 0.0001) * amountMoney / openPrice
                self.backtest.money += moneyChange
                print(f"Total {self.backtest.money: <8.3f} Change in pips {(openPrice - closePrice - 0.0001) * 10000: <12.7f} Open Price {openPrice: <9.7} Close Price {closePrice: <9.7} Percent being riksed {round(((amountMoney/self.backtest.leverage) / self.backtest.money),4)} {amountMoney}")
            else:
                moneyChange = (openPrice - closePrice) * amountMoney / openPrice
                self.backtest.money += moneyChange
                print(f"Total {self.backtest.money: <8.3f} Change in pips {(openPrice - closePrice) * 10000: <12.7f} Open Price {openPrice: <9.7} Close Price {closePrice: <9.7} Percent being riksed {round(((amountMoney/self.backtest.leverage) / self.backtest.money),4)} {amountMoney}")

            self.buyOrders.append(openPrice - closePrice - 0.0001)
