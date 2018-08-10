"""
" Count the appearance of IPs in each /16 subnets within our campus.
" As long as one IP appears, it is only count as once.
"""

from src.util.FileReader import fileReader
from src.util.DNSFieldLocMap import FieldToLoc


def doApperaedCount(filename, fieldCkecked):
    subnetPools = {}
    for subnet in range(256):
        subnetPools[subnet] = set()

    file = fileReader(filename)
    for line in file:
        IP = line.split("\t")[fieldCkecked]
        ThirdSubmet = int(IP.split(".")[2])
        subnetPools[ThirdSubmet].add(IP)

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


if __name__ == '__main__':
    filename = "../../data/sampleFileDNS.log"
    print(doSubnetAppearedCount(filename))