"""
" Draw the Bar chart of subnet analysis
"""


from src.util.FolderReader import folderReader
from src.util.FileReader import fileReader
from src.paint.Bar import bar
from collections import Counter

def getSubnetData(filename):
    yDataDict = Counter()
    file = fileReader(filename)
    for line in file:
        subnetID = int(line.split("\t")[0])
        subnetCount = int(line.split("\t")[1])
        yDataDict[subnetID] = subnetCount
    return yDataDict


def drawSubnetBar(filename, cookie):
    yDataDict = getSubnetData(filename)
    xData = range(256)
    yData = [yDataDict[i] for i in xData]
    subnetBar = bar(xData=xData, yData=yData)
    subnetBar.setLabel(xLabel="subnet ID", yLabel="Count of total sessions")
    subnetBar.setLim("y", [0, 1000])
    subnetBar.doPaint(cookie)


if __name__ == '__main__':
    date = "2018-03-07"
    filename = "../../result/SubnetCount/%s/occurred/outbound/outSubnet_2018-03-07_00.log" % date
    drawSubnetBar(filename, "outbound")
