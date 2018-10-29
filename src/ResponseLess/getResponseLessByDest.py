"""
" Get the record without any valid response (responseless) of DNS query.
" Based on the code from src/Response/getValidResponseRow.py
" By Zhengping on 2018-10-16
"""


from src.util.FileReader import fileReader
from src.util.FileWriter import fileWriter
from src.util.FolderReader import folderReader
from src.util.DNSFieldLocMap import FieldToLoc
import os


def getHourlyResponseLess(filename):
    file = fileReader(filename)
    responseLineList = []
    for line in file:
        response = line.split("\t")[FieldToLoc["answers"]]
        if response == "-":
            responseLineList.append(line+"\n")
    return responseLineList


def dumpDailyResponseLess(taskName, date):
    foldername = "../../result/%s/%s/" % (taskName, date)
    folder = folderReader(foldername)
    outputFoldername = "../../result/ResponseLess/%s/%s" % (taskName, date)
    if not os.path.exists(outputFoldername):
        os.makedirs(outputFoldername)
    for filename in folder:
        absFilename = filename.split("/")[-1]
        outputFilename = "%s/responseless_%s" % (outputFoldername, absFilename)
        print("Start dumping %s" % outputFilename)
        dumpHourlyesponseList(filename, outputFilename)


def dumpHourlyesponseList(filename, outputFilename):
    responseLineList = getHourlyResponseLess(filename)
    outputFile = fileWriter(outputFilename)
    outputStr = ""
    for responseLine in responseLineList:
        outputStr = outputStr + responseLine
    outputFile.writeString(outputStr)


if __name__ == '__main__':
    date = "2018-09-11"
    dateList = ["2018-09-11", "2018-09-10", "2018-09-09"]
    # dateList = ["2018-09-12", "2018-09-14","2018-09-15"]
    # dateList = ["2018-09-13"]

    # 205Unknown Case can be ignored, since it returns no valid response.
    cookieList = ["CampusTwo", "Auroral",
                  "CampusNew", "CampusOne",
                  "CPSC", "Phys", "Other",
                  # "205Unknown",
                  "Akamai", ]

    for date in dateList:
        for cookie in cookieList:
            taskName = "To%s" % cookie
            dumpDailyResponseLess(taskName, date)

    # filename = "../../data/%s/inbound/%s_00.log" % (date, date)
    # # getHourlyResponseLess(filename)
    # outputFilename = "../../result/Response/%s/response_%s_00.log" % (date, date)
    # dumpHourlyesponseList(filename, outputFilename)