"""
" Get the counter of each provided hourly record files.
" Receive a line_list as input.
" By Zhengping on 2018-08-08
"""

from src.util.FileLineCounter import lineCount


def getHourlyOverallCount(inComing=None, outGoing=None):
    inCount = -1
    outCount = -1
    sumCount = -1
    if inComing is not None:
        inCount = lineCount(inComing)
    else:
        print("Warning: input incoming file is ignored")

    if outGoing is not None:
        outCount = lineCount(outGoing)
    else:
        print("Warning: input outgoing file is ignored")
    sumCount = inCount + outCount
    return sumCount, inCount, outCount


def getHourlyOverallCount_AsString(hour, inComing=None, outGoing=None):
    sumCount, inCount, outCount = \
        getHourlyOverallCount(inComing, outGoing)

    return "%02d\t%s\t%s\t%s\n" % (hour, sumCount, inCount, outCount)


if __name__ == '__main__':
    sampleFile = "../../data/sampleFileDNS.log"
    print(getHourlyOverallCount_AsString(0, sampleFile, sampleFile))