"""
" Get the occurance count (lines in DNS files) in each individual second in a certain time period
" By Zhengping on 2018-08-09
"""

from src.util.FileReader import fileReader
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter


def doSecondlyCount(startTime, endTime, filename):
    if startTime > endTime:
        startTime, endTime = endTime, startTime
    minutelyCounter = Counter()
    file = fileReader(filename)
    fieldName="timestamp"

    for line in file:
        timeStamp = int(float(line.split("\t")[FieldToLoc[fieldName]]))
        if startTime <= timeStamp <= endTime:
            minutelyCounter[timeStamp] += 1
    return minutelyCounter


def getSecondlyCount_AsString(startTime, endTime, filename):
    minutelyCounter = doSecondlyCount(int(startTime), int(endTime), filename)
    ret_str = ""
    for minute in minutelyCounter.keys():
        ret_str += "%d\t%d\n" % (minute, minutelyCounter[minute])
    return ret_str


if __name__ == '__main__':
    start = "1520834310"
    end = "1520834429"
    sampleFile = "../../data/sampleFileDNS.log"
    print(getSecondlyCount_AsString(start, end, sampleFile))