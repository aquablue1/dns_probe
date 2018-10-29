"""
" Get the overall sessions that goes to the 205 Unknown hosts (i.e. 136.159.205.37/38/39)
"""

from src.util.FolderReader import folderReader
from src.util.FileReader import fileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
import os


def getHourlyUnknownRow(filename, UnknownFoldername):
    file = fileReader(filename)
    UnknownFilename = UnknownFoldername + "/" + filename.split("/")[-1]
    UnknownDNSList = ["136.159.205.37", "136.159.205.38", "136.159.205.39"]
    dump_str = ""
    for line in file:
        dstIP = line.split("\t")[FieldToLoc["dstIP"]]
        if dstIP in UnknownDNSList:
            dump_str += (line + "\n")
    UnknownFile = fileWriter(UnknownFilename)
    UnknownFile.writeString(dump_str)


def getDaily205UnknownRow(foldername, UnknownFoldername):
    folder = folderReader(foldername)
    for filename in folder:
        getHourlyUnknownRow(filename, UnknownFoldername)
        print("Done - %s" % filename)

if __name__ == '__main__':
    date = "2018-09-12"
    foldername = "../../data/%s/inbound/" % date
    unknownFoldername = "../../result/To205Unknown/%s/" % date
    if not os.path.exists(unknownFoldername):
        os.makedirs(unknownFoldername)
    getDaily205UnknownRow(foldername, unknownFoldername)