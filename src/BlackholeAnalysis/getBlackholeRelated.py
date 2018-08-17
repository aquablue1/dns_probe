"""
" Get the original Blackhole related traffic. Only consider outbound traffic.
" Only two popular blackhole IPs are covered, i.e.
" 192.33.14.30 & 192.175.48.6
" By Zhengping on 2018-08-11
"""

from src.util.FolderReader import folderReader
from src.util.FileReader import fileReader
from src.util.FileWriter import batchFileWriter
from src.util.DNSFieldLocMap import FieldToLoc


def doHourlyCPSCRelatedGen(inputFilename):
    inputFile = fileReader(inputFilename)
    dstIPs = ["192.33.14.30", "192.175.48.6"]
    ret_list = []
    for line in inputFile:
        queriedName = line.split("\t")[FieldToLoc["dstIP"]]
        if queriedName in dstIPs:
            ret_list.append(line)
    return ret_list


def doDailyCPSCRelatedGen(inputFolder, outputFolder):
    filenames = folderReader(inputFolder, date)
    outputHandler = batchFileWriter(outputFolder)
    for filename in filenames:
        outputFilename = "BlackholeRow_%s" % filename.split("/")[-1]
        hourlyRowData = doHourlyCPSCRelatedGen(filename)
        for line in hourlyRowData:
            outputHandler.writeString(outputFilename, line+"\n")



if __name__ == '__main__':
    date = "2018-03-07"
    inputFolder = "../../data/%s/outbound/" % date
    outputFolder = "../../result/Blackhole/%s/" % date

    doDailyCPSCRelatedGen(inputFolder, outputFolder)
