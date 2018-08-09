"""
" Get the count of each distinct error type and its occurrence in each individual hour
" Two files are suggested as the input files.
" By Zhengping on 2018-08-08
"""

from src.util.FileReader import fileReader
from src.util.DNSFieldLocMap import FieldToLoc


def doEndingStatistics(filename):
    fieldName = "error"
    error_dict = {}
    file = fileReader(filename)
    for line in file:
        error = line.split("\t")[FieldToLoc[fieldName]]
        if error in error_dict.keys():
            error_dict[error] += 1
        else:
            error_dict[error] = 1
    return error_dict


def getEndingStatistics(filename=None):
    ErrorDict = None

    if filename is not None:
        ErrorDict = doEndingStatistics(filename)

    return ErrorDict


def getEndingStatistics_AsString(filename):
    ErrorDict = getEndingStatistics(filename)
    ret_str = ""
    for key in ErrorDict.keys():
        ret_str += ("%s\t%d\n" % (key, ErrorDict[key]))
    return ret_str


if __name__ == '__main__':
    sampleFile = "../../data/sampleFileDNS.log"
    print(getEndingStatistics_AsString(sampleFile))