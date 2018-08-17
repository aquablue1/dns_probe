"""
" Get the Row data of new appeared IPs
" Based on the result from ./getNewIPList.py
" dump the file to result/ScanCheck/%date/NewIPRow_%date_%hour.log
" By Zhengping on 2018-08-15
"""

from src.ScanCheck.getNewIPList import getNewIPList
from src.util.FileReader import fileReader
from src.util.DNSFieldLocMap import FieldToLoc
from src.util.FileWriter import fileWriter


def getNewIPRow(cookie, filenameA, filenameB, outputFilename):
    newIPList = getNewIPList(cookie, filenameA, filenameB)
    newIPList.sort()
    file = fileReader(filenameA)
    if "src" in cookie:
        fieldName = "srcIP"
    else:
        fieldName="dstIP"
    ret_str = ""
    for line in file:
        ip = line.split("\t")[FieldToLoc[fieldName]]
        if ip in newIPList:
            ret_str += "%s\n" % line

    outputF = fileWriter(outputFilename)
    outputF.writeString(ret_str)


if __name__ == '__main__':
    date = "2018-03-07"
    cookie = "srcIP"
    filenameA = "../../data/%s/outbound/%s_23.log" % (date, date)
    filenameB = "../../data/%s/outbound/%s_00.log" % (date, date)
    outputFilename = "../../result/ScanCheck/%s/NewIPRow_%s_23.log" % (date, date)
    getNewIPRow(cookie, filenameA, filenameB, outputFilename)
