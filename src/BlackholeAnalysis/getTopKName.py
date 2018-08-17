"""
" Get the top K popular domain names that queried to black hole DNS.
" Codes are updated from topKNameCount in DailyAnalysis
" By Zhengping on 2018-08-13
"""

from src.util.FileReader import fileReader
from src.util.FolderReader import folderReader
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


def getDailyNameCount(foldername):
    nameCounter = Counter()
    folder = folderReader(foldername)
    for filename in folder:
        nameCounter += doNameOccuranceCount(filename)
    return nameCounter.most_common(10)


if __name__ == '__main__':
    date = "2018-03-07"
    foldername = "../../result/Blackhole/%s/" % date
    print(getDailyNameCount(foldername))
