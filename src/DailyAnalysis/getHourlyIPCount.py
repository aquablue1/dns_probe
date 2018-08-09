"""
" Get the count of distinct IPs in each individual hour
" Two files are suggested as the input files.
" By Zhengping on 2018-08-08
"""

from src.util.FileReader import fileReader
from src.util.DNSFieldLocMap import FieldToLoc


def doDistinceIPCount(filename, fieldName):
    IP_set = set()
    file = fileReader(filename)
    for line in file:
        IP = line.split("\t")[FieldToLoc[fieldName]]
        IP_set.add(IP)
    return len(IP_set)


def getHourlyIPCount(inComing=None, outGoing=None):
    inSrcCount = -1
    inDstCount = -1
    outSrcCount = -1
    outDstCount = -1

    srcFieldName = "srcIP"
    dstFieldName = "dstIP"
    if inComing is not None:
        inSrcCount = doDistinceIPCount(inComing, srcFieldName)
    if inComing is not None:
        inDstCount = doDistinceIPCount(inComing, dstFieldName)
    if outGoing is not None:
        outSrcCount = doDistinceIPCount(outGoing, srcFieldName)
    if outGoing is not None:
        outDstCount = doDistinceIPCount(outGoing, dstFieldName)

    return inSrcCount, inDstCount, outSrcCount, outDstCount


def getHourlyOverallCount_AsString(hour, inComing=None, outGoing=None):
    inSrcCount, inDstCount, outSrcCount, outDstCount = \
        getHourlyIPCount(inComing, outGoing)

    return "%02d\t%s\t%s\t%s\t%s\n" % (hour, inSrcCount, inDstCount, outSrcCount, outDstCount)


if __name__ == '__main__':
    sampleFile = "../../data/sampleFileDNS.log"
    print(getHourlyOverallCount_AsString(0, sampleFile, sampleFile))