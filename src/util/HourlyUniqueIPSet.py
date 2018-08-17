"""
" Get a set of unique IP appeared in an hourly data.
" Accept two params: 1. cookie to identify inbound/outbound.
" 2. filename that stores the hourly data
" return the unique IP set
" By Zhengping on 2018-08-15
"""

from src.util.FileReader import fileReader
from src.util.DNSFieldLocMap import FieldToLoc


def getUniqueIPSet(cookie, filename):
    if "src" in cookie:
        fieldName = "srcIP"
    elif "dst" in cookie:
        fieldName = "dstIP"
    else:
        raise ValueError("invalid input cookie %s" % cookie)
    file = fileReader(filename)
    uniqIPSet = set()
    for line in file:
        ip = line.split("\t")[FieldToLoc[fieldName]]
        uniqIPSet.add(ip)

    return uniqIPSet