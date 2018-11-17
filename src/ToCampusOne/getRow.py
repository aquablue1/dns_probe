"""
" Get the overall sessions that goes to one of the Campus level DNS server (ip: 136.159.1.21)
"""

from src.util.FolderReader import folderReader
from src.util.FileReader import fileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
import os


def getHourlyCampusOneRow(filename, campusOneFoldername):
    file = fileReader(filename)
    campusOneFilename = campusOneFoldername + "/" + filename.split("/")[-1]
    campusOneDNSList = ["136.159.1.21"]
    dump_str = ""
    for line in file:
        dstIP = line.split("\t")[FieldToLoc["dstIP"]]
        if dstIP in campusOneDNSList:
            dump_str += (line + "\n")
    campusFile = fileWriter(campusOneFilename)
    campusFile.writeString(dump_str)


def getDailyCampusOneRow(foldername, campusOneFoldername):
    folder = folderReader(foldername)
    for filename in folder:
        getHourlyCampusOneRow(filename, campusOneFoldername)
        print("Done - %s" % filename)

if __name__ == '__main__':
    # date = "2018-03-07"
    dateList = ["2018-09-09", "2018-09-10", "2018-09-11", "2018-09-12",
                "2018-09-13", "2018-09-14", "2018-09-15", ]
    dateList = ["2018-06-27", "2018-07-04"]
    dateList = ["2018-09-09"]
    for date in dateList:
        foldername = "../../data/%s/inbound/" % date
        campusOneFoldername = "../../result/ToCampusOne/%s/" % date
        if not os.path.exists(campusOneFoldername):
            os.makedirs(campusOneFoldername)
        getDailyCampusOneRow(foldername, campusOneFoldername)