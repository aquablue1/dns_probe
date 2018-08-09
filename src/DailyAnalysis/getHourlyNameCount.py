"""
" Get the count of distinct Domain Names queried in each individual hour
" Two files are suggested as the input files.
" By Zhengping on 2018-08-08
"""

from src.util.FileReader import fileReader
from src.util.DNSFieldLocMap import FieldToLoc


def doDistinceNameCount(filename, fieldName):
    Name_set = set()
    file = fileReader(filename)
    for line in file:
        name = line.split("\t")[FieldToLoc[fieldName]]
        Name_set.add(name)
    return len(Name_set)


def getHourlyNameCount(inComing=None, outGoing=None):
    inNameCount = -1
    outNameCount = -1

    srcFieldName = "query"
    dstFieldName = "query"
    if inComing is not None:
        inNameCount = doDistinceNameCount(inComing, srcFieldName)
    if outGoing is not None:
        outNameCount = doDistinceNameCount(outGoing, dstFieldName)

    return inNameCount, outNameCount


def getHourlyNameCount_AsString(hour, inComing=None, outGoing=None):
    inNameCount,  outNameCount = getHourlyNameCount(inComing, outGoing)

    return "%02d\t%s\t%s\n" % (hour, inNameCount, outNameCount)


if __name__ == '__main__':
    sampleFile = "../../data/sampleFileDNS.log"
    print(getHourlyNameCount_AsString(0, sampleFile, sampleFile))