"""
" Get the original CPSC related DNS traffic from original data files.
" Since CPSC DNS (ns1/2.cpsc.ucalgary.ca) mostly involved in the inbound traffic.
" Therefore only the inbound traffic is considered.
" By Zhengping on 2018-08-10
"""

from src.util.FolderReader import folderReader
from src.util.FileReader import fileReader
from src.util.FileWriter import batchFileWriter
from src.util.DNSFieldLocMap import FieldToLoc
import os


def doHourlyCPSCRelatedGen(inputFilename):
    inputFile = fileReader(inputFilename)
    checkedNames = ["ns1.cpsc.ucalgary.ca", "ns2.cpsc.ucalgary.ca", "mirror.cpsc.ucalgary.ca"]
    ret_list = []
    for line in inputFile:
        queriedName = line.split("\t")[FieldToLoc["query"]]
        if queriedName in checkedNames:
            ret_list.append(line)
    return ret_list


def doDailyCPSCRelatedGen(inputFolder, outputFolder):
    filenames = folderReader(inputFolder, date)
    outputHandler = batchFileWriter(outputFolder)
    for filename in filenames:
        outputFilename = "CPSCRow_%s" % filename.split("/")[-1]
        hourlyRowData = doHourlyCPSCRelatedGen(filename)
        for line in hourlyRowData:
            outputHandler.writeString(outputFilename, line+"\n")



if __name__ == '__main__':
    date = "2018-07-01"
    inputFolder = "../../data/%s/inbound" % date
    outputFolder = "../../result/CPSCRow/%s/" % date
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)
    doDailyCPSCRelatedGen(inputFolder, outputFolder)
