"""
" Get the record with valid response of DNS query.
" Based on the code from src/Response/getValidResponseRow.py
" By Zhengping on 2018-10-16
"""


from src.util.FileReader import fileReader
from src.util.FileWriter import fileWriter
from src.util.FolderReader import folderReader
from src.util.DNSFieldLocMap import FieldToLoc
import os


def getHourlyValidResponse(filename):
    file = fileReader(filename)
    responseLineList = []
    for line in file:
        response = line.split("\t")[FieldToLoc["answers"]]
        if response != "-":
            responseLineList.append(line+"\n")
    return responseLineList


def dumpDailyValidResponse(taskName, date):
    foldername = "../../result/%s/%s/" % (taskName, date)
    folder = folderReader(foldername)
    outputFoldername = "../../result/Response/%s/%s" % (taskName, date)
    if not os.path.exists(outputFoldername):
        os.makedirs(outputFoldername)
    for filename in folder:
        absFilename = filename.split("/")[-1]
        outputFilename = "%s/response_%s" % (outputFoldername, absFilename)
        print("Start dumping %s" % outputFilename)
        dumpHourlyesponseList(filename, outputFilename)


def dumpHourlyesponseList(filename, outputFilename):
    responseLineList = getHourlyValidResponse(filename)
    outputFile = fileWriter(outputFilename)
    outputStr = ""
    for responseLine in responseLineList:
        outputStr = outputStr + responseLine
    outputFile.writeString(outputStr)


if __name__ == '__main__':
    date = "2018-09-11"
    dateList = ["2018-09-11", "2018-09-12", "2018-09-13"]
    dateList = ["2018-09-16","2018-09-17","2018-09-18"]
    cookieList = ["205Unknown", "Akamai", "Auroral",
                  "CampusNew", "CampusOne", "CampusTwo",
                  "CPSC",
                  # "Phys", "Other"
                 ]

    for date in dateList:
        for cookie in cookieList:
            taskName = "To%s" % cookie
            dumpDailyValidResponse(taskName, date)

    # filename = "../../data/%s/inbound/%s_00.log" % (date, date)
    # # getHourlyValidResponse(filename)
    # outputFilename = "../../result/Response/%s/response_%s_00.log" % (date, date)
    # dumpHourlyesponseList(filename, outputFilename)