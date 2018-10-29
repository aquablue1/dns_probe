"""
" Draw the heatmap of reverse DNS queries.
" By Zhengping on 2018-10-15
"""


from src.util.FileReader import fileReader
from src.util.DNSFieldLocMap import FieldToLoc
from src.util.ReverseIP import getNormByReverse
from src.util.FileWriter import fileWriter
from src.util.FolderReader import folderReader
from collections import Counter
from src.paint.HeatMap import doDrawHeatMap
import math


def dumpParticalIP(filename, outputFilename):
    outputStr = ""
    file = fileReader(filename)
    for line in file:
        query = line.split("\t")[FieldToLoc["query"]]
        if ".in-addr.arpa" in query:
            fullIP = getNormByReverse(query)
            particalIP = ".".join(fullIP.split(".")[2:4])
            if particalIP != "" and "." in particalIP :
                outputStr = outputStr + particalIP + "\n"
    outputFile = fileWriter(outputFilename)
    outputFile.writeString(outputStr)


def getStatistics(filename):
    startX = 0
    startY = 200
    size = 50
    file = fileReader(filename)
    IPDict = [[] for _ in range(size)]
    for i in range(size):
        IPDict[i] = [0] * size
    for line in file:
        print(line)
        if "." not in line:
            continue
        [IPForth, IPThird] = line.strip().split(".")
        if startX <= int(IPThird) < startX+size and startY <= int(IPForth) < startY+size:
            IPDict[int(IPThird)-startX][int(IPForth)-startY] += 1
    print(IPDict[int(size/2)])
    for i in range(len(IPDict)):
        for j in range(len(IPDict[i])):
            if IPDict[i][j] == 0:
                continue
            IPDict[i][j] = math.log10(IPDict[i][j])
    xticks = [str(i) for i in range(startX, startX+size)]
    yticks = [str(i) for i in range(startY, startY+size)]
    doDrawHeatMap(IPDict, xticks, yticks)


def getCount(filename):
    IPCounter = Counter()
    file = fileReader(filename)
    for line in file:
        print(line)
        if "." not in line:
            continue
        line = line.strip()
        IPCounter[line] += 1
    print(len(IPCounter))


if __name__ == '__main__':
    date = "2018-07-01"
    filename = "../../result/ToCPSC/%s/%s_22.log" % (date, date)
    outputFilename = "../../result/ToCPSC/ReverseAnalysis/heatMap/%s/reverseIP_%s_22.log" % (date, date)
    dumpParticalIP(filename, outputFilename)

    # getStatistics(outputFilename)
    # getCount(outputFilename)