"""
" Get the volume count of sessions in each second during a certain time period.
" By Zhengping on 2018-08-09
"""

from src.util.FileReader import fileReader
from src.util.CONNFieldLocMap import FieldToLoc
from src.util.SkipDashAdd import resolveStringAsInt
from collections import Counter


def doMinutelyCount(startTime, endTime, filename):
    if startTime > endTime:
        startTime, endTime = endTime, startTime
    sentByteVolumeCounter = Counter()
    recvByteVolumeCounter = Counter()
    file = fileReader(filename)
    fieldNameTime = "timestamp"
    fieldNameSrc = "sentByte"
    fieldNameDst = "recvByte"

    for line in file:
        line_list = line.split("\t")
        timeStamp = int(float(line_list[FieldToLoc[fieldNameTime]]))

        if startTime <= timeStamp <= endTime:
            sentByteVolumeCounter[timeStamp] += resolveStringAsInt(line_list[FieldToLoc[fieldNameSrc]])
            recvByteVolumeCounter[timeStamp] += resolveStringAsInt(line_list[FieldToLoc[fieldNameDst]])

    return (sentByteVolumeCounter, recvByteVolumeCounter)


def getMinutelyCount_AsString(startTime, endTime, filename):
    (srcByteCounter, dstByteCounter) = doMinutelyCount(int(startTime), int(endTime), filename)
    ret_str = ""
    for minute in sorted(list(set(srcByteCounter.keys()).union(set(dstByteCounter.keys())))):
        ret_str += "%d\t%d\t%d\n" % (minute, srcByteCounter[minute], dstByteCounter[minute])
    return ret_str


if __name__ == '__main__':
    start = "1520834110"
    end = "1520834429"
    sampleFile = "../../data/sampleFileCONN.log"
    print(getMinutelyCount_AsString(start, end, sampleFile))