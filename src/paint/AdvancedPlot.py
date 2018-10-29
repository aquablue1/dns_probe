"""
" Advanced Method to draw the plot
" Compared with Plot: 1. it can contain multiple plots
" 2. It will set the lines between zero-value points as dot lines.
" By Zhengping on 2018-09-21
"""


import matplotlib.pyplot as plt
from src.util.PaintPlugs import markerList, colorList


class advancedPlot():
    def __init__(self):
        self.plt = plt
        self.indexPlug = 0
        self.isDotForZero = False

    def setLabel(self, xLabel=None, yLabel=None, fontsize=20):
        self.plt.xlabel(xLabel, fontsize=fontsize)
        self.plt.ylabel(yLabel, fontsize=fontsize)

    def setTitle(self, title, fontsize=30):
        self.plt.title(title, fontsize=fontsize)

    def setTicks(self, axis, realData, labelData, rotation=0):
        if axis.lower() == "x":
            self.plt.xticks(realData, labelData, rotation=rotation)
        elif axis.lower() == "y":
            self.plt.yticks(realData, labelData, rotation=rotation)

    def setLim(self, axis, lim):
        if axis.lower() == "x":
            self.plt.xlim(lim)
        elif axis.lower() == "y":
            self.plt.ylim(lim)

    def doPaint(self, xData, yData, label):
        if not self.isDotForZero:
            self.plt.plot(xData, yData, label=label, color=colorList[self.indexPlug], marker=markerList[self.indexPlug])
            self.indexPlug += 1
            self.plt.legend(loc="best", fontsize=15)
        else:
            breakList = self._getBreakList(yData)
            print(breakList)
            xDataList = self._resolveList(xData, self._getBreakList(yData))
            yDataList = self._resolveList(yData, self._getBreakList(yData))
            for xpData, ypData in zip(xDataList, yDataList):
                print(xpData)
                print(ypData)
                print("----")
                linestyle = '--' if ypData[-1] == 0 else '-'
                self.plt.plot(xpData, ypData, label=label, linestyle=linestyle,
                              color=colorList[self.indexPlug], marker=markerList[self.indexPlug])


    def _getBreakList(self, dataList):
        breakList = []
        isZero = True if dataList[0] == 0 else False
        for i in range(1, len(dataList)):
            if isZero and dataList[i] != 0:
                breakList.append(i-1)
                isZero = False
            elif not isZero and dataList[i] == 0:
                breakList.append(i-1)
                isZero = True
        breakList.append(len(dataList)-1)
        return breakList

    def _resolveList(self, toResolveList, breakList):
        ResolvedList = []
        for bp in breakList:
            front = toResolveList[0:bp+1]
            ResolvedList.append(front)
            back =  toResolveList[bp:]
            toResolveList = back
            breakList[:] = [i-len(front)+1 for i in breakList]
        if not toResolveList:
            ResolvedList.append(toResolveList)
        return ResolvedList


    def doShow(self):
        self.plt.show()


if __name__ == '__main__':
    x = [1,5, 10, 15]
    y1 = [1, 30, 40, 50]
    y2 = [1, 20, 30, 40]
    xy = advancedPlot()
    xy.setLabel(xLabel="X", yLabel="Y")
    # xy.doPaint(x, y1, "x-y1")
    # xy.doPaint(x, y2, "x-y2")
    # xy.doShow()
    toRL = [0,0,2,3,0,0,0,2,4,5,0,]
    breakList = [1, 3, 6, 9, 10]
    # print(xy._getBreakList(toRL))
    # print(xy._resolveList(toRL, breakList))
    xy.isDotForZero = False
    xy.doPaint(list(range(len(toRL))), toRL, "label")
    xy.doShow()