"""
" Count a certain field based on the filtering of another field.
" Extended based on DailyQueryCount
" Note: if the filterField is set as None, all the input will be ignored.
" By Zhengping on 2018-08-16
"""

from src.util.FileReader import batchFileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter, OrderedDict


class dailyCountByField():
    def __init__(self, date, foldername, toField, filterField=None, filterVal=None):
        self.date = date
        self.foldername = foldername
        self.toField = toField
        self.filterField = filterField
        self.filterVal = filterVal


    def getDailyCount(self):
        foldername = self.foldername + "/%s/" % self.date
        CountStr = self.getDailyCount_AsString(foldername)

        outputFilename = self.foldername + "/%sCounterBy%s=%s_%s.log" % (self.toField, self.filterField,
                                                                         self.filterVal, self.date)
        outputF = fileWriter(outputFilename)

        outputF.writeString(CountStr)

    def __doHourlyCount(self, foldername):
        files = batchFileReader(foldername, cookie=self.date)
        filterCounter = Counter()
        for line in files:
            if self.filterField is None or line.split("\t")[FieldToLoc[self.filterField]] != self.filterVal:
                continue
            else:
                name = line.split("\t")[FieldToLoc[self.toField]]
                filterCounter[name] += 1
        return filterCounter

    def __getHourlyCount(self, foldername):
        return self.__doHourlyCount(foldername)

    def getDailyCount_AsString(self, foldername):
        filterCounter = self.__doHourlyCount(foldername)
        filterCounter = OrderedDict(filterCounter.most_common())
        ret_str = ""
        for key in filterCounter.keys():
            ret_str += "%s\t%d\n" % (key, filterCounter[key])
        return ret_str
