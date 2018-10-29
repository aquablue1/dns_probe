"""
" Get the overall sessions that goes to the less lessPop campus DNS server
"""

from src.util.FolderReader import folderReader
from src.util.FileReader import fileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
import os


def getHourlylessPopRow(filename, lessPopFoldername):
    file = fileReader(filename)
    lessPopFilename = lessPopFoldername + "/" + filename.split("/")[-1]
    PopDNSList = ["136.159.222.2", "136.159.222.10",
                      "136.159.222.244",
                      "136.159.205.37", "136.159.205.38", "136.159.205.39",
                      "136.159.2.1", "136.159.2.4",
                      "136.159.1.21", "136.159.34.201",
                      "136.159.142.4", "136.159.142.5",
                      "136.159.51.4",  "136.159.51.5", "136.159.52.10"]
    dump_str = ""
    for line in file:
        dstIP = line.split("\t")[FieldToLoc["dstIP"]]
        if dstIP not in PopDNSList:
            dump_str += (line + "\n")
    lessPopFile = fileWriter(lessPopFilename)
    lessPopFile.writeString(dump_str)


def getDailyOtherRow(foldername, lessPopFoldername):
    folder = folderReader(foldername)
    for filename in folder:
        getHourlylessPopRow(filename, lessPopFoldername)
        print("Done - %s" % filename)

if __name__ == '__main__':
    date = "2018-09-12"
    foldername = "../../data/%s/inbound/" % date
    lessPopFoldername = "../../result/ToOther/%s/" % date
    if not os.path.exists(lessPopFoldername):
        os.makedirs(lessPopFoldername)
    getDailyOtherRow(foldername, lessPopFoldername)