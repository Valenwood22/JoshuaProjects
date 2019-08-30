
__author__ = "Joshua Gisi, Timothy Alexander"
__copyright__ = "Copyright 2019, Project Money Tree"
__version__ = "treasureMap"
__email__ = "TJEnterprises2019@gmail.com"
__status__ = "Demo"



from tkinter import *
from Companion import Companion as companion
import numpy as np


class Map:
    def __init__(self, root, data, positions):
        """
        Constructor to initiate defaults
        :param root: TKinter root
        :param data: candle data
        :param positions: buy/sell positions
        """
        npData = np.array(data)
        high = float(max(npData[...,companion.columnKey['HIGH']]))
        low = float(min(npData[...,companion.columnKey['LOW']]))
        numberOfCandles = len(data)
        heightDif = high-low
        self.padding = 50
        canvasHeight = max(720,heightDif*50000)

        self.scaleFactor = (canvasHeight / heightDif)

        frame=Frame(root)

        frame.pack(side=LEFT)

        self.purchaseInfo = []

        self.canvas=Canvas(frame,width=0,height=0,scrollregion=(0,0,max(1300,(20 + numberOfCandles*10)),max(900,(self.padding + 20 + heightDif*50000))))

        hbar=Scrollbar(frame,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command=self.canvas.xview)
        vbar=Scrollbar(frame,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=self.canvas.yview)

        self.canvas.config(width=1200,height=720, bg='#6393a6')
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

        self.selectionList = []
        self.addCandleStick(self.canvas, data, high, positions)
        self.pointerHigh = None
        self.pointerLow = None

        self.canvas.bind("<1>", lambda event, data=data: self.leftClickOnCanvas(event, data))
        self.canvas.pack(side=LEFT, expand=True, fill=BOTH)
        print(self.purchaseInfo)








    def leftClickOnCanvas(self, evt, data):
        """
        Handles left click events on the canvas to select candles and orders
        :param evt:
        :param data: candle data
        :return:
        """
        xClick = self.canvas.canvasx(evt.x)
        yClick = self.canvas.canvasy(evt.y)

        for purchaseRow in self.purchaseInfo:
            if (purchaseRow['ButtonDataOpen'][0] <= xClick <= purchaseRow['ButtonDataOpen'][2] and purchaseRow['ButtonDataOpen'][1] <= yClick <= purchaseRow['ButtonDataOpen'][3]) or (purchaseRow['ButtonDataClose'][0] <= xClick <= purchaseRow['ButtonDataClose'][2] and purchaseRow['ButtonDataClose'][1] <= yClick <= purchaseRow['ButtonDataClose'][3]):
                info =( "PIPS " +'\t\t' + str( round(((purchaseRow['candleDataClose'][2] - purchaseRow['candleDataOpen'][2]) *1000),3))+ "\n" +
                        "Position" + '\t\t' + str(purchaseRow['pos']) + "\n" +
                        "Buy Price" +'\t' + str(purchaseRow['candleDataOpen'][2])+ "\n" +
                        "Sell Price" + '\t\t' + str(purchaseRow['candleDataClose'][2]) + "\n"
                        )


                Label(self.canvas, text=info, justify=LEFT, bg='#dce4f2').place(x=230, y=15)

                try: self.canvas.delete(self.pointerHigh); self.canvas.delete(self.pointerLow)
                except: pass
                self.pointerHigh = self.canvas.create_polygon([purchaseRow['selectionCoordsOpen'][0], purchaseRow['selectionCoordsOpen'][2] - 17,
                                                               purchaseRow['selectionCoordsOpen'][0] - 5, purchaseRow['selectionCoordsOpen'][2] - 27,
                                                               purchaseRow['selectionCoordsOpen'][0] + 5, purchaseRow['selectionCoordsOpen'][2] - 27], fill='#2F4F4F')

                self.pointerLow = self.canvas.create_polygon([purchaseRow['selectionCoordsClose'][0], purchaseRow['selectionCoordsClose'][2] - 17,
                                                               purchaseRow['selectionCoordsClose'][0] - 5, purchaseRow['selectionCoordsClose'][2] - 27,
                                                               purchaseRow['selectionCoordsClose'][0] + 5, purchaseRow['selectionCoordsClose'][2] - 27],
                                                             fill='#2F4F4F')
                return None




        i = int((min([row[0] for row in self.selectionList], key=lambda x:abs(x - xClick)) / 10) - 1)
        if self.selectionList[i][2] < yClick < self.selectionList[i][3]:

            info = ("PID     " +'\t\t' + str(data[i][companion.columnKey['PID']] )+ "\n" +
                    "DATETIME"+'\t' + str(data[i][companion.columnKey['DATETIME']]) + "\n" +
                    "OPEN    " +'\t\t' + str(data[i][companion.columnKey['OPEN']]) + "\n" +
                    "HIGH    "+'\t\t' + str(data[i][companion.columnKey['HIGH']] )+ "\n" +
                    "LOW     "+'\t\t' + str(data[i][companion.columnKey['LOW']]) + "\n" +
                    "CLOSE   "+'\t\t' + str(data[i][companion.columnKey['CLOSE']]) + "\n" +
                    "VOLUME  "+'\t' + str(data[i][companion.columnKey['VOLUME']]) + "\n" +
                    "GENERATED"+'\t' + str(data[i][companion.columnKey['GENERATED']]) )

            Label(self.canvas, text=info, justify= LEFT, bg='#dce4f2' ).place(x=15, y=15)
            #self.selectionList = [incCandle, o, h, l, c]

            try: self.canvas.delete(self.pointerHigh); self.canvas.delete(self.pointerLow)
            except: pass
            self.pointerHigh = self.canvas.create_polygon([ self.selectionList[i][0], self.selectionList[i][2] - 7,
                                         self.selectionList[i][0] - 5, self.selectionList[i][2] - 17,
                                          self.selectionList[i][0] + 5, self.selectionList[i][2] - 17 ], fill='#2F4F4F')

            self.pointerLow = self.canvas.create_polygon([self.selectionList[i][0], self.selectionList[i][3] + 7,
                                                           self.selectionList[i][0] - 5, self.selectionList[i][3] + 17,
                                                           self.selectionList[i][0] + 5, self.selectionList[i][3] + 17],
                                                          fill='#2F4F4F')







    def addCandleStick(self, canvas, data, high, positions):
        """
        A method to add a single candle stick
        :param canvas: The canvas to add it to
        :param data: basic candle stick data
        :param high: the highest pixel on the chart
        :param positions: whether an order was created at this candle stick
        :return:
        """
        incCandle = 10
        i=0
        currPositionIndex = 0
        for row in data:
            o = self.padding + (self.scaleFactor * (high - row[companion.columnKey['OPEN']]))
            h = self.padding + (self.scaleFactor * (high - row[companion.columnKey['HIGH']]))
            l = self.padding + (self.scaleFactor * (high - row[companion.columnKey['LOW']]))
            c = self.padding + (self.scaleFactor * (high - row[companion.columnKey['CLOSE']]))
            if o>c: fillColor = "#4c7c20" # bull
            else: fillColor = "#dce4f2"   # bear
            canvas.create_line(incCandle, h, incCandle, l)
            canvas.create_rectangle(incCandle-3, o, incCandle+3, c, fill=fillColor)

            self.selectionList.append([incCandle, o, h, l, c])

            if row[companion.columnKey['GENERATED']] == 1:
                self.markAsGenerated(incCandle,l+10,2.5,canvas)


            if currPositionIndex < len(positions):
                if row[companion.columnKey['DATETIME']] == positions[currPositionIndex]['openPos']:
                    self.purchaseInfo.append({'pos': positions[currPositionIndex]['pos'],'candleDataOpen': row, 'selectionCoordsOpen': self.selectionList[-1]})
                    self.markOpen(incCandle,h-10,4,canvas)

                if row[companion.columnKey['DATETIME']] == positions[currPositionIndex]['closePos']:
                    self.purchaseInfo[-1]['candleDataClose'] = row
                    self.purchaseInfo[-1]['selectionCoordsClose'] = self.selectionList[-1]
                    self.markClose(incCandle,h-10,4,canvas, self.purchaseInfo[-1]['selectionCoordsOpen'])
                    currPositionIndex += 1

            incCandle += 10
            i+=1







    def markOpen(self, x, y, r, canvas):
        """
        Draws a dot on top of the beginning of an open position
        :param x: pixel to draw at on x-axis
        :param y: pixel to draw at on y-axis
        :param r: radius of circle
        :param canvas: canvas to draw on
        :return:
        """
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        self.purchaseInfo[-1]['ButtonDataOpen'] = [x0, y0, x1, y1]
        canvas.create_oval(x0, y0, x1, y1, fill='YELLOW')







    def markClose(self, x, y, r, canvas, selectionListRef):
        """
        Draws a dot on top of a close position
        :param x: pixel to draw at on x-axis
        :param y: pixel to draw at on y-axis
        :param r: radius of circle
        :param canvas: canvas to draw on
        :param selectionListRef: Creates a line from open to close to help visualize the trade
        :return:
        """
        # self.selectionList = [incCandle, o, h, l, c]
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        self.purchaseInfo[-1]['ButtonDataClose'] = [x0, y0, x1, y1]
        canvas.create_line( selectionListRef[0]-3, selectionListRef[1],  self.selectionList[-1][0]-3, self.selectionList[-1][1])
        canvas.create_oval(x0, y0, x1, y1, fill='ORANGE')



    def markAsGenerated(self, x, y, r, canvas): #center coordinates, radius
        """
        Marks a dirty candle stick as the back testing data has a few holes
        :param x: pixel to draw at on x-axis
        :param y: pixel to draw at on y-axis
        :param r: radius of circle
        :param canvas: canvas to draw on
        :return:
        """
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        canvas.create_oval(x0, y0, x1, y1, fill='BLACK')





if __name__ == '__main__':
    root=Tk()

    Data = companion("C:\\Users\\Administrator\\Desktop\\BackTestData.db")
    dataSet = Data.getDataByDatetime("EUR_USD", printReturn=False, startDatetime='2009-01-05 19:00:00',
                                     endDatetime='2009-01-06 02:00:00')

    Map(root, dataSet, [{'openPos':'2009-01-05 19:32:00', 'closePos':'2009-01-05 20:06:00','pos':'long'},
                        {'openPos':'2009-01-05 20:07:00', 'closePos':'2009-01-05 20:27:00','pos':'long'}])

    root.mainloop()
    Data.closeConnection()


# Setup example
'''
from tkinter import *
import treasureMap
from sqlForest import sqlCompanion as companion

root=Tk()

Data = companion("C:\\Users\\Administrator\\Desktop\\BackTestData.db")
dataSet = Data.getDataByDatetime("EUR_USD", printReturn=False, startDatetime='2009-01-05 19:00:00',
                                 endDatetime='2009-01-06 02:00:00')

treasureMap.Map(root, dataSet, [{'openPos':'2009-01-05 19:32:00', 'closePos':'2009-01-05 20:06:00','pos':'long'},
                    {'openPos':'2009-01-05 20:07:00', 'closePos':'2009-01-05 20:27:00','pos':'long'}])

root.mainloop()
Data.closeConnection()
'''

