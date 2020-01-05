class condition:
    def __init__(self, backtestRef=None):
        print("Setting up")
        pass


    def run(self, currentCandle, candlesUpToCurrent):
        print(currentCandle.datetime)
        return True