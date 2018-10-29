"""
" Get the count of requests to CPSC servers by organization.
" Accept two types of files as input: 1. the IP to organization files.
" 2. The IP and its counting.
" For each organization in IP-Org files, get the count based on IP-Count files. The add the count.
" By Zhengping on 2018-08-17
"""

from src.util.FileReader import fileReader
from src.util.FolderReader import folderReader
from src.util.FileWriter import fileWriter
from collections import Counter, OrderedDict


def getIPCountDict(filename):
    file = fileReader(filename)
    ipCountDict = {}
    for line in file:
        ip = line.split("\t")[0]
        count = int(line.split("\t")[1])
        ipCountDict[ip] = count
    return ipCountDict


def getIPOrgDict(foldername, date):
    folder = folderReader(foldername)
    ipOrgDict = {}
    for filename in folder:
        if "srcIPOrg_" in filename and date in filename:
            file = fileReader(filename)
            for line in file:
                if (len(line.split("\t"))) < 2:
                    continue
                ip = line.split("\t")[0]
                org = line.split("\t")[1]
                ipOrgDict[ip] = org

    return ipOrgDict


def getDailyOrgCount(ipCountFilename, orgIPFoldername, date):
    ipCountDict = getIPCountDict(ipCountFilename)
    ipOrgDict = getIPOrgDict(orgIPFoldername, date)
    orgCounter = Counter()
    for ip in ipOrgDict.keys():
        orgCounter[ipOrgDict[ip]] += ipCountDict[ip]
    return orgCounter


def getDailyOrgCount_AsString(ipCountFilename, orgIPFoldername, date):
    orgCounter = getDailyOrgCount(ipCountFilename, orgIPFoldername, date)
    orgCounter = OrderedDict(orgCounter.most_common())
    ret_str = ""
    for org in orgCounter.keys():
        ret_str += "%s\t%d\n" % (org, orgCounter[org])
    return ret_str


def dumpDailyOrgCount(outputFoldername, ret_str, date):
    outputFilename = outputFoldername + "dailyOrgCount_%s.log" % date
    outputF = fileWriter(outputFilename)
    outputF.writeString(ret_str)




if __name__ == '__main__':
    date = "2018-03-07"
    ipCountFilename = "../../result/ToCPSC/ReverseAnalysis/reverseDNSToRow_NS1_%s_srcIPCounter.log" % date

    orgIPFoldername = "../../result/ToCPSC/ReverseAnalysis/"

    ret_str = getDailyOrgCount_AsString(ipCountFilename, orgIPFoldername, date)
    dumpDailyOrgCount(orgIPFoldername, ret_str, date)

