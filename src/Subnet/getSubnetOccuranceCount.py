"""
" Count the occures of DNS Requests in each /16 subnets within our campus.
" As long as one session appears, its counting adds one.
"""

from src.util.FileReader import fileReader
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter


def doApperaedCount(filename, fieldCkecked):
    subnetPools = Counter()

    file = fileReader(filename)
    for line in file:
        IP = line.split("\t")[fieldCkecked]
        ThirdSubmet = int(IP.split(".")[2])
        subnetPools[ThirdSubmet] += 1

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


if __name__ == '__main__':
    filename = "../../data/sampleFileDNS.log"
    print(doSubnetAppearedCount(filename))