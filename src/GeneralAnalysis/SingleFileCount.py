"""
" Count specified fields in a given file.
" A given file sometimes indicates a single hour, or single day.
" Return the counter of each specified field.
" By Zhengping on 2018-08-19
"""

from src.util.FileReader import fileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter, OrderedDict

class singleFileCount():
    def __init__(self, date, filename):
        self.date = date
        self.filename = filename

    def getSpecifiedCount(self, fieldName):
        file = fileReader(self.filename)
        certainCounter = Counter()
        for line in file:
            specifiedFieldVal = line.split("\t")[FieldToLoc[fieldName]]
            certainCounter[specifiedFieldVal] += 1
        return certainCounter

    def dumpSpecifiedCount(self, fieldName):
        certainCounter = OrderedDict(self.getSpecifiedCount(fieldName).most_common())
        outputFilename = ".".join(self.filename.split(".")[:-1]) + "_%sCounter.log" % fieldName
        outputF = fileWriter(outputFilename)
        ret_str = ""
        for elem in certainCounter.keys():
            ret_str += "%s\t%d\n" % (elem, certainCounter[elem])
        outputF.writeString(ret_str)


if __name__ == '__main__':
    date = "2018-03-07"
    filename = "../../result/ToCPSC/ReverseAnalysis/reverseDNSToRow_NS1_%s.log" % date
    fcount = singleFileCount(date, filename)
    query_list = ["query", "error", "srcIP", "srcPort"]
    query_list = ["type"]
    for query in query_list:
        print(fcount.dumpSpecifiedCount(query))

