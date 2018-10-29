"""
" Get the daily top-K statistics of DNS requests' IP counting
" Including 1. Total distinct incoming src IPs
            2. Total distinct incoming dst IPs
            3. Total distinct outgoing src IPs
            4. Total distinct outgoing dst IPs
" By zhengping on 2018-09-19
"""

from src.util.FolderReader import folderReader
from src.util.FileReader import fileReader
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter
import os


def doHourlyIPCount(filename):
    srcField = "srcIP"
    dstField = "dstIP"
    srcIPCounter = Counter()
    dstIPCounter = Counter()
    File = fileReader(filename)
    for line in File:
        srcIPCounter[line.split("\t")[FieldToLoc[srcField]]] += 1
        dstIPCounter[line.split("\t")[FieldToLoc[dstField]]] += 1
    return srcIPCounter, dstIPCounter


def folderNameGen(date, direction):
    return "../../data/%s/%sbound" % (date, direction)


def getDailyIPCount(date, direction, topK = 10):
    Files = folderReader(folderNameGen(date, direction))
    dailySrcCount, dailyDstCount = Counter(), Counter()
    for file in Files:
        src, dst = doHourlyIPCount(file)
        dailySrcCount += src
        dailyDstCount += dst
        # print(dailyStatistics)
    return dailySrcCount.most_common(topK), dailyDstCount.most_common(topK)


if __name__ == '__main__':
    # date = "2018-09-09"
    dateList = ["2018-09-09", "2018-09-10", "2018-09-11", "2018-09-12",
                "2018-09-13", "2018-09-14", "2018-09-15", ]
    dateList = ["2018-05-02", "2018-05-16", "2018-05-30", "2018-06-06",]
    dateList = ["2018-05-09", "2018-06-20", "2018-06-27", "2018-07-04",
                "2018-07-11", "2018-07-18", "2018-07-25", "2018-08-01",
                "2018-08-08"]
    dateList = ["2018-06-13"]
    dateList = ["2018-05-23", "2018-08-15", "2018-08-22", "2018-08-29", "2018-09-05", "2018-09-19"]
    dateList = ["2018-06-12", "2018-06-14", "2018-06-15", "2018-06-16",
                "2018-06-17", "2018-06-18", "2018-06-19"]
    dateList = [ "2018-06-28", "2018-06-29", "2018-06-30", "2018-07-01",
                "2018-07-02", "2018-07-03"]
    for date in dateList:
        direction = "in"
        outputFoldername = "../../result/LongPeriodSample/%s/" % date
        if not os.path.exists(outputFoldername):
            os.makedirs(outputFoldername)
        outputSrcFilename = outputFoldername + "/dailySrcIPCount_%s.log" % date
        outputDstFilename = outputFoldername + "/dailyDstIPCount_%s.log" % date
        outputSrcFile = open(outputSrcFilename, 'a')
        outputDstFile = open(outputDstFilename, 'a')
        src, dst = getDailyIPCount(date, direction, 50)
        for srcIP, dstIP, index in zip(src, dst, range(1, len(src)+1)):
            srcOutput = "%d\t%s\t%d\n" % (index, srcIP[0], srcIP[1])
            outputSrcFile.write(srcOutput)
            dstOutput = "%d\t%s\t%d\n" % (index, dstIP[0], dstIP[1])
            outputDstFile.write(dstOutput)
        outputSrcFile.close()
        outputDstFile.close()

