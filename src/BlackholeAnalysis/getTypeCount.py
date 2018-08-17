"""
" Count the distinct query types of the queries to DNS black hole.
" By Zhengping on 2018-03-13
"""

from src.util.FileReader import fileReader
from src.util.FolderReader import folderReader
from src.util.DNSFieldLocMap import FieldToLoc
from collections import Counter


def getHourlyCount(filename):
    file = fileReader(filename)
    typeCounter = Counter()
    for line in file:
        type = line.split("\t")[FieldToLoc["type"]]
        typeCounter[type] += 1
    return typeCounter


def getDailyCount(foldername):
    folder = folderReader(foldername)
    typeCounter = Counter()
    for filename in folder:
        typeCounter += getHourlyCount(filename)
    return typeCounter


if __name__ == '__main__':
    date = "2018-03-07"
    foldername = "../../result/Blackhole/%s/" % date
    print(getDailyCount(foldername))