"""
" Count the distinct reverse DNS and normal DNS.
" Accept the /result/ToCPSCAnalysis/nameCounter_%date.log as input.
" return the count of both reverse DNS and normal DNS
" By Zhengping on 2018-08-15
"""

from src.util.FileReader import fileReader


def getReverseCount(filename):
    file = fileReader(filename)
    reverseCount = 0
    normCount = 0
    for line in file:
        name = line.split("\t")[0]
        if ".arpa" in name:
            reverseCount += 1
        else:
            normCount += 1
    return "Reverse DNS Count: %d.\tNorm DNS Count: %d\n" % (reverseCount, normCount)

def getReversePrivateCount(filename):
    file = fileReader(filename)
    campusCount = 0
    privateCount = 0
    for line in file:
        name = line.split("\t")[0]
        if "159.136" in name:
            campusCount += 1
        elif "10" in name or "192" in name or "172" in name:
            privateCount += 1
    return "Campus DNS Count: %d.\tPrivate DNS Count: %d\n" % (campusCount, privateCount)

if __name__ == '__main__':
    date = "2018-03-07"
    filename = "../../result/ToCPSC/ReverseAnalysis/reverseDNSToRow_NS2_%s_queryCounter.log" % date
    print(getReversePrivateCount(filename))