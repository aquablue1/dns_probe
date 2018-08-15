"""
" Get the organization info of all the source IPs which once sent request to CPSC DNS Servers.
" Required Inputfile: *srcCounter* file
" By Zhengping on 2018-08-14
"""

from src.GeneralAnalysis.IPListToOrg import ipListToOrg
from src.util.LoadIPOrgCache import getCache
from src.util.FileReader import fileReader
from src.util.FileWriter import fileWriter


def getOrgDict(ipList):
    cachedIPOrg = "../../result/ToCPSCAnalysis/srcIPOrg_2018-03-07.log"
    return ipListToOrg(ipList, getCache(cachedIPOrg))


def getSrcIPList(filename):
    file = fileReader(filename)
    ipList = []
    for line in file:
        queryCount = int(line.split("\t")[1])
        if queryCount > 50:
            ipList.append(line.split("\t")[0])

    return ipList


def dumpOrgDict(orgDict, outputFilename):
    outputF = fileWriter(outputFilename)
    ret_str = ""
    for ip in orgDict.keys():
        ret_str += "%s\t%s\n" % (ip, orgDict[ip])
        print("%s\t%s\n" % (ip, orgDict[ip]))
    outputF.writeString(ret_str)


if __name__ == '__main__':
    date = "2018-03-07"
    filename = "../../result/ToCPSCAnalysis/srcCounter_%s.log" % date
    outputFilename = "../../result/ToCPSCAnalysis/srcIPOrg_%s.log" % date
    srcOrgDict = getOrgDict(getSrcIPList(filename))
    print(srcOrgDict)
    print(dumpOrgDict(srcOrgDict, outputFilename))