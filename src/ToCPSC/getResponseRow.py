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


def dumpDailyValidResponse(date):
    foldername = "../../result/ToCPSC/%s/" % (date) ## !! ## Modify from here.
    folder = folderReader(foldername)
    outputFoldername = "../../result/Response/ToCPSC/%s" % date
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
    dateList = ["2018-09-12"]
    cookie = "inbound"
    for date in dateList:
        dumpDailyValidResponse(date)

    # filename = "../../data/%s/inbound/%s_00.log" % (date, date)
    # # getHourlyValidResponse(filename)
    # outputFilename = "../../result/Response/%s/response_%s_00.log" % (date, date)
    # dumpHourlyesponseList(filename, outputFilename)