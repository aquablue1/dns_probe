import os
from src.util.FileReader import fileReader
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter


def doNameOccuranceCount(filename):
    """
    Get the counter of domains in the given file
    :param filename: input file name, should be normal DNS log
    :return: counter object of distinct names
    """
    file = fileReader(filename)
    fieldName = "query"
    nameCounter = Counter()
    for line in file:
        name = line.split("\t")[FieldToLoc[fieldName]]
        nameCounter[name] += 1
    return nameCounter


def doTopKNameCount(filename, k):
    """
    return the result of top-k count as a dict
    :param filename: input DNS filename
    :param k: the K of top specified
    :return: topK as a dict
    """
    topKDict = {}
    nameCounter = doNameOccuranceCount(filename)
    for key in sorted(nameCounter, key=lambda k: nameCounter[k], reverse=True):
        if k <= 0:
            break
        k -= 1
        topKDict[key] = nameCounter[key]
    return topKDict


def getTopKNameCount(inComing=None, outGoing=None, k=0):
    inTopKName = None
    outTopKName = None

    if inComing is not None:
        inTopKName = doTopKNameCount(inComing, k)
    if outGoing is not None:
        outTopKName = doTopKNameCount(outGoing, k)

    return inTopKName, outTopKName


if __name__ == '__main__':
    sampleFile = "../../data/sampleFileDNS.log"
    print(getTopKNameCount(sampleFile, None, 2))
