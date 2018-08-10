"""
" Get the daily statistics of overall DNS counting
" Including 1. Total DNS requests
            2. Total incoming DNS requests
            3. Total outgoing DNS requests
" By zhengping on 2018-08-09
"""

from src.util.FolderReader import folderReader
from src.DailyAnalysis.getHourlyOverallCount import getHourlyOverallCount


def folderNameGen(date, direction):
    return "../../data/%s/%sbound" % (date, direction)


def getDailyOverallCount(date):
    inComingFiles = folderReader(folderNameGen(date, "in"))
    outGoingFiles = folderReader(folderNameGen(date, "out"))
    dailyStatistics = ""
    for inComing, outGoing, hour in zip(inComingFiles, outGoingFiles, range(24)):
        print(inComing,outGoing)
        totalCount, inCount, outCount = getHourlyOverallCount(inComing, outGoing)
        dailyStatistics += "%02d\t%d\t%d\t%d\n" % (hour, totalCount, inCount, outCount)
        # print(dailyStatistics)
    return dailyStatistics


if __name__ == '__main__':
    date = "2018-03-07"
    outputFilename = "../../result/dailyOverallCount_%s.log" % date
    outputF = open(outputFilename, 'a')
    outputF.write(getDailyOverallCount(date))
    outputF.close()
