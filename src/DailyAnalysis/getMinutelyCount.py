"""
" Get the occurance count (lines in DNS files) in each individual minute in a certain time period
" By Zhengping on 2018-08-09
"""

from src.util.FileReader import fileReader
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter


def doMinutelyCount(startTime, endTime, filename):
    if startTime > endTime:
        startTime, endTime = endTime, startTime
    startMinute = int(startTime/60)
    endMinute = int(endTime/60)
    minutelyCounter = Counter()
    file = fileReader(filename)
    fieldName="timestamp"

    for line in file:
        timeStamp = int(float(line.split("\t")[FieldToLoc[fieldName]]))
        timeMinute = int(timeStamp/60)
        if startMinute <= timeMinute <= endMinute:
            minutelyCounter[timeMinute] += 1
    return minutelyCounter


def getMinutelyCount_AsString(startTime, endTime, filename):
    minutelyCounter = doMinutelyCount(int(startTime), int(endTime), filename)
    ret_str = ""
    for minute in minutelyCounter.keys():
        ret_str += "%d\t%d\n" % (minute, minutelyCounter[minute])
    return ret_str


if __name__ == '__main__':
    start = "1520834310"
    end = "1520834429"
    sampleFile = "../../data/sampleFileDNS.log"
    print(getMinutelyCount_AsString(start, end, sampleFile))