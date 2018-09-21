"""
" Draw the scatter of the rank of distinct names/ports/IPs and their corresponding occurrence.
" By Zhengping on 2018-08-19
"""

from src.util.FileReader import fileReader
from src.paint.ScatterLog import scatterLog


def drawSrcIPCounterScatter(filename):
    file = fileReader(filename)
    countList = []
    for line in file:
        countList.append(int(line.split("\t")[1]))
    graph = scatterLog(range(1, 1+len(countList)), countList)

    graph.setLabel(xLabel="rank of distinct reverse query names", yLabel="number of corresponding queries")
    xReal = [1, 10, 100, 1000, 10000, 100000]
    xTick = ["1", "10", "100", "10E3", "10E4", "10E5"]
    yReal = [1, 10, 100, 1000, 10000, 100000]
    yTick = ["1", "10", "100", "10E3", "10E4", "10E5"]
    graph.setTicks("x", xReal, xTick)
    graph.setTicks("y", yReal, yTick)
    graph.doPaint(label="reverse query names")


if __name__ == '__main__':
    filename = "../../result/ToCPSCAnalysis/ReverseAnalysis/reverseDNSToRow_NS1_2018-03-07_queryCounter.log"
    drawSrcIPCounterScatter(filename)