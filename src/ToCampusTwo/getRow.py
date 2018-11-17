"""
" Get the overall sessions that goes to Two of the Campus level DNS server (ip: 136.159.1.21)
"""

from src.util.FolderReader import folderReader
from src.util.FileReader import fileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
import os


def getHourlyCampusTwoRow(filename, campusTwoFoldername):
    file = fileReader(filename)
    campusTwoFilename = campusTwoFoldername + "/" + filename.split("/")[-1]
    campusTwoDNSList = ["136.159.34.201"]
    dump_str = ""
    for line in file:
        dstIP = line.split("\t")[FieldToLoc["dstIP"]]
        if dstIP in campusTwoDNSList:
            dump_str += (line + "\n")
    campusFile = fileWriter(campusTwoFilename)
    campusFile.writeString(dump_str)


def getDailyCampusTwoRow(foldername, campusTwoFoldername):
    folder = folderReader(foldername)
    for filename in folder:
        getHourlyCampusTwoRow(filename, campusTwoFoldername)
        print("Done - %s" % filename)

if __name__ == '__main__':
    # date = "2018-03-07"
    dateList = ["2018-09-09", "2018-09-10", "2018-09-11", "2018-09-12",
                "2018-09-13", "2018-09-14", "2018-09-15", ]
    dateList = ["2018-08-13", "2018-09-12"]
    dateList = ["2018-06-27", "2018-07-04"]
    dateList = ["2018-09-09"]
    for date in dateList:
        foldername = "../../data/%s/inbound/" % date
        campusTwoFoldername = "../../result/ToCampusTwo/%s/" % date
        if not os.path.exists(campusTwoFoldername):
            os.makedirs(campusTwoFoldername)
        getDailyCampusTwoRow(foldername, campusTwoFoldername)