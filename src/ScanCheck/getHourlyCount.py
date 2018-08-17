"""
" Get the hourly count of srcIP, dstIP, queried name and port of the newIP records
" Input, /result/ScanCheck/%date/hourlyData.log
" Output, the corresponding analysis results
" By Zhengping on 2018-08-15
"""

from src.util.FileReader import fileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter, OrderedDict


def getHourlySrcIPCount(filename):
    srcCounter = Counter()
    file = fileReader(filename)
    for line in file:
        srcIP = line.split("\t")[FieldToLoc["srcIP"]]
        srcCounter[srcIP] += 1
    return srcCounter


def getHourlyDstIPCount(filename):
    dstCounter = Counter()
    file = fileReader(filename)
    for line in file:
        dstIP = line.split("\t")[FieldToLoc["dstIP"]]
        dstCounter[dstIP] += 1
    return dstCounter


def getHourlyNameIPCount(filename):
    nameCounter = Counter()
    file = fileReader(filename)
    for line in file:
        nameIP = line.split("\t")[FieldToLoc["query"]]
        nameCounter[nameIP] += 1
    return nameCounter


def getHourlySrcPortIPCount(filename):
    srcPortCounter = Counter()
    file = fileReader(filename)
    for line in file:
        srcPortIP = line.split("\t")[FieldToLoc["srcPort"]]
        srcPortCounter[srcPortIP] += 1
    return srcPortCounter


def dumpCounter(counter, outputFilename):
    ret_src = ""
    counter = OrderedDict(counter.most_common())
    for elem in counter.keys():
        ret_src += "%s\t%d\n" % (elem, counter[elem])

    outputF = fileWriter(outputFilename)
    outputF.writeString(ret_src)


if __name__ == '__main__':
    date = "2018-03-07"
    filename = "../../result/ScanCheck/%s/NewIPRow_%s_23.log" % (date, date)
    outputSrc = "../../result/ScanCheck/srcCount_%s_23.log" % date
    outputDst = "../../result/ScanCheck/dstCount_%s_23.log" % date
    outputName = "../../result/ScanCheck/nameCount_%s_23.log" % date
    outputSrcPort = "../../result/ScanCheck/srcPortCount_%s_23.log" % date
    dumpCounter(getHourlySrcIPCount(filename), outputSrc)
    dumpCounter(getHourlyDstIPCount(filename), outputDst)
    dumpCounter(getHourlyNameIPCount(filename), outputName)
    dumpCounter(getHourlySrcPortIPCount(filename), outputSrcPort)