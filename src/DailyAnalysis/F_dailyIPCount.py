"""
" Get the daily statistics of DNS requests' IP counting
" Including 1. Total distinct incoming src IPs
            2. Total distinct incoming dst IPs
            3. Total distinct outgoing src IPs
            4. Total distinct outgoing dst IPs
" By zhengping on 2018-08-09
"""

from src.util.FolderReader import folderReader
from src.DailyAnalysis.getHourlyIPCount import getHourlyIPCount


def folderNameGen(date, direction):
    return "../../data/%s/%sbound" % (date, direction)


def getDailyIPCount(date):
    inComingFiles = folderReader(folderNameGen(date, "in"))
    outGoingFiles = folderReader(folderNameGen(date, "out"))
    dailyStatistics = ""
    for inComing, outGoing, hour in zip(inComingFiles, outGoingFiles, range(24)):
        print(inComing,outGoing)
        inSrc, inDst, outSrc, outDst = getHourlyIPCount(inComing, outGoing)
        dailyStatistics += "%02d\t%d\t%d\t%d\t%d\n" % (hour, inSrc, inDst, outSrc, outDst)
        # print(dailyStatistics)
    return dailyStatistics


if __name__ == '__main__':
    date = "2018-03-07"
    outputFilename = "../../result/dailyIPCount_%s.log" % date
    outputF = open(outputFilename, 'a')
    outputF.write(getDailyIPCount(date))
    outputF.close()
