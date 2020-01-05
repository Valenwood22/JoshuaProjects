class condition:
    def __init__(self, backtestRef=None):
        self.backtest = backtestRef
        self.flag = True
        self.hi = float('-inf')
        self.lo = float('inf')
        self.reset = False
        self.lock = True
        self.rangingCandles = []
        pass


    def run(self, currentCandle, candlesUpToCurrent):
        from HistoryAnalysis import backTest
        time = currentCandle.datetime.split(':')
        hour = int(time[0][-2:])
        min = int(time[1])


        if hour == 8 and min >= 0 and self.flag:
            self.flag = False
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", color="Yellow")
            backTest.addHorizontalLine(self.backtest, currentCandle.datetime, "Horizontal At Price", price=self.hi)
            backTest.addHorizontalLine(self.backtest, currentCandle.datetime, "Horizontal At Price", price=self.lo)
            self.wasRanging = self.calculateTrendingIndex(self.rangingCandles)
            self.reset = True


        # Sleeping
        if 0 <= hour < 3:
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", color="White")
            self.updateHiLo(currentCandle)
            self.rangingCandles.append(currentCandle)

        # London
        elif 3 <= hour < 8:
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", color="Green")
            #return self.openPos(currentCandle)
            self.updateHiLo(currentCandle)
            self.rangingCandles.append(currentCandle)

        # Overlap
        elif 8 <= hour < 12:
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", color="Brown")
            return self.openPos(currentCandle)

        # United States
        elif 12 <= hour < 17:
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", color="Red")
            #return self.openPos(currentCandle)
            #self.updateHiLo(currentCandle)

        # Sleeping
        elif 17 <= hour:
            backTest.addMarker(self.backtest, currentCandle.datetime, "Simple Mark Above", color="White")
            self.updateHiLo(currentCandle)
            self.rangingCandles.append(currentCandle)
        else:
            print("INVALID CANDLE")




        # Reset Flag
        if hour >= 17:
            self.flag = True


    def updateHiLo(self, currentCandle):
        if self.reset:
            self.rangingCandles.clear()
            self.hi = float('-inf')
            self.lo = float('inf')
            self.reset = False
            self.lock = True

        self.hi = max(self.hi, currentCandle.high)
        self.lo = min(self.lo, currentCandle.low)



    def openPos(self, currentCandle):
        if self.wasRanging < 14:
            if currentCandle.open <= self.lo and self.lock:
                self.lock = False
                return "short"
            elif currentCandle.open >= self.hi and self.lock:
                self.lock = False
                return "long"


    def calculateTrendingIndex(self, candles):

        high = float("-inf")
        low = float("inf")
        absTotal = 0
        for i, c in enumerate(candles):      
            if i < 60:
                absTotal += abs(c.high-c.low)
                if c.high > high: high = c.high
                if c.low < low: low = c.low
            else:
                break

        overallTotal = high - low

        if(absTotal != 0): return(100*overallTotal/absTotal)
        else: return(0)