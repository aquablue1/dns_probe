"""
" Get the overall sessions that goes to the campus New hosts (i.e. 136.159.222.2/10)
"""

from src.util.FolderReader import folderReader
from src.util.FileReader import fileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
import os


def getHourlyCampusNewRow(filename, CampusNewFoldername):
    file = fileReader(filename)
    CampusNewFilename = CampusNewFoldername + "/" + filename.split("/")[-1]
    CampusNewDNSList = ["136.159.222.2", "136.159.222.10"]
    dump_str = ""
    for line in file:
        dstIP = line.split("\t")[FieldToLoc["dstIP"]]
        if dstIP in CampusNewDNSList:
            dump_str += (line + "\n")
    CampusNewFile = fileWriter(CampusNewFilename)
    CampusNewFile.writeString(dump_str)


def getDailyCampusNewRow(foldername, CampusNewFoldername):
    folder = folderReader(foldername)
    for filename in folder:
        getHourlyCampusNewRow(filename, CampusNewFoldername)
        print("Done - %s" % filename)

if __name__ == '__main__':
    date = "2018-09-09"
    foldername = "../../data/%s/inbound/" % date
    CampusNewFoldername = "../../result/ToCampusNew/%s/" % date
    if not os.path.exists(CampusNewFoldername):
        os.makedirs(CampusNewFoldername)
    getDailyCampusNewRow(foldername, CampusNewFoldername)