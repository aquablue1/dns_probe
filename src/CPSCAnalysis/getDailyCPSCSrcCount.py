"""
" Get the daily count of distinct source IPs of CPSC related traffics
" By Zhengping  on 2018-08-10
"""


from src.util.FileReader import batchFileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter, OrderedDict


def doDailySrcCount(foldername, date):
    files = batchFileReader(foldername, cookie=date)
    srcCounter = Counter()
    for line in files:
        srcIP = line.split("\t")[FieldToLoc["srcIP"]]
        srcCounter[srcIP] += 1
    return srcCounter


def getDailySrcCount(foldername, date):
    return doDailySrcCount(foldername, date)


def getDailySrcCount_AsString(foldername, date):
    srcCounter = doDailySrcCount(foldername, date)
    srcCounter = OrderedDict(srcCounter.most_common())
    ret_str = ""
    for key in srcCounter.keys():
        ret_str += "%s\t%d\n" % (key, srcCounter[key])

    return ret_str


if __name__ == '__main__':
    date = "2018-03-07"
    foldername = "../../result/CPSCRow/%s/" % date
    srcCountStr = getDailySrcCount_AsString(foldername, date)

    outputFilename = "../../result/CPSCRow/srcCounter_%s.log" % date
    outputF = fileWriter(outputFilename)

    outputF.writeString(srcCountStr)
