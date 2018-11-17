"""
" General Analysis script. Take the input from all ToXXX folders.
" Output the count of lines (valid number of sessions)
" By Zhengping on 2018-11-15
"""

# import sys
# sys.path.append('/home/grads/zhang.zhengping/DNS/DNSPythonWorkSpace')
from src.util.FolderReader import folderReader
from src.util.FileReader import fileReader
from src.util.FileLineCounter import lineCount
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
import os


def __exp_getHourlyCount(filename):
    # Expired because of duplication problem in some files [FROM 2018-09-18_21 TO 2018-09-24_09]
    return lineCount(filename)


def __exp_getDailyCount(date, cookie):
    foldername = "../../result/To%s/%s" % (cookie, date)
    folder = folderReader(foldername)
    countDict = {}
    for filename in folder:
        countDict[filename[-6:-4]] = __exp_getHourlyCount(filename)
    return countDict


def getHourlyCount(filename):
    file = fileReader(filename)
    traceSet = set()
    for line in file:
        lineList = line.strip().split("\t")
        info = lineList[FieldToLoc["uid"]] + lineList[FieldToLoc["srcIP"]] + lineList[FieldToLoc["srcPort"]] + \
            lineList[FieldToLoc["dstIP"]] + lineList[FieldToLoc["transID"]] + lineList[FieldToLoc["query"]]
        traceSet.add(info)
    return len(traceSet)


def getDailyCount(date, cookie):
    foldername = "../../result/To%s/%s" % (cookie, date)
    folder = folderReader(foldername)
    countDict = {}
    for filename in folder:
        countDict[filename[-6:-4]] = getHourlyCount(filename)
    return countDict


def dumpDailyCount(date, cookie):
    countDict = getDailyCount(date, cookie)
    __exp_countDict = __exp_getDailyCount(date, cookie)
    str_out = ""
    # Get filtered result
    for hour in sorted(countDict.keys()):
        str_out += "%s\t%d\n" % (hour, countDict[hour])
    # Get original result
    for hour in countDict.keys():
        str_out += "%s\t%d\n" % (hour, __exp_countDict[hour])
    # dump/write result
    outputFoldername = "../../result_summary/connectionCount/To%s/" % (cookie)
    if not os.path.exists(outputFoldername):
        os.makedirs(outputFoldername)
    outputFilename = outputFoldername + "%s.log" % (date)
    outputFile = fileWriter(outputFilename)
    outputFile.writeString(str_out)


def batchedAnalysis(dateList, cookieList):
    for cookie in cookieList:
        for date in dateList:
            dumpDailyCount(date, cookie)
            print("Done - %s_%s" % (cookie, date))


if __name__ == '__main__':
    # cookie = "CampusNew"
    dateList = ["2018-09-%s" % (str(day).zfill(2)) for day in range(1, 31)]

    cookieList = ["Phys", "Auroral", "CampusNew",
                  "CampusOne", "CampusTwo", "CPSC",
                  "Other", "Akamai", "205Unknown"]
    batchedAnalysis(dateList, cookieList)
    # dumpDailyCount("2018-09-19", "Phys")