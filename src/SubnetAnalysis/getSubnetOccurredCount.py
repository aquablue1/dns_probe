"""
" Count the occures of DNS Requests in each /16 subnets within our campus.
" As long as one session appears, its counting adds one.
"""

from src.util.FileReader import fileReader
from src.util.FolderReader import folderReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter


def doOccurredCount(filename, fieldCkecked):
    subnetPools = Counter()

    file = fileReader(filename)
    for line in file:
        IP = line.split("\t")[fieldCkecked]
        ThirdSubmet = int(IP.split(".")[2])
        subnetPools[ThirdSubmet] += 1

    return subnetPools


def doSubnetOccurredCount(inComing=None, outGoing=None):
    inSubnetPools = None
    outSubnetPools = None
    if inComing is not None:
        inSubnetPools = doOccurredCount(inComing, FieldToLoc["dstIP"])
        # print(inSubnetPools)
    if outGoing is not None:
        outSubnetPools = doOccurredCount(outGoing, FieldToLoc["srcIP"])
        # print(outSubnetPools)
    return inSubnetPools, outSubnetPools


def getHourlySubnetOccurredCount(inComing, outGoing, inComingOutput, outGoingOutput):
    inSubnetPools, outSubnetPools = doSubnetOccurredCount(inComing, outGoing)
    inRet_str = ""
    outRet_str = ""
    if inSubnetPools is not None:
        for key in inSubnetPools.keys():
            inRet_str += "%d\t%d\n" % (key, inSubnetPools[key])
        outputF = fileWriter(inComingOutput)
        outputF.writeString(inRet_str)
    if outSubnetPools is not None:
        for key in outSubnetPools.keys():
            outRet_str += "%d\t%d\n" % (key, outSubnetPools[key])
        outputF = fileWriter(outGoingOutput)
        outputF.writeString(outRet_str)

    return inRet_str, outRet_str


def getDailySubnetAppendedCount(inFoldername, outFoldername, outputFoldername):
    inFolder = folderReader(inFoldername)
    outFolder = folderReader(outFoldername)
    for inComing, outGoing in zip(inFolder, outFolder):
        inComingOutputFilename = outputFoldername + "/inSubnet_%s" % inComing.split("/")[-1]
        outGoingOutputFilename = outputFoldername + "/outSubnet_%s" % outGoing.split("/")[-1]
        getHourlySubnetOccurredCount(inComing, outGoing, inComingOutputFilename, outGoingOutputFilename)


if __name__ == '__main__':
    date = "2018-03-07"
    inFoldername = "../../data/%s/inbound" % date
    outFoldername = "../../data/%s/outbound" % date
    outputFoldername = "../../result/SubnetCount/%s/occurred/" % date
    getDailySubnetAppendedCount(inFoldername, outFoldername, outputFoldername)
