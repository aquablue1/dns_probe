"""
" Get the total traffic volume of each hour in record files.
" Receive two hourly CONN files as input.
" By Zhengping on 2018-08-08
"""

from src.util.FileReader import fileReader
from src.util.CONNFieldLocMap import FieldToLoc


def doHourlyOverallCount(filename):
    file = fileReader(filename)
    srcVolume = 0
    dstVolume = 0
    for line in file:
        srcVolume_t = line.split("\t")[FieldToLoc["sentByte"]]
        dstVolume_t = line.split("\t")[FieldToLoc["recvByte"]]
        if srcVolume_t == "-" or dstVolume_t == "-":
            continue
        else:
            srcVolume += int(srcVolume_t)
            dstVolume += int(dstVolume_t)
    return (srcVolume, dstVolume)


def getHourlyOverallVolume(filename=None):
    volumePair = None
    if filename is not None:
        volumePair = doHourlyOverallCount(filename)
    else:
        print("Warning: input incoming file is ignored")

    return volumePair


def getHourlyOverallVolume_AsString(hour, inComing=None):
    (srcVolume, dstVolume) = getHourlyOverallVolume(inComing, )

    return "%02d\t%d\t%d\n" % (hour, srcVolume, dstVolume)


if __name__ == '__main__':
    sampleFile = "../../data/sampleFileCONN.log"
    print(getHourlyOverallVolume_AsString(0, sampleFile))