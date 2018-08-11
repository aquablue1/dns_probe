"""
" Count the appearance of IPs in each /16 subnets within our campus.
" As long as one IP appears, it is only count as once.
"""

from src.util.FileReader import fileReader
from src.util.DNSFieldLocMap import FieldToLoc
from src.util.FolderReader import folderReader
from src.util.FileWriter import fileWriter

def doApperaedCount(filename, fieldCkecked):
    subnetPools = {}
    for subnet in range(256):
        subnetPools[subnet] = set()

    file = fileReader(filename)
    for line in file:
        IP = line.split("\t")[fieldCkecked]
        ThirdSubnet = int(IP.split(".")[2])
        subnetPools[ThirdSubnet].add(IP)

    for subnet in subnetPools.keys():
        subnetPools[subnet] = len(subnetPools[subnet])

    return subnetPools


def doSubnetAppearedCount(inComing=None, outGoing=None):
    inSubnetPools = None
    outSubnetPools = None
    if inComing is not None:
        inSubnetPools = doApperaedCount(inComing, FieldToLoc["dstIP"])
        # print(inSubnetPools)
    if outGoing is not None:
        outSubnetPools = doApperaedCount(outGoing, FieldToLoc["srcIP"])
        # print(outSubnetPools)
    return inSubnetPools, outSubnetPools


def getHourlySubnetAppearedCount(inComing, outGoing, inComingOutput, outGoingOutput):
    inSubnetPools, outSubnetPools = doSubnetAppearedCount(inComing, outGoing)
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
        getHourlySubnetAppearedCount(inComing, outGoing, inComingOutputFilename, outGoingOutputFilename)


if __name__ == '__main__':
    date = "2018-03-07"
    inFoldername = "../../data/%s/inbound" % date
    outFoldername = "../../data/%s/outbound" % date
    outputFoldername = "../../result/SubnetCount/%s/appeared/" % date
    getDailySubnetAppendedCount(inFoldername, outFoldername, outputFoldername)