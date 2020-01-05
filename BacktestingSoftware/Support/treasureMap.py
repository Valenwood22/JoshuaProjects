__author__ = "Joshua Gisi"
__copyright__ = "Copyright 2019, Project Money Tree"
__version__ = "1.3.4"
__email__ = "TJEnterprises2019@gmail.com"
__status__ = "Development"

import time
from tkinter import *
from Support.Companion import sqlCompanion as companion
from datetime import datetime as dt


class Map:
    def __init__(self, root, data, positions, markers=[], indicators=[]):
        """
        Create the window for the back testing software and add data
        :param root: TKinter root
        :param data: Array of candle objects, "RED"
        :param positions: Array of where positions where opened and closed
        :param markers: Array of date times and data on markers ex. {'datetime':'10-12-2018', 'type':"Simple Mark Above",
            'pipOffset': 12, 'color':"RED", 'text':"Stop Loss"}
        :param indicators: The different indicators to add to the window ex. {'name':'EMA(100)', 'color':'BLUE'}
        """

        self.markers = sorted(markers, key=lambda m: dt.strptime(m['datetime'],"%Y-%m-%d %H:%M:%S"))
        self.markers.append({'datetime': "TAIL", "type": None})

        high, low = self.findHiLo(data)     # Find the highest and lowest candle price. Used to set the diplay scale
        self.numberOfCandles = len(data)
        heightDif = high-low
        self.padding = 50
        canvasHeight = max(720, heightDif*50000)

        self.scaleFactor = (canvasHeight / heightDif)
        self.canvasHeight = max(900,(self.padding + 20 + heightDif*50000))
        self.canvasWidth = (20 + self.numberOfCandles*10)
        frame = Frame(root)

        frame.pack(side=LEFT)

        self.purchaseInfo = []

        self.canvas = Canvas(frame,width=0,height=0,scrollregion=(0,0,max(1300,self.canvasWidth),self.canvasHeight))

        hbar = Scrollbar(frame,orient=HORIZONTAL)
        hbar.bind('<ButtonRelease-1>', lambda event, data=data, high=high: self.startScrolling(event, data, high))
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command=self.canvas.xview)
        vbar = Scrollbar(frame,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=self.canvas.yview)

        self.i = 0
        bottomFrame = Frame(frame)
        prevTradeB = Button(bottomFrame, text="Prev", padx=26, command=lambda: self.prevTrade(data, high))
        prevTradeB.pack(side=LEFT, anchor='w', padx=4)
        nextTradeB = Button(bottomFrame, text="Next", padx=26, command=lambda: self.nextTrade(data, high))
        nextTradeB.pack(side=LEFT, anchor='w', padx=4)
        bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=True)


        self.canvas.config(width=1200,height=720, bg='#6393a6')
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

        self.selectionList = []
        self.addCandleStick(self.canvas, data, high, positions, indicators)
        self.pointerHigh = None
        self.pointerLow = None

        self.paintTotalPips()

        self.canvas.bind("<1>", lambda event, data=data: self.leftClickOnCanvas(event, data))
        self.canvas.bind("<3>", lambda event, data=data: self.rightClickOnCanvas(event, data, high))
        root.bind('w', lambda event, data=data: self.WinLoss(event, data, high))

        self.canvas.pack(side=LEFT, expand=True, fill=BOTH)
        self.setCanvasToStartingCandles(data,high)
        self.SLDebug = []
        self.TPDebug = []
        self.ATRsCntr = {}



    def WinLoss(self,evt, data, high):
        """
        A method to quickly test a closing strategy on all candles
        :param evt:
        :param data: Array of candle objects
        :param high: Highest candle in the data set
        :return:
        """
        for i in range(15, len(data)-1):
            openPrice = data[i].open
            from Conditions.exitStrategy import condition
            tp = data[i].open + data[i].indicators['ATR(14)']
            sl = data[i].open - data[i].indicators['ATR(14)']
            exitStrat = condition(data[i], tp, sl)
            j = i
            upToCurrent = []
            while j < len(data):
                rtrn = exitStrat.run(data[j], upToCurrent)
                if rtrn == "continue":
                    j += 1
                elif rtrn == "update":
                    j += 1
                else:
                    break

            ATRsWon = 0
            tempPriceList = exitStrat.closePrice
            tempPriceList.insert(0, openPrice)
            for k in range(1, len(tempPriceList)):
                if tempPriceList[k-1] < tempPriceList[k]:
                    ATRsWon += 1
                else:
                    ATRsWon -= 1


            if self.ATRsCntr.get(ATRsWon):
                self.ATRsCntr[ATRsWon] += 1
            else:
                self.ATRsCntr[ATRsWon] = 1
            self.simpleMarkAbove((i+1)*10, self.padding + (self.scaleFactor * (high - data[i+1].high)), 0, self.canvas, "Green", text=ATRsWon)
        print(self.ATRsCntr)






    def rightClickOnCanvas(self, evt, data, high):
        """
        A method to quickly test a closing strategy on a single candle
        :param evt:
        :param data: Array of candle objects
        :param high: Highest candle in the data set
        :return:
        """
        xClick = self.canvas.canvasx(evt.x)
        yClick = self.canvas.canvasy(evt.y)

        i = int((min([row[0] for row in self.selectionList], key=lambda x: abs(x - xClick)) / 10) - 1)

        if self.selectionList[i][2] < yClick < self.selectionList[i][3]:
            openPrice = data[i].open
            from Conditions.exitStrategy import condition
            tp = data[i].open + data[i].indicators['ATR(14)']
            sl = data[i].open - data[i].indicators['ATR(14)']
            exitStrat = condition(data[i], tp, sl)
            upToCurrent = []
            j=i

            for i in range(len(self.SLDebug)):
                self.canvas.delete(self.SLDebug[i])
                self.canvas.delete(self.TPDebug[i])

            self.SLDebug.append(self.horizonAtPrice(self.canvas, high, data[i], self.selectionList[j][0], 80, "Orange", exitStrat.stopLoss[-1]))
            self.TPDebug.append(self.horizonAtPrice(self.canvas, high, data[i], self.selectionList[j][0], 80, "Orange", exitStrat.takeProfit[-1]))

            while j < len(data):
                upToCurrent.append(data)
                rtrn = exitStrat.run(data[j], upToCurrent)
                if rtrn == "continue":
                    j += 1
                elif rtrn == "update":
                    self.SLDebug.append(self.horizonAtPrice(self.canvas, high, data[j], self.selectionList[j][0], 80, "Orange", exitStrat.stopLoss[-1]))
                    self.TPDebug.append(self.horizonAtPrice(self.canvas, high, data[j], self.selectionList[j][0], 80, "Orange", exitStrat.takeProfit[-1]))
                    j += 1
                else:
                    break

            ATRsWon = 0
            tempPriceList = exitStrat.closePrice
            tempPriceList.insert(0, openPrice)
            for i in range(1, len(tempPriceList)):
                if tempPriceList[i-1] < tempPriceList[i]:
                    ATRsWon += 1
                else:
                    ATRsWon -= 1


            try: self.canvas.delete(self.pointerLow)
            except: pass
            self.pointerLow = self.canvas.create_polygon([self.selectionList[j][0], self.selectionList[j][3] + 17,
                                                          self.selectionList[j][0] - 5, self.selectionList[j][3] + 27,
                                                          self.selectionList[j][0] + 5, self.selectionList[j][3] + 27],
                                                          fill='#FFA500')


            print("=======================================")
            print(f"ATRs won {ATRsWon} open Price {openPrice} close Price {exitStrat.closePrice[-1]}")
            print("=======================================")





    def leftClickOnCanvas(self, evt, data):
        """
        Handles the selection logic when a user wants to see the specific data on a candle stick
        :param evt:
        :param data: An array of candle objects
        :param high: Highest candle in the data set
        :return:
        """
        xClick = self.canvas.canvasx(evt.x)
        yClick = self.canvas.canvasy(evt.y)

        for purchaseRow in self.purchaseInfo:

            if (purchaseRow['ButtonDataOpen'][0] <= xClick <= purchaseRow['ButtonDataOpen'][2] and purchaseRow['ButtonDataOpen'][1] <= yClick <= purchaseRow['ButtonDataOpen'][3]) or (purchaseRow['ButtonDataClose'][0] <= xClick <= purchaseRow['ButtonDataClose'][2] and purchaseRow['ButtonDataClose'][1] <= yClick <= purchaseRow['ButtonDataClose'][3]):
                info =( "PIPS " +'\t\t' + str( round(((purchaseRow['candleData']['closePrice'] - purchaseRow['candleData']['openPrice']) *10000),3))+ "\n" +
                        "Position" + '\t\t' + str(purchaseRow['pos']) + "\n" +
                        "Buy Price" +'\t' + str(purchaseRow['candleData']['openPrice'])+ "\n" +
                        "Sell Price" + '\t\t' + str(purchaseRow['candleData']['closePrice']) + "\n"
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

            indiData = '\n'.join([f'{key:<22s} {value:<22f}' for (key, value) in data[i].indicators.items()])

            info = ("PID     " + '\t\t' + str(data[i].pid) + "\n" +
                    "DATETIME" + '\t' + str(data[i].datetime) + "\n" +
                    "OPEN    " + '\t\t' + str(data[i].open) + "\n" +
                    "HIGH    " + '\t\t' + str(data[i].high) + "\n" +
                    "LOW     " + '\t\t' + str(data[i].low) + "\n" +
                    "CLOSE   " + '\t\t' + str(data[i].close) + "\n" +
                    "VOLUME  " + '\t' + str(data[i].volume) + "\n" +
                    "GENERATED" + '\t' + str(data[i].generated) + "\n" +
                    "INDICATORS" + '\n' + indiData)

            Label(self.canvas, text=info, justify= LEFT, bg='#dce4f2' ).place(x=15, y=15)

            try: self.canvas.delete(self.pointerHigh); self.canvas.delete(self.pointerLow)
            except: pass
            self.pointerHigh = self.canvas.create_polygon([ self.selectionList[i][0], self.selectionList[i][2] - 7,
                                         self.selectionList[i][0] - 5, self.selectionList[i][2] - 17,
                                          self.selectionList[i][0] + 5, self.selectionList[i][2] - 17 ], fill='#2F4F4F')

            self.pointerLow = self.canvas.create_polygon([self.selectionList[i][0], self.selectionList[i][3] + 7,
                                                           self.selectionList[i][0] - 5, self.selectionList[i][3] + 17,
                                                           self.selectionList[i][0] + 5, self.selectionList[i][3] + 17],
                                                          fill='#2F4F4F')







    def addCandleStick(self, canvas, data, high, positions, indicators):
        """
        Logic to paint the candles onto the canvas
        :param canvas: TKinter canvas created in the __inti__ method
        :param data: An array of candle objects
        :param high: The highest candle in the array. A constant used for scaling
        :param positions: Array of where positions where opened and closed
        :param indicators: The indicators added to the
        :return:
        """
        incCandle = 10
        i = 0
        j = 0
        m = 0
        currPositionIndex = 0
        prevRow = data[0]
        for row in data:
            o = self.padding + (self.scaleFactor * (high - row.open))
            h = self.padding + (self.scaleFactor * (high - row.high))
            l = self.padding + (self.scaleFactor * (high - row.low))
            c = self.padding + (self.scaleFactor * (high - row.close))
            if o>c: fillColor = "#4c7c20" # bull
            else: fillColor = "#dce4f2"   # bear
            canvas.create_line(incCandle, h, incCandle, l)
            canvas.create_rectangle(incCandle-3, o, incCandle+3, c, fill=fillColor)

            self.selectionList.append([incCandle, o, h, l, c])

            if row.generated == 1:
                self.markAsGenerated(incCandle,l+10,2.5,canvas)

            # Handles Indicators 1
            try:
                for indi in indicators:
                    yCur = self.padding + (self.scaleFactor * (high - row.indicators[indi['name']]))  # convert to grid coords
                    yNext = self.padding + (self.scaleFactor * (high - prevRow.indicators[indi['name']]))
                    canvas.create_line(incCandle, yCur, incCandle-10, yNext, fill=indi['color'])
                    j += 1
                prevRow = row
            except:
                pass


            while row.datetime == self.markers[m]['datetime']:
                if self.markers[m]['type'] == 'Simple Mark Above':
                    self.simpleMarkAbove(incCandle, h-20, 4, canvas, self.markers[m]['color'], self.markers[m]['text'])
                elif self.markers[m]['type'] == 'Simple Horizontal Above':
                    self.horizonCenterAbove(canvas, high, row, incCandle, 250, self.markers[m]['color'], pipOffset=self.markers[m]['pipOffset'])
                elif self.markers[m]['type'] == 'Simple Horizontal Below':
                    self.horizonCenterBelow(canvas, high, row, incCandle, 250, self.markers[m]['color'], pipOffset=self.markers[m]['pipOffset'])
                elif self.markers[m]['type'] == 'Horizontal At Price':
                    self.horizonAtPrice(canvas, high, row,incCandle, 250, self.markers[m]['color'], self.markers[m]['price'])
                m += 1



            if currPositionIndex < len(positions):
                if row.datetime == positions[currPositionIndex]['openDT']:
                    self.purchaseInfo.append({'pos': positions[currPositionIndex]['pos'], 'candleData': positions[currPositionIndex], 'selectionCoordsOpen': self.selectionList[-1], })
                    self.markOpen(incCandle,h-10,4,canvas)
                try:
                    if row.datetime == positions[currPositionIndex]['closeDT']:
                        self.purchaseInfo[-1]['selectionCoordsClose'] = self.selectionList[-1]
                        self.markClose(incCandle,h-10,4,canvas, high, self.purchaseInfo[-1]['selectionCoordsOpen'], positions[currPositionIndex])
                        currPositionIndex += 1
                except:
                    pass

            incCandle += 10
            i += 1







    def paintTotalPips(self):
        """
        Calculate the pips won/lost and add it to the top right corner of the canvas
        :return:
        """
        total = 0
        totalWFee = 0
        tradesWon = 0
        tradesLost = 0
        tradesEven = 0
        for purchaseRow in self.purchaseInfo:

            if purchaseRow['pos'] == 'long':
                try:
                    total += round(((purchaseRow['candleData']['closePrice'] - purchaseRow['candleData']['openPrice']) * 10000), 3)
                    totalWFee += round(((purchaseRow['candleData']['closePrice'] - purchaseRow['candleData']['openPrice'] - 0.0001) * 10000), 3)

                    if 0 <= abs(round(((purchaseRow['candleData']['closePrice'] - purchaseRow['candleData']['openPrice'] - 0.0001) * 10000), 3)) < 0.00001: tradesEven += 1
                    elif round(((purchaseRow['candleData']['closePrice'] - purchaseRow['candleData']['openPrice']) * 10000), 3) > 0: tradesWon += 1
                    else: tradesLost += 1
                except: pass
            else:
                try:
                    total += round(((purchaseRow['candleData']['openPrice'] - purchaseRow['candleData']['closePrice']) * 10000), 3)
                    totalWFee += round(((purchaseRow['candleData']['openPrice'] - purchaseRow['candleData']['closePrice'] - 0.0001) * 10000), 3)

                    if 0 <= abs(round(((purchaseRow['candleData']['openPrice'] - purchaseRow['candleData']['closePrice'] - 0.0001) * 10000), 3)) < 0.00001: tradesEven += 1
                    elif round(((purchaseRow['candleData']['closePrice'] - purchaseRow['candleData']['openPrice']) * -10000), 3) > 0: tradesWon += 1
                    else: tradesLost += 1
                except: pass
        info = ("Total PIPs (No Fees): \t"+str(round(total,3)) + '\n' +
                "Total PIPs (1 pip Fee): \t"+str(round(totalWFee,3)) + '\n' +
                "Trades Made: \t\t" + str(len(self.purchaseInfo)) + '\n' +
                "Trades Won: \t\t" + str(tradesWon) + '\n' +
                "Trades Even: \t\t" + str(tradesEven) + '\n' +
                "Trades Lost: \t\t" + str(tradesLost))
        Label(self.canvas, text=info, justify=LEFT, bg='#dce4f2').place(x=1000, y=15)







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







    def markClose(self, x, y, r, canvas, high, selectionListRef, orders):
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
        openGridCoords = self.padding + (self.scaleFactor * (high - orders['openPrice']))
        closeGridCoords = self.padding + (self.scaleFactor * (high - orders['closePrice']))
        canvas.create_line(selectionListRef[0], openGridCoords, self.selectionList[-1][0], closeGridCoords)
        canvas.create_oval(x0, y0, x1, y1, fill='ORANGE')







    def simpleMarkAbove(self, x, y, r, canvas, color, text=None):
        """
        Draws a dot above a candle
        :param x: pixel to draw at on x-axis
        :param y: pixel to draw at on y-axis
        :param r: radius of circle
        :param canvas: canvas to draw on
        :param color: Color of the mark
        :param text: Text to add with the mark
        :return:
        """
        # self.selectionList = [incCandle, o, h, l, c]
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        canvas.create_oval(x0, y0, x1, y1, fill=color)
        if text is not None:
            canvas.create_text((x, y - 106), text=text)







    def horizonCenterAbove(self,canvas, high, candle, incCandle, length, color, pipOffset=0):
        """
        Draws a line centered above a candle
        :param canvas: Canvas to draw on
        :param high: Used for scaling
        :param candle: Candle the drw the line above
        :param incCandle: The x pixel coord of the candle
        :param length: The length of the line in pixels
        :param color: The color of the line
        :param pipOffset: How far above the candle in pips
        :return:
        """
        x1 = incCandle
        y1 = self.padding + (self.scaleFactor * (high - (candle.high + pipOffset/10000)))
        x2 = incCandle + length
        y2 = self.padding + (self.scaleFactor * (high - (candle.high + pipOffset/10000)))
        canvas.create_line(x1, y1, x2, y2, fill=color)







    def horizonCenterBelow(self,canvas, high, candle, incCandle, length, color, pipOffset=0):
        """
        Draws a line centered below a candle
        :param canvas: Canvas to draw on
        :param high: Used for scaling
        :param candle: Candle the drw the line above
        :param incCandle: The x pixel coord of the candle
        :param length: The length of the line in pixels
        :param color: The color of the line
        :param pipOffset: How far below the candle in pips
        :return:
        """
        x1 = incCandle
        y1 = self.padding + (self.scaleFactor * (high - (candle.low - pipOffset/10000)))
        x2 = incCandle + length
        y2 = self.padding + (self.scaleFactor * (high - (candle.low - pipOffset/10000)))
        canvas.create_line(x1, y1, x2, y2, fill=color)






    def horizonAtPrice(self,canvas, high, candle, incCandle, length, color, price):
        """
        Draws a horizontal line at the specified price
        :param canvas: Canvas to draw on
        :param high: Used for scaling
        :param candle: Candle the drw the line above
        :param incCandle: The x pixel coord of the candle
        :param length: The length of the line in pixels
        :param color: The color of the line
        :param price: The price the line should be drawn at
        :return:
        """
        x1 = incCandle
        y1 = self.padding + (self.scaleFactor * (high - price))
        x2 = incCandle + length
        y2 = self.padding + (self.scaleFactor * (high - price))
        return canvas.create_line(x1, y1, x2, y2, fill=color)






    def markAsGenerated(self, x, y, r, canvas):  # center coordinates, radius
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







    def findHiLo(self, data):
        """
        Find the highest and the lowest candle in the array of candle objects
        :param data: An array of candle objects
        :return:
        """
        hi = -1
        low = 100000000000000
        for candle in data:
            if candle.high > hi: hi = candle.high
            if candle.low < low: low = candle.low

        return float(hi), float(low)







    def nextTrade(self, data, high):
        """
        A button to jump to the next trade
        :param data: An array of candle objects
        :param high: The highest candle used for scaling
        :return:
        """
        self.i += 1
        if self.i == len(self.purchaseInfo): self.i = 0
        detinationIncCandle = self.purchaseInfo[self.i]['selectionCoordsOpen'][0]
        self.canvas.xview_moveto((detinationIncCandle-50)/self.canvasWidth)
        self.setCanvasToStartingCandles(data, high)







    def prevTrade(self, data, high):
        """
        A button to jump to the previous trade
        :param data: An array of candle objects
        :param high: The highest candle used for scaling
        :return:
        """
        self.i -= 1
        if self.i == 0: self.i = len(self.purchaseInfo)-1
        detinationIncCandle = self.purchaseInfo[self.i]['selectionCoordsOpen'][0]
        self.canvas.xview_moveto((detinationIncCandle-50)/self.canvasWidth)
        self.setCanvasToStartingCandles(data, high)




    def startScrolling(self, evt, data, high):
        """
        A method to handle re-positioning the candles as the user scrolls
        :param evt:
        :param data: An array of candle objects
        :param high: The highest candle used for scaling
        :return:
        """
        currentViewIncandle = round((self.canvas.xview()[1] * max(1300,(20 + self.numberOfCandles*10)))/10)
        try:
            mid = (data[currentViewIncandle].high - data[currentViewIncandle].low)+data[currentViewIncandle].low
            midScreenCoords = self.padding + (self.scaleFactor * (high - mid))
            self.canvas.yview_moveto((midScreenCoords - 400) / self.canvasHeight)
        except: pass






    def setCanvasToStartingCandles(self, data, high):
        """
        Sets the canvas to the center of the starting candles
        :param data: An array of candle objects
        :param high: The highest candle used for scaling
        :return:
        """
        currentViewIncandle = round((self.canvas.xview()[1] * max(1300,(20 + self.numberOfCandles*10)))/10)
        mid = (data[currentViewIncandle].high - data[currentViewIncandle].low)+data[currentViewIncandle].low

        midScreenCoords = self.padding + (self.scaleFactor * (high - mid))
        self.canvas.yview_moveto((midScreenCoords-400)/self.canvasHeight)










if __name__ == '__main__':
    root=Tk()
    Data = companion("C:\\Users\\treeb\\OneDrive\\Desktop\\BackTestData.db")
    dataSet = Data.getDataByDatetime("GBP_USD", printReturn=False, startDatetime='2016-03-08 19:00:00',
                                     endDatetime='2016-05-09 02:00:00', indicators=['ATR(14)'])

    Map(root, dataSet, [])

    root.mainloop()
    Data.closeConnection()


# Setup examples
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

