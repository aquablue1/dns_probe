"""
" Read a file and return all the reverse dns queries.
" Return two lists, i.e. pure reverseList and dnsSDList.
" By Zhengping on 2018-08-13
"""

from src.util.FileReader import fileReader
from src.util.FolderReader import folderReader
from src.util.DNSFieldLocMap import FieldToLoc


def getReverse(filename):
    reverseCheckCookie = ".in-addr.arpa"
    dnsSDCheckCookie = "_dns-sd."
    reverseList = []
    dnsSDList = []
    file = fileReader(filename)
    for line in file:
        query = line.split("\t")[FieldToLoc["query"]]
        if reverseCheckCookie in query:
            if dnsSDCheckCookie in query:
                dnsSDList.append(line)
            else:
                reverseList.append(line)

    return reverseList, dnsSDList

def getDailyReverse(foldername):
    folder = folderReader(foldername)
    reverseLen = 0
    dnsSDLen = 0
    for filename in folder:
        reverse, dnsSD = getReverse(filename)
        reverseLen += len(reverse)
        dnsSDLen += len(dnsSD)
    print("Reverse length is %d, dnsSD length is %d" % (reverseLen, dnsSDLen))

if __name__ == '__main__':
    date = "2018-03-07"
    foldername = "../../result/Blackhole/%s/" % date
    getDailyReverse(foldername)