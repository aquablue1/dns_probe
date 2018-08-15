"""
" Get the daily count of distinct destination IPs (Campus DNS) of CPSC related traffics
" By Zhengping  on 2018-08-10
"""


from src.util.FileReader import batchFileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter, OrderedDict


def doDailyDstCount(foldername, date):
    files = batchFileReader(foldername, cookie=date)
    srcCounter = Counter()
    for line in files:
        srcIP = line.split("\t")[FieldToLoc["dstIP"]]
        srcCounter[srcIP] += 1
    return srcCounter


def getDailyDstCount(foldername, date):
    return doDailyDstCount(foldername, date)


def getDailyDstCount_AsString(foldername, date):
    srcCounter = doDailyDstCount(foldername, date)
    srcCounter = OrderedDict(srcCounter.most_common())
    ret_str = ""
    for key in srcCounter.keys():
        ret_str += "%s\t%d\n" % (key, srcCounter[key])

    return ret_str


if __name__ == '__main__':
    date = "2018-03-07"
    foldername = "../../result/CPSCRow/%s/" % date
    dstCountStr = getDailyDstCount_AsString(foldername, date)

    outputFilename = "../../result/CPSCRow/dstCounter_%s.log" % date
    outputF = fileWriter(outputFilename)

    outputF.writeString(dstCountStr)
