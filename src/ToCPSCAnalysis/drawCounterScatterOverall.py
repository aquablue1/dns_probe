"""
" Draw the scatter of rank of IP/port/name and their corresponding occurrences.
" This script focuses on the overall count of ToCPSC Traffic.
" By Zhengping on 2018-08-19
"""

from src.paint.ScatterLog import scatterLog
from src.util.FileReader import fileReader


def drawSrcIPCounterScatter(filename):
    file = fileReader(filename)
    countList = []
    for line in file:
        countList.append(int(line.split("\t")[1]))
    graph = scatterLog(range(1, 1+len(countList)), countList)

    graph.setLabel(xLabel="rank of distinct queried names", yLabel="number of corresponding queries")
    xReal = [1, 10, 100, 1000, 10000, 100000]
    xTick = ["1", "10", "100", "10E3", "10E4", "10E5"]
    yReal = [1, 10, 100, 1000, 10000, 100000, 1000000]
    yTick = ["1", "10", "100", "10E3", "10E4", "10E5", "10E6"]
    graph.setTicks("x", xReal, xTick)
    graph.setTicks("y", yReal, yTick)
    graph.doPaint(label="name")


if __name__ == '__main__':
    filename = "../../result/ToCPSCAnalysis/nameCounter_2018-03-07.log"
    drawSrcIPCounterScatter(filename)