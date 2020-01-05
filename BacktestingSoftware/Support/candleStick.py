
__authors__ = "Joshua Gisi"
__copyright__ = "Copyright 2019, Project Money Tree"
__version__ = "0.0.1"
__email__ = "TJEnterprises2019@gmail.com"
__status__ = "Development"


class candle:

    def __init__(self, pid, datetime, open, high, low, close, volume, generated=None, indicators=None):
        """
        Initiate a cnadle object
        :param pid: ID of the candle from the sql database
        :param datetime: Date time of the candle
        :param open: Open price of the candle
        :param high: High of the candle
        :param low: Low of the candle
        :param close: Close of the candle
        :param volume: Volume of the candle
        :param generated: Whether the candle was generated to help fill in blank spaces
        :param indicators: A dictionary of indicators
        """
        if indicators is None:
            indicators = {}
        self.pid = pid
        self.datetime = datetime
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.generated = generated
        self.indicators = indicators


    def __str__(self) -> str:
        """
        Format candle
        :return:
        """
        return f"{self.datetime} \t O {self.open} H {self.high} L {self.low} C {self.close} V {self.volume} \t\t Indicators {self.indicators}"
