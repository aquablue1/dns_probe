"""
" Draw the rank of distinct names queried to black hole servers and their corresponding counts.
" Based on the result from getTopKName
" By Zhengping on 2018-08-13
"""

from src.util.FileReader import fileReader
from src.util.FolderReader import folderReader
from src.util.DNSFieldLocMap import FieldToLoc
from src.paint.ScatterLog import scatterLog
from collections import Counter
import math


def doNameOccuranceCount(filename):
    """
    Get the counter of domains in the given file
    :param filename: input file name, should be normal DNS log
    :return: counter object of distinct names
    """
    file = fileReader(filename)
    fieldName = "query"
    nameCounter = Counter()
    for line in file:
        name = line.split("\t")[FieldToLoc[fieldName]]
        nameCounter[name] += 1
    return nameCounter


def getDailyNameCount(foldername):
    nameCounter = Counter()
    folder = folderReader(foldername)
    for filename in folder:
        nameCounter += doNameOccuranceCount(filename)
    print("The num of distinct name is %d." % len(nameCounter))
    print("The most popular one is %s" % nameCounter.most_common(11))
    return nameCounter

def drawNameCount(count):
    countList = list(count.values())
    countList.sort(reverse=True)

    nameScatter = scatterLog(range(1, len(countList)), countList[1:])
    nameScatter.setLabel(xLabel="rank of queried names", yLabel="count of query to black hole")

    xReal = [math.log10(2), 10, 100, 1000, 10000, 100000]
    xTick = ["2", "10", "100", "10E3", "10E4", "10E5"]
    yReal = [1, 10, 100, 1000, 10000]
    yTick = ["1", "10", "100", "10E3", "10E4"]
    nameScatter.setTicks("x", xReal, xTick)
    nameScatter.setTicks("y", yReal, yTick)

    nameScatter.doPaint(label="black hole query")


if __name__ == '__main__':
    date = "2018-03-07"
    foldername = "../../result/Blackhole/%s/" % date

    drawNameCount(getDailyNameCount(foldername))