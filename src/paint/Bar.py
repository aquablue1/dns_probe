"""
" draw the bar
" accept two lists as input, indicates X and Y axises respectively.
" Other parameters including"
" x/y labels, title and Ticks
"""

import matplotlib.pyplot as plt



class bar():
    def __init__(self):
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

    def doPaint(self, xData, yData, label, color="black"):
        self.plt.bar(xData, yData, label=label, color=color)

    def doshow(self):
        self.plt.legend(loc="best", fontsize=15)
        self.plt.show()


if __name__ == '__main__':
    x = [1,2,3,4,5,6,7,8,9]
    y = [1773309, 484266, 408669, 264095, 178955, 20701, 20675, 3782650,  929031]
    y2 = [403257, 116253, 88300, 72487, 140276, 12312, 8644, 0, 30401]
    xy = bar()
    xy.setLabel(xLabel="Target DNS Server", yLabel="Session Count on 2018-09-12(Million)")
    xy.doPaint(x, y, "Total Queries")
    xy.doPaint(x, y2, "Valid Response", color='green')
    xy.setTicks('y', [500000, 1000000, 1500000, 2000000, 2500_000, 3000_000, 3500_000],
                ["0.5", "1", "1.5", "2", "2.5", "3", '3.5'])
    xy.setTicks('x', x, ["CPSC NSes", "CampusOne", "CampusTwo", "CampusNew",
                         "Akamai", "Phys", "Auroral", "205Unknown", "Others"])

    for i in range(len(x)):
        xy.plt.text(x[i]-0.15, y[i]+25000, "%.0f%%" % (y2[i]/y[i]*100))

    xy.doshow()