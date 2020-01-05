class condition:

    def __init__(self, backtestRef=None):
        self.backtest = backtestRef
        self.pips = 10
        self.sl = -1
        self.moneyInTrade = 0
        self.openPrice = -1
        self.pipsWon = 0



    def run(self, currentCandle, candlesUpToCurrent, position):

        if position =="long":
            if currentCandle.open >= self.openPrice + 0.0012:
                self.moneyInTrade = self.getMoneyToRisk()
                self.updateMoney(self.openPrice + 0.0012, position, self.moneyInTrade, self.openPrice, "", currentCandle)
                return True

            if currentCandle.open <= self.openPrice - 0.0012:
                self.moneyInTrade = self.getMoneyToRisk()
                self.updateMoney(self.openPrice - 0.0012, position, self.moneyInTrade, self.openPrice, "", currentCandle)
                return True

        elif position == "short":
            if currentCandle.open >= self.openPrice + 0.0012:
                self.moneyInTrade = self.getMoneyToRisk()
                self.updateMoney(self.openPrice + 0.0012, position, self.moneyInTrade, self.openPrice, "", currentCandle)
                return True

            if currentCandle.open <= self.openPrice - 0.0012:
                self.moneyInTrade = self.getMoneyToRisk()
                self.updateMoney(self.openPrice - 0.0012, position, self.moneyInTrade, self.openPrice, "", currentCandle)
                return True







    def getMoneyToRisk(self):
        maxMoney = self.backtest.money * self.backtest.leverage
        return maxMoney




    def setup(self, currentCandle, candlesUpToCurrent,  position):
        self.openPrice = currentCandle.open
        pass




    def updateMoney(self, closePrice, position, amountMoney, openPrice, state, curCandle, fee=True):
        self.backtest.purchases[-1]['closePrice'] = closePrice
        self.backtest.purchases[-1]['closeDT'] = curCandle.datetime
        self.moneyInTrade = amountMoney
        if position == 'long':
            if fee:
                moneyChange = (closePrice - openPrice - 0.0001) * amountMoney / openPrice
                self.pipsWon += (closePrice - openPrice) * 10000 - 1
                print(
                   f"Total {self.backtest.money: <8.3f} Pips Won {self.pipsWon: <12.7f}  Change in pips {(closePrice - openPrice - 0.0001) * 10000: <12.7f} Open Price {openPrice: <9.7} Close Price {closePrice: <9.7} Percent being risked {round(((amountMoney/self.backtest.leverage) / self.backtest.money),4)} {amountMoney}")
                self.backtest.money += moneyChange

            else:
                moneyChange = (closePrice - openPrice) * amountMoney / openPrice
                self.pipsWon += (closePrice - openPrice) * 10000
                print(
                   f"Total {self.backtest.money: <8.3f} Pips Won {self.pipsWon: <12.7f} Change in pips {(closePrice - openPrice) * 10000: <12.7f} Open Price {openPrice: <9.7} Close Price {closePrice: <9.7} Percent being risked {round(((amountMoney/self.backtest.leverage) / self.backtest.money),4)} {amountMoney}")
                self.backtest.money += moneyChange


        else:
            if fee:
                moneyChange = (openPrice - closePrice - 0.0001) * amountMoney / openPrice
                self.pipsWon += (openPrice - closePrice) * 10000 - 1
                print(f"Total {self.backtest.money: <8.3f} Pips Won {self.pipsWon: <12.7f}  Change in pips {(openPrice - closePrice - 0.0001) * 10000: <12.7f} Open Price {openPrice: <9.7} Close Price {closePrice: <9.7} Percent being risked {round(((amountMoney/self.backtest.leverage) / self.backtest.money),4)} {amountMoney}")
                self.backtest.money += moneyChange

            else:
                moneyChange = (openPrice - closePrice) * amountMoney / openPrice
                self.pipsWon += (openPrice - closePrice) * 10000
                print(f"Total {self.backtest.money: <8.3f} Pips Won {self.pipsWon: <12.7f}  Change in pips {(openPrice - closePrice) * 10000: <12.7f} Open Price {openPrice: <9.7} Close Price {closePrice: <9.7} Percent being risked {round(((amountMoney/self.backtest.leverage) / self.backtest.money),4)} {amountMoney}")
                self.backtest.money += moneyChange