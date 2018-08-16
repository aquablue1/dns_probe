"""
" General analysis script
" Count the source Port in a given day.
" Modified from get CPSCAnalysis/getDailyCPSCCount
" By Zhengping on 2018-08-14
"""

from src.util.FileReader import batchFileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter, OrderedDict


class dailySrcPortCount():
    def __init__(self, date, foldername):
        self.date = date
        self.foldername = foldername

    def getDailySrcPortCount(self):
        foldername = self.foldername + "/%s/" % self.date
        srcPortCountStr = self.getDailySrcPortCount_AsString(foldername)

        outputFilename = self.foldername + "/srcPortCounter_%s.log" % self.date
        outputF = fileWriter(outputFilename)

        outputF.writeString(srcPortCountStr)

    def __doHourlySrcPortCount(self, foldername):
        files = batchFileReader(foldername, cookie=self.date)
        srcPortCounter = Counter()
        for line in files:
            srcPortIP = line.split("\t")[FieldToLoc["srcPort"]]
            srcPortCounter[srcPortIP] += 1
        return srcPortCounter

    def __getHourlySrcPortCount(self, foldername):
        return self.__doHourlySrcPortCount(foldername)

    def getDailySrcPortCount_AsString(self, foldername):
        srcPortCounter = self.__doHourlySrcPortCount(foldername)
        srcPortCounter = OrderedDict(srcPortCounter.most_common())
        ret_str = ""
        for key in srcPortCounter.keys():
            ret_str += "%s\t%d\n" % (key, srcPortCounter[key])

        return ret_str