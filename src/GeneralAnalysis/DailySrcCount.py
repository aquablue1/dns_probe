"""
" General analysis script
" Count the source IP in a given day.
" Modified from get CPSCAnalysis/getDailyCPSCCount
" By Zhengping on 2018-08-14
"""

from src.util.FileReader import batchFileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter, OrderedDict


class dailySrcCount():
    def __init__(self, date, foldername):
        self.date = date
        self.foldername = foldername

    def getDailySrcCount(self):
        foldername = self.foldername + "/%s/" % self.date
        srcCountStr = self.getDailySrcCount_AsString(foldername)

        outputFilename = self.foldername + "/srcCounter_%s.log" % self.date
        outputF = fileWriter(outputFilename)

        outputF.writeString(srcCountStr)

    def __doHourlySrcCount(self, foldername):
        files = batchFileReader(foldername, cookie=self.date)
        srcCounter = Counter()
        for line in files:
            srcIP = line.split("\t")[FieldToLoc["srcIP"]]
            srcCounter[srcIP] += 1
        return srcCounter


    def __getHourlySrcCount(self, foldername):
        return self.__doHourlySrcCount(foldername)


    def getDailySrcCount_AsString(self, foldername):
        srcCounter = self.__doHourlySrcCount(foldername)
        srcCounter = OrderedDict(srcCounter.most_common())
        ret_str = ""
        for key in srcCounter.keys():
            ret_str += "%s\t%d\n" % (key, srcCounter[key])

        return ret_str