"""
" Analysis the src IP of NBSTAT related traffic.
"""


from src.util.FolderReader import folderReader
from src.util.FileReader import fileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
import os
from collections import Counter


def getHourlySrcIPCount(filename):
    file = fileReader(filename)
    srcIPCounter = Counter()
    for line in file:
        srcIP = line.split("\t")[FieldToLoc["srcIP"]]
        srcIPCounter[srcIP] += 1
    return srcIPCounter


def dumpDailySrcIPCount(date):
    dailySrcIPCounter = Counter()
    for time in range(24):
        # Generate Hourly Report
        dump_str = ""
        time = str(time).zfill(2)
        filename = "../../result/NBSTAT/%s/%s_%02s.log" % (date, date, time)
        outputFoldername = "../../result/NBSTAT/srcIPAnalysis/%s" % date
        if not os.path.exists(outputFoldername):
            os.makedirs(outputFoldername)
        outputFilename = "%s/srcIP_%s_%s.log" % (outputFoldername, date, time)
        srcIPCounter = getHourlySrcIPCount(filename)
        for tuple in srcIPCounter.most_common(50):
            dump_str = dump_str + str(tuple[0]) + "\t" + str(tuple[1]) + "\n"
        campusFile = fileWriter(outputFilename)
        campusFile.writeString(dump_str)
        dailySrcIPCounter += srcIPCounter
    # Generate Daily Summary
    dump_str = ""
    dailySummaryFilename = "../../result/NBSTAT/srcIPAnalysis/srcIP_dailySummary_%s.log" % date
    for tuple in dailySrcIPCounter.most_common(100):
        dump_str = dump_str + str(tuple[0]) + "\t" + str(tuple[1]) + "\n"
    campusFile = fileWriter(dailySummaryFilename)
    campusFile.writeString(dump_str)


if __name__ == '__main__':
    date = "2018-09-13"

    # dumpParticalIP(filename, outputFilename)
    dumpDailySrcIPCount(date)
