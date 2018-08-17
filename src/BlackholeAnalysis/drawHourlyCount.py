"""
" Draw the hourly count of queries that sent to blackhole
" Modified based on drawHourlyCount from CPSCAnalysis.
" By Zhengping on 2018-08-13
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
    yLim = [0, 120000]
    hourlyPlot.setLim("y", yLim)
    hourlyPlot.doPaint("hourly black hole count")


if __name__ == '__main__':
    foldername = "../../result/Blackhole/2018-03-07/"
    paintHourlyCount(doHourlyCount(foldername))