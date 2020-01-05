class condition:
    def __init__(self, backtestRef=None):
        pass


    def run(self, currentCandle, candlesUpToCurrent):
        if currentCandle.datetime == '2009-01-05 19:32:00':
            return True
        return False