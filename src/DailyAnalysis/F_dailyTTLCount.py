"""
" Get the TTL count of 24 hours in a give day.
" Export the result to an independent file for each hour.
" By Zhengping on 2018-08-09
"""

from src.util.FileWriter import batchFileWriter
from src.DailyAnalysis.getHourlyTTLCount import getHourlyTTLCount, getHourlyTTLCount_AsString
from src.util.FolderReader import folderReader

def doHourlyTTLCount(filename):
    return getHourlyTTLCount_AsString(filename)


def doDailyTTLCount_ByHour(date, inputFoldername, outputFoldername):
    inFolder = folderReader(inputFoldername, cookie=date)
    outHander = batchFileWriter(outputFoldername)
    for filename in inFolder:
        outputFilename = "TTLStatistics_%s" % filename.split("/")[-1]
        outHander.writeString(outputFilename, doHourlyTTLCount(filename), isOverWrite=True)
    return True


def getDailyTTLCount(date):
    inComingFolder = "../../data/%s/inbound" % date
    outGoingFolder = "../../data/%s/outbound" % date

    inComingOutputFolder = "../../result/TTLCount/inbound"
    outGoingOutputFolder = "../../result/TTLCount/outbound"

    doDailyTTLCount_ByHour(date, inComingFolder, inComingOutputFolder)
    doDailyTTLCount_ByHour(date, outGoingFolder, outGoingOutputFolder)


if __name__ == '__main__':
    date = "2018-03-07"
    getDailyTTLCount(date)