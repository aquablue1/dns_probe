"""
" General analysis script
" Count the type of DNS queries in a given day.
" Modified from get CPSCAnalysis/getDailyCPSCCount
" By Zhengping on 2018-09-23
"""

from src.util.FileReader import batchFileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter, OrderedDict


class dailyTypeCount():
    def __init__(self, date, folderType):
        self.date = date
        self.folderType = folderType

    def getDailyTypeCount(self):
        folderType = self.folderType + "/%s/" % self.date
        srcCountStr = self.getDailyTypeCount_AsString(folderType)

        outputFileType = self.folderType + "/typeCounter_%s.log" % self.date
        outputF = fileWriter(outputFileType)

        outputF.writeString(srcCountStr)

    def __doHourlyTypeCount(self, folderType, ):
        files = batchFileReader(folderType, cookie=self.date)
        srcCounter = Counter()
        for line in files:
            type = line.split("\t")[FieldToLoc["type"]]
            srcCounter[type] += 1
        return srcCounter

    def __getHourlyTypeCount(self, folderType):
        return self.__doHourlyTypeCount(folderType)

    def getDailyTypeCount_AsString(self, folderType):
        srcCounter = self.__doHourlyTypeCount(folderType)
        srcCounter = OrderedDict(srcCounter.most_common())
        ret_str = ""
        for key in srcCounter.keys():
            ret_str += "%s\t%d\n" % (key, srcCounter[key])

        return ret_str
