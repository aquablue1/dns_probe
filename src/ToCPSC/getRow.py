"""
" Get the overall sessions that goes to the CPSC nses (i.e. 136.159.2.1 and 136.159.2.4)
"""

from src.util.FolderReader import folderReader
from src.util.FileReader import fileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
import os


def getHourlyCPSCRow(filename, cpscFoldername):
    file = fileReader(filename)
    cpscFilename = cpscFoldername + "/" + filename.split("/")[-1]
    cpscDNSList = ["136.159.2.1", "136.159.2.4"]
    dump_str = ""
    for line in file:
        dstIP = line.split("\t")[FieldToLoc["dstIP"]]
        if dstIP in cpscDNSList:
            dump_str += (line + "\n")
    cpscFile = fileWriter(cpscFilename)
    cpscFile.writeString(dump_str)


def getDailyCPSCRow(foldername, cpscFoldername):
    folder = folderReader(foldername)
    for filename in folder:
        getHourlyCPSCRow(filename, cpscFoldername)
        print("Done - %s" % filename)

if __name__ == '__main__':
    date = "2018-09-09"
    foldername = "../../data/%s/inbound/" % date
    cpscFoldername = "../../result/ToCPSC/%s/" % date
    if not os.path.exists(cpscFoldername):
        os.makedirs(cpscFoldername)
    getDailyCPSCRow(foldername, cpscFoldername)