"""
" General analysis script
" Count the unique name queried in a given day.
" Modified from get CPSCAnalysis/getDailyCPSCCount
" By Zhengping on 2018-08-15
"""

from src.util.FileReader import batchFileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter, OrderedDict


class dailyNameCount():
    def __init__(self, date, foldername):
        self.date = date
        self.foldername = foldername

    def getDailyNameCount(self):
        foldername = self.foldername + "/%s/" % self.date
        srcCountStr = self.getDailyNameCount_AsString(foldername)

        outputFilename = self.foldername + "/nameCounter_%s.log" % self.date
        outputF = fileWriter(outputFilename)

        outputF.writeString(srcCountStr)

    def __doHourlyNameCount(self, foldername):
        files = batchFileReader(foldername, cookie=self.date)
        srcCounter = Counter()
        for line in files:
            name = line.split("\t")[FieldToLoc["query"]]
            srcCounter[name] += 1
        return srcCounter

    def __getHourlyNameCount(self, foldername):
        return self.__doHourlyNameCount(foldername)

    def getDailyNameCount_AsString(self, foldername):
        srcCounter = self.__doHourlyNameCount(foldername)
        srcCounter = OrderedDict(srcCounter.most_common())
        ret_str = ""
        for key in srcCounter.keys():
            ret_str += "%s\t%d\n" % (key, srcCounter[key])

        return ret_str