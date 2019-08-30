__author__ = "Joshua Gisi, Timothy Alexander"
__copyright__ = "Copyright 2019, Project Money Tree"
__version__ = "1.0.0"
__email__ = "TJEnterprises2019@gmail.com"
__status__ = "Demo"

import sqlite3


class Companion:
    # Global column key that corresponds to each row of the sql data base
    columnKey = {'PID': 0, 'DATETIME': 1, 'OPEN': 2, 'HIGH': 3, 'LOW': 4, 'CLOSE': 5, 'VOLUME': 6, 'GENERATED': 7}

    def __init__(self, databasePath):
        """
        Initiate connection to the database
        :param databasePath: The file path to the database
        """
        self.databasePath = databasePath
        self.connection = sqlite3.connect(self.databasePath)
        self.cursor = self.connection.cursor()







    def getDataInRange(self, tableName, printReturn=False, columns=None, granularity='M1', startPID=1, endPID=2):
        """
        Returns all the columns from the database in range of the specified PID's. Also used in other methods to
        get rows by datetime
        :param tableName: Which table to query from ie. EURUSD, EURGBP ect..
        :param printReturn: Whether or not to print the resulting rows
        :param columns: An array representing which columns to print ie. PID, OPEN, CLOSE, ect...
        :param granularity: The time frame of the candles ie. M1, M15
        :param startPID: The PID is the index of the table row 1 has a PID of 1
        :param endPID: The PID where the query stops
        :return: A matrix representing the chosen candlesticks in the database
        """
        dataset = []
        if granularity == 'M1':  # Get M1 candles by executing a SQL Select command
            for rowPID in range(startPID, endPID + 1):  # Only one row is selected at a time because of the limited memory on Digital Ocean
                self.cursor.execute('SELECT ' + self.__formatColumns(columns) + ' FROM ' + tableName + ' WHERE PID=' + str(rowPID))
                row = self.cursor.fetchall()[0]
                dataset.append(row)
                if printReturn:
                    print(row)
            return dataset

        elif granularity == 'M15':  # Get M15 candles by executing a SQL select command
            i = 0
            o = -1
            h = -1
            l = 100000000
            c = -1
            v = 0
            pid = -1
            datetime = 'NULL'
            for rowPID in range(startPID, endPID + 1):  # Convert M1 candles to M15 candles
                i += 1
                self.cursor.execute('SELECT * FROM ' + tableName + ' WHERE PID=' + str(rowPID))
                row = self.cursor.fetchall()[0]

                if i == 1:
                    o = row[self.columnKey['OPEN']]
                    pid = row[self.columnKey['PID']]
                    datetime = row[self.columnKey['DATETIME']]
                if row[self.columnKey['HIGH']] > h: h = row[self.columnKey['HIGH']]
                if row[self.columnKey['LOW']] < l: l = row[self.columnKey['LOW']]
                if i == 15: c = row[self.columnKey['CLOSE']]
                v += row[self.columnKey['VOLUME']]

                if i >= 15:
                    rowM15 = []
                    for colSelection in columns:    # Select columns based on the specified column set
                        if colSelection == 'PID':
                            rowM15.append(pid)
                        elif colSelection == 'DATETIME':
                            rowM15.append(datetime)
                        elif colSelection == 'OPEN':
                            rowM15.append(o)
                        elif colSelection == 'HIGH':
                            rowM15.append(h)
                        elif colSelection == 'LOW':
                            rowM15.append(l)
                        elif colSelection == 'CLOSE':
                            rowM15.append(c)
                        elif colSelection == 'VOLUME':
                            rowM15.append(v)
                        else:
                            print("INVALID COLUMN NAME")
                    i = 0
                    o = -1
                    h = -1
                    l = 100000000
                    c = -1
                    v = 0
                    dataset.append(rowM15)
                    if printReturn:
                        print(rowM15)

            return dataset

        else:
            return "Invalid Granularity: Choose (M1, M15)"







    def getDataAll(self, tableName, granularity='M1', printReturn=False, columns=None):
        """
        Gets all the rows in a database table ie. EURUSD, EURGBP ect..
        :param tableName: Which table to query from
        :param granularity: The time frame of the candles ie. M1, M15
        :param printReturn: Whether or not to print the resulting rows
        :param columns: An array representing which columns to print ie. PID, OPEN, CLOSE, ect...
        :return: A matrix representing all candlesticks in the database
        """
        self.cursor.execute('SELECT MAX(PID) FROM ' + tableName)
        largestPID = self.cursor.fetchall()[0][0]
        return self.getDataInRange(tableName, printReturn=printReturn, granularity=granularity, columns=columns, endPID=largestPID)







    def getDataByDatetime(self, tableName, startDatetime, endDatetime, granularity='M1', columns=None, printReturn=False):
        """
        Returns all the columns from the database in range of the specified datetime. the datetime parameter can either be a
        String or a datetime object
        :param tableName: Which table to query from ie. EURUSD, EURGBP ect..
        :param startDatetime: A string or a datetime object that specifies where the query should start
        :param endDatetime: A string or a datetime object that specifies where the query should end
        :param granularity: The time frame of the candles ie. M1, M15
        :param columns: An array representing which columns to print ie. PID, OPEN, CLOSE, ect...
        :param printReturn: Whether or not to print the resulting rows
        :return:
        """
        # checks if a datetime object was passed as a parameter if so converts to a string
        startDatetime, endDatetime = self.__formatDatetimeType(startDatetime, endDatetime)
        # Find the start datetime with the corresponding PID
        self.cursor.execute('SELECT PID FROM ' + tableName + ' WHERE DATETIME= "' + startDatetime + '"')
        startPID = self.cursor.fetchall()[0][0]
        # Find the end datetime with the corresponding PID
        self.cursor.execute('SELECT PID FROM ' + tableName + ' WHERE DATETIME= "' + endDatetime + '"')
        endPID = self.cursor.fetchall()[0][0]
        return self.getDataInRange(tableName, printReturn=printReturn, granularity=granularity, columns=columns, startPID=startPID, endPID=endPID)






    @staticmethod
    def __formatDatetimeType(start, end):
        """
        A private method to convert a datetime object to a string
        :param start: Start datetime
        :param end: End datetime
        :return: A start and end datetime string
        """
        if not isinstance(start, str):
            startStr = start.strftime("%Y-%m-%d %H:%M:%S")
        else:
            startStr = start
        if not isinstance(end, str):
            endStr = end.strftime("%Y-%m-%d %H:%M:%S")
        else:
            endStr = end

        return startStr, endStr







    @staticmethod
    def __formatColumns(columns):
        """
        Formats the selected columns parameter for the select queries from a Python list to SQL
        :param columns: An array of columns to format
        :return: A string of names separated by commas ie. ['OPEN', 'High', 'Low'] -> "Open, High, Low"
        """
        if not columns:
            return '*'
        temp = ''
        for c in columns:
            temp += c + ", "
        return temp[:-2]







    def closeConnection(self):
        """
        Closes the connection to the database
        :return:
        """
        self.connection.close()


'''
Examples
import Companion

# Initiate companion object
Data = Companion.Companion("C:\\Users\\Administrator\\Desktop\\BackTestData.db")

# Get M1 candles within datetime range
dataSet = Data.getDataByDatetime("EUR_USD",printReturn=True, startDatetime='2007-01-03 02:00:00', endDatetime='2007-01-03 04:00:00', 
                                    columns=['DATETIME','OPEN','HIGH','LOW','CLOSE'])

# Get M15 candles within datetime range
dataSet2 = Data.getDataByDatetime("EUR_USD",printReturn=True, granularity='M15', startDatetime='2006-01-03 02:00:00', 
                                    endDatetime='2006-01-03 02:29:00')

# Gets all candles from database
Data.getDataAll('EUR_USD', granularity='M15', printReturn=True)

# Gets data in PID range
Dataset = Data.getDataInRange("EUR_USD", startPID=200, endPID=250, printReturn=True, granularity='M15')

# Close connection
Data.closeConnection()
'''
