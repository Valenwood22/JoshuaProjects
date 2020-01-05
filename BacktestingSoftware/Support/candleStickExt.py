__authors__ = "Timothy Alexander, Joshua Gisi"
__copyright__ = "Copyright 2019, Project Money Tree"
__version__ = "0.0.1"
__email__ = "TJEnterprises2019@gmail.com"
__status__ = "Development"

from Support.candleStick import candle
import random

class candleExt:

    def __init__(self, candle, cost, marker, predictions, generated=None):
        self.candle = candle
        self.cost = cost
        self.marker = marker
        self.predictions = predictions
        self.generated = generated




    def calculateCost(self, candle2, scalingFactor):
        if(len(self.candle.indicators) == 0): self.cost = random.random()
        else:
            c = 0
            for k in self.candle.indicators.keys():
                temp = (self.candle.indicators[k] - candle2.candle.indicators[k]) / (scalingFactor[k])
                c += (temp * temp)

            self.cost = 1/c if c != 0 else random.random()


    def calculateScalingFactor(self, candles_past):
        scalingFactor = {}
        if(len(self.candle.indicators) == 0): return scalingFactor

        for k in self.candle.indicators.keys():
            scalingFactor[k] = 0
            for i in range(0, len(candles_past), 10):
                scalingFactor[k] += abs(self.candle.indicators[k] - candles_past[i].candle.indicators[k])

            scalingFactor[k] /= (len(candles_past) / 10)

        return scalingFactor





    def __str__(self) -> str:
        return f"{self.candle.datetime} \t O {self.candle.open} H {self.candle.high} L {self.candle.low} C {self.candle.close} V {self.candle.volume} \t Indicators {self.candle.indicators} C {self.cost} M {self.marker}  \t Predictions {self.predictions}"
