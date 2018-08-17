"""
" draw the scatter
" accept two lists as input, indicates X and Y axises respectively.
" Other parameters including"
" x/y labels, title and Ticks
"""

import matplotlib.pyplot as plt



class scatter():
    def __init__(self, xData, yData,):
        self.xData = xData
        self.yData = yData
        self.plt = plt

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

    def doPaint(self, label):
        self.plt.scatter(self.xData, self.yData, label=label, color="black", marker="x")
        self.plt.legend(loc="best", fontsize=15)
        self.plt.show()


if __name__ == '__main__':
    x = [1,10, 100, 1000]
    y = [1, 200, 3000, 40000]
    xy = scatter(x, y)
    xy.setLabel(xLabel="X", yLabel="Y")
    xy.doPaint("x-y")