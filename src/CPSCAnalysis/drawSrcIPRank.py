"""
" Draw the scatter/plot of popularity of Source IPs of dns sessions that queried CPSC URLs
" By Zhengping on 2018-08-12
"""

from src.util.FileReader import fileReader
from src.paint.ScatterLog import scatterLog
from src.paint.PlotLog import plotLog


def drawSrcIP(filename):
    countList = []
    file = fileReader(filename)
    for line in file:
        count = int(line.split("\t")[1])
        countList.append(count)

    countList.sort(reverse=True)
    srcIPScatter = scatterLog(range(1, 1+len(countList)), countList)
    srcIPScatter.setLabel(xLabel="rank of source IPs", yLabel="number of query")
    xReal = [1, 10, 100, 1000, 10000, 100000]
    xTick = ["1", "10", "100", "10E3", "10E4", "10E5"]
    yReal = [1, 10, 100, 1000, 10000]
    yTick = ["1", "10", "100", "10E3", "10E4"]
    srcIPScatter.setTicks("x", xReal, xTick)
    srcIPScatter.setTicks("y", yReal, yTick)
    srcIPScatter.doPaint(label="query counting")



if __name__ == '__main__':
    date = "2018-03-07"
    filename = "../../result/CPSCRow/srcCounter_%s.log" % date
    drawSrcIP(filename)
