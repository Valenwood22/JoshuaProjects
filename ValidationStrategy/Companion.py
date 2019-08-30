
__author__ = "Joshua Gisi, Timothy Alexander"
__copyright__ = "Copyright 2019, Project Money Tree"
__version__ = "1.0.0"
__email__ = "TJEnterprises2019@gmail.com"
__status__ = "Demo"



import sqlite3



class Companion:
    # Global column key
    columnKey = {'PID':0, 'DATETIME':1, 'OPEN':2, 'HIGH':3, 'LOW':4, 'CLOSE':5, 'VOLUME':6, 'GENERATED':7}

    def __init__(self, databasePath):
        """
        Initiate connection to the database
        :param databasePath: The filepath to the database
        """
        self.databasePath = databasePath
        self.connection = sqlite3.connect(self.databasePath)
        self.cursor = self.connection.cursor()







    def getDataInRange(self, tableName, printReturn=False, columns=None, granularity='M1', startPID=1, endPID=2):
        """

        :param tableName:
        :param printReturn:
        :param columns:
        :param granularity:
        :param startPID:
        :param endPID:
        :return:
        """
        dataset = []
        if granularity == 'M1':
            for rowPID in range(startPID, endPID+1):
                self.cursor.execute('SELECT ' + self.__formatColumns(columns) + ' FROM ' + tableName + ' WHERE PID=' + str(rowPID))
                row = self.cursor.fetchall()[0]
                dataset.append(row)
                if printReturn:
                    print(row)
            return dataset

        elif granularity == 'M15':
            i = 0
            o = -1
            h = -1
            l = 100000000
            c = -1
            v = 0
            pid = -1
            datetime = 'NULL'
            for rowPID in range(startPID, endPID+1):
                i += 1
                self.cursor.execute('SELECT * FROM ' + tableName + ' WHERE PID=' + str(rowPID))
                row = self.cursor.fetchall()[0]

                if i==1:
                    o=row[self.columnKey['OPEN']]
                    pid=row[self.columnKey['PID']]
                    datetime=row[self.columnKey['DATETIME']]
                if row[self.columnKey['HIGH']] > h: h=row[self.columnKey['HIGH']]
                if row[self.columnKey['LOW']] < l: l=row[self.columnKey['LOW']]
                if i==15: c=row[self.columnKey['CLOSE']]
                v+=row[self.columnKey['VOLUME']]

                if i >= 15:
                    rowM15 = []
                    for colSelection in columns:
                        if colSelection == 'PID': rowM15.append(pid)
                        elif colSelection == 'DATETIME': rowM15.append(datetime)
                        elif colSelection == 'OPEN': rowM15.append(o)
                        elif colSelection == 'HIGH': rowM15.append(h)
                        elif colSelection == 'LOW': rowM15.append(l)
                        elif colSelection == 'CLOSE': rowM15.append(c)
                        elif colSelection == 'VOLUME': rowM15.append(v)
                        else: print("INVALID COLUMN NAME")
                    i=0
                    o=-1
                    h = -1
                    l = 100000000
                    c=-1
                    v=0
                    dataset.append(rowM15)
                    if printReturn:
                        print(rowM15)

            return dataset

        else:
            return "Invalid Granularity: Choose (M1, M15)"







    def getDataAll(self, tableName, granularity='M1', printReturn=False, columns=None):
        self.cursor.execute('SELECT MAX(PID) FROM ' + tableName)
        largestPID = self.cursor.fetchall()[0][0]
        return self.getDataInRange(tableName, printReturn=printReturn, granularity=granularity, columns=columns, endPID=largestPID)







    def getDataByDatetime(self, tableName, startDatetime, endDatetime, granularity='M1', columns=None, printReturn=False):
        startDatetime, endDatetime = self.__formatDatetimeType(startDatetime,endDatetime)
        self.cursor.execute('SELECT PID FROM ' + tableName + ' WHERE DATETIME= "' + startDatetime+'"')
        startPID = self.cursor.fetchall()[0][0]
        self.cursor.execute('SELECT PID FROM ' + tableName + ' WHERE DATETIME= "' + endDatetime+'"')
        endPID = self.cursor.fetchall()[0][0]
        return self.getDataInRange(tableName, printReturn=printReturn, granularity=granularity, columns=columns, startPID=startPID, endPID=endPID)







    def __formatDatetimeType(self, start, end):
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
        if not columns:
            return '*'
        temp = ''
        for c in columns:
            temp += c + ", "
        return temp[:-2]







    def closeConnection(self):
        self.connection.close()




'''
examples
Data = sqlForest.sqlCompanion("C:\\Users\\Administrator\\Desktop\\BackTestData.db")

dataSet = Data.getDataByDatetime("EUR_USD",printReturn=True, startDatetime='2007-01-03 02:00:00', endDatetime='2007-01-03 04:00:00', columns=['DATETIME','OPEN','HIGH','LOW','CLOSE'])


print('=========')

dataSet2 = Data.getDataByDatetime("EUR_USD",printReturn=True, granularity='M15', startDatetime='2006-01-03 02:00:00', endDatetime='2006-01-03 02:29:00')


Data.getDataAll('EUR_USD', granularity='M15', printReturn=True)

Dataset = Data.getDataInRange("EUR_USD", startPID=200, endPID=250, printReturn=True, granularity='M15')


Data.closeConnection()
'''











