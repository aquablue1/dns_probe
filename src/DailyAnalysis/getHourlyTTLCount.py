"""
" Get the hourly count of TTL based on DNS files.
" ignore those without a valid TTL number.
"By Zhengpingon 2018-08-09
"""

from src.util.DNSFieldLocMap import FieldToLoc
from src.util.FileReader import fileReader
from collections import Counter


def parseTTLVector(ttlVector):
    return [float(ttl) for ttl in ttlVector.split(",")]


def doHourlyTTLCount(filename):
    ttlCounter = Counter()
    file = fileReader(filename)
    for line in file:
        ttlVector = line.split("\t")[FieldToLoc["ttls"]]
        if ttlVector == "-":
            continue
        ttl_list = parseTTLVector(ttlVector)
        for ttl in ttl_list:
            ttlCounter[ttl] += 1
    return ttlCounter


def getHourlyTTLCount(filename):
    return doHourlyTTLCount(filename)


def getHourlyTTLCount_AsString(filename):
    ttlCounter = doHourlyTTLCount(filename)
    ret_str = ""
    for key in ttlCounter.keys():
        ret_str += "%.0f\t%d\n" % (key, ttlCounter[key])
    return ret_str


if __name__ == '__main__':
    filename = "../../data/sampleFileDNS.log"
    print(getHourlyTTLCount_AsString(filename))