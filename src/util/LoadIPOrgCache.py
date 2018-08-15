"""
" Load the IP to org cache.
" By Zhengping on 2018-08-15
"""

from src.util.FileReader import fileReader



def getCache(filename):
    file = fileReader(filename)
    ipOrgDict = {}
    for line in file:
        [ip, org] = line.split("\t")
        ipOrgDict[ip] = org
    return ipOrgDict


if __name__ == '__main__':
    filename = "../../result/ToCPSCAnalysis/srcIPOrg_2018-03-07.log"
    print(getCache(filename))