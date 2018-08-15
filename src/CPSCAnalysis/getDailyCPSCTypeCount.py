"""
" Get the daily count of distinct query Tpyes (A/AAAA) of CPSC related traffics
" By Zhengping  on 2018-08-10
"""


from src.util.FileReader import batchFileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter, OrderedDict


def doDailyTypeCount(foldername, date):
    files = batchFileReader(foldername, cookie=date)
    typeCounter = Counter()
    for line in files:
        srcIP = line.split("\t")[FieldToLoc["type"]]
        typeCounter[srcIP] += 1
    return typeCounter


def getDailyTypeCount(foldername, date):
    return doDailyTypeCount(foldername, date)


def getDailyTypeCount_AsString(foldername, date):
    typeCounter = doDailyTypeCount(foldername, date)
    typeCounter = OrderedDict(typeCounter.most_common())
    ret_str = ""
    for key in typeCounter.keys():
        ret_str += "%s\t%d\n" % (key, typeCounter[key])

    return ret_str


if __name__ == '__main__':
    date = "2018-03-07"
    foldername = "../../result/CPSCRow/%s/" % date
    typeCountStr = getDailyTypeCount_AsString(foldername, date)

    outputFilename = "../../result/CPSCRow/typeCounter_%s.log" % date
    outputF = fileWriter(outputFilename)

    outputF.writeString(typeCountStr)
