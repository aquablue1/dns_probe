"""
" draw the count of queries to CPSC popular names by hourly.
"
"""


from src.util.FolderReader import folderReader
from src.util.FileLineCounter import lineCount
from src.paint.Plot import plot


def doHourlyCount(foldername):
    folder = folderReader(foldername)
    countList = []
    for filename in folder:
        countList.append(lineCount(filename))
    return countList


def paintHourlyCount(countList):
    hourlyPlot = plot(xData=range(24), yData=countList)
    hourlyPlot.setLabel(xLabel="time", yLabel="count of queries in hour")
    xReal = range(24)
    xTick = ["%02d:00" % i for i in range(24)]
    hourlyPlot.setTicks("x", xReal, xTick, rotation=20)
    yLim = [0, 100000]
    hourlyPlot.setLim("y", yLim)
    hourlyPlot.doPaint("hourly request count")

if __name__ == '__main__':
    foldername = "../../result/CPSCRow/2018-03-07/"
    paintHourlyCount(doHourlyCount(foldername))
