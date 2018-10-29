"""
" Get the row data of DNS response based on data/inbound/
" Ignore all the invisible response.
" By Zhengping on 2018-10-15
"""

from src.util.FileReader import fileReader
from src.util.FileWriter import fileWriter
from src.util.FolderReader import folderReader
from src.util.DNSFieldLocMap import FieldToLoc
import os


def getHourlyValidResponse(filename):
    file = fileReader(filename)
    responseList = []
    for line in file:
        response = line.split("\t")[FieldToLoc["answers"]]
        if response != "-":
            responseList.append(response)
    return responseList


def dumpDailyValidResponse(date, cookie):
    foldername = "../../data/%s/%s" % (date, cookie)
    folder = folderReader(foldername)
    outputFoldername = "../../result/Response/%s" % date
    if not os.path.exists(outputFoldername):
        os.makedirs(outputFoldername)
    for filename in folder:
        absFilename = filename.split("/")[-1]
        outputFilename = "%s/response_%s" % (outputFoldername, absFilename)
        print("Start dumping %s" % outputFilename)
        dumpHourlyesponseList(filename, outputFilename)


def dumpHourlyesponseList(filename, outputFilename):
    responseList = getHourlyValidResponse(filename)
    outputFile = fileWriter(outputFilename)
    outputStr = ""
    for response in responseList:
        outputStr = outputStr + response + "\n"
    outputFile.writeString(outputStr)


if __name__ == '__main__':
    date = "2018-09-11"
    dateList = ["2018-09-11", "2018-09-12", "2018-09-13"]
    dateList = ["2018-09-19"]
    cookie = "inbound"
    for date in dateList:
        dumpDailyValidResponse(date, cookie)

    # filename = "../../data/%s/inbound/%s_00.log" % (date, date)
    # # getHourlyValidResponse(filename)
    # outputFilename = "../../result/Response/%s/response_%s_00.log" % (date, date)
    # dumpHourlyesponseList(filename, outputFilename)