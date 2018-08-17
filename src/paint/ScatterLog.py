"""
" draw the scatter with log scale of both
" X and Y axis
" accept two lists as input
" range, x/y labels and
"""

import matplotlib.pyplot as plt
import math


class scatterLog():
    def __init__(self, xData, yData,):
        self.xData = [math.log10(x) for x in xData]
        self.yData = [math.log10(y) for y in yData]
        self.plt = plt

    def setLabel(self, xLabel=None, yLabel=None, fontsize=20):
        self.plt.xlabel(xLabel, fontsize=fontsize)
        self.plt.ylabel(yLabel, fontsize=fontsize)

    def setTitle(self, title, fontsize=30):
        self.plt.title(title, fontsize=fontsize)

    def setTicks(self, axis, realData, labelData):
        if axis.lower() == "x":
            realDataLog = [math.log10(rData) for rData in realData]
            self.plt.xticks(realDataLog, labelData)
        elif axis.lower() == "y":
            realDataLog = [math.log10(rData) for rData in realData]
            self.plt.yticks(realDataLog, labelData)

    def doPaint(self, label):
        self.plt.scatter(self.xData, self.yData, label=label, color="black", marker="x")
        self.plt.legend(loc="best", fontsize=15)
        self.plt.show()


if __name__ == '__main__':
    x = [1,10, 100, 1000]
    y = [1, 200, 3000, 40000]
    xy = scatterLog(x, y)
    xy.setLabel(xLabel="X", yLabel="Y")
    xy.doPaint("x-y")