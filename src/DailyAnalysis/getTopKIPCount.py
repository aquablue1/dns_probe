"""
" Get the selected dict of topK IPs and its count
" By Zhengping on 2018-08-09
"""
import os
from src.util.FileReader import fileReader
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter


def doIPOccuranceCount(filename, fieldName):
    """
    Get the counter of distinct IPs in the given file
    :param filename: input file name, should be normal DNS log
    :param fieldName: FieldName of IP specified, must be either srcIP or dstIP
    :return: counter object of IPs
    """
    file = fileReader(filename)
    nameCounter = Counter()
    for line in file:
        name = line.split("\t")[FieldToLoc[fieldName]]
        nameCounter[name] += 1
    return nameCounter


def doTopKIPCount(filename, fieldName, k):
    """
    return the result of top-k count as a dict
    :param filename: input DNS filename
    :param fieldName: FieldName of IP specified, must be either srcIP or dstIP
    :param k: the K of top specified
    :return: topK as a dict
    """
    nameCounter = doIPOccuranceCount(filename, fieldName)
    # topKDict = {}
    # for key in sorted(nameCounter, key=lambda k: nameCounter[k], reverse=True):
        # if k <= 0:
            # break
        # k -= 1
        # topKDict[key] = nameCounter[key]
    return nameCounter.most_common(k)


def getTopKNameCount(inComing=None, outGoing=None, k=0):
    inTopKSrcIP = None
    inTopKDstIP = None
    outTopSrcIP = None
    outTopDstIP = None

    if inComing is not None:
        fieldName = "srcIP"
        inTopKSrcIP = doTopKIPCount(inComing, fieldName, k)
        fieldName = "dstIP"
        inTopKDstIP = doTopKIPCount(inComing, fieldName, k)
    if outGoing is not None:
        fieldName = "srcIP"
        outTopSrcIP = doTopKIPCount(outGoing, fieldName, k)
        fieldName = "dstIP"
        outTopDstIP = doTopKIPCount(outGoing, fieldName, k)

    return inTopKSrcIP, inTopKDstIP, outTopSrcIP, outTopDstIP


if __name__ == '__main__':
    sampleFile = "../../data/sampleFileDNS.log"
    print(getTopKNameCount(sampleFile, sampleFile, 2))