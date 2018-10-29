"""
" Load the IP to org cache.
" By Zhengping on 2018-08-15
"""

from src.util.FileReader import fileReader
from src.util.IsFileExist import isFileExist

def getCache(filename):
    if not isFileExist(filename):
        return None
    file = fileReader(filename)
    ipOrgDict = {}
    for line in file:
        if len(line.split("\t")) > 1:
            [ip, org] = line.split("\t")
            ipOrgDict[ip] = org
    print(ipOrgDict)
    return ipOrgDict


if __name__ == '__main__':
    filename = "../../result/ToCPSC/srcIPOrg_2018-03-07.log"
    print(getCache(filename))