"""
" General analysis script
" Count the destination IP in a given day.
" Modified from get CPSCAnalysis/getDailyCPSCCount
" By Zhengping on 2018-08-14
"""

from src.util.FileReader import batchFileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter, OrderedDict


class dailyDstCount():
    def __init__(self, date, foldername):
        self.date = date
        self.foldername = foldername

    def getDailyDstCount(self):
        foldername = self.foldername + "/%s/" % self.date
        DstCountStr = self.getDailyDstCount_AsString(foldername)

        outputFilename = self.foldername + "/dstCounter_%s.log" % self.date
        outputF = fileWriter(outputFilename)

        outputF.writeString(DstCountStr)

    def __doHourlyDstCount(self, foldername):
        files = batchFileReader(foldername, cookie=self.date)
        dstCounter = Counter()
        for line in files:
            srcIP = line.split("\t")[FieldToLoc["dstIP"]]
            dstCounter[srcIP] += 1
        return dstCounter

    def __getHourlyDstCount(self, foldername):
        return self.__doHourlyDstCount(foldername)

    def getDailyDstCount_AsString(self, foldername):
        dstCounter = self.__doHourlyDstCount(foldername)
        dstCounter = OrderedDict(dstCounter.most_common())
        ret_str = ""
        for key in dstCounter.keys():
            ret_str += "%s\t%d\n" % (key, dstCounter[key])

        return ret_str