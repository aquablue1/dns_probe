"""
" Get the list of IPs which new appeared.
" Provides two basic methods: 1. directly returns the new appeared list.
" 2. dump the new appeared list into a file.
"""

from src.util.SetMinus import setMinus
from src.util.HourlyUniqueIPSet import getUniqueIPSet
from src.util.FileWriter import fileWriter


def getNewIPList(cookie, filenameA, filenameB):
    ipListA = getUniqueIPSet(cookie, filenameA)
    ipListB = getUniqueIPSet(cookie, filenameB)
    return setMinus(ipListA, ipListB)


def dumpUniqueIPList(cookie, filenameA, filenameB, outputFilename):
    ipList = getNewIPList(cookie, filenameA, filenameB)
    outputF = fileWriter(outputFilename)
    ret_str = ""
    for ip in ipList:
        ret_str += "%s\n" % ip
    outputF.writeString(ret_str)


if __name__ == '__main__':
    date = "2018-03-07"
    cookie = "srcIP"
    filenameA = "../../data/%s/outbound/%s_23.log" % (date, date)
    filenameB = "../../data/%s/outbound/%s_00.log" % (date, date)
    print(len(getNewIPList(cookie, filenameA, filenameB)))