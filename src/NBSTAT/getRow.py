"""
" Get the Source of NBSTAT realted DNS Traffic
" By Zhengping on 2018-11-05
"""


from src.util.FolderReader import folderReader
from src.util.FileReader import fileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
import os


def getHourlyNBSTATRow(filename, NBSTATFoldername):
    file = fileReader(filename)
    NBSTATFilename = NBSTATFoldername + "/" + filename.split("/")[-1]
    dump_str = ""
    for line in file:
        type = line.split("\t")[FieldToLoc["type"]]
        if type=="NBSTAT":
            dump_str += (line + "\n")
    campusFile = fileWriter(NBSTATFilename)
    campusFile.writeString(dump_str)


def getDailyNBSTATRow(foldername, NBSTATFoldername):
    folder = folderReader(foldername)
    for filename in folder:
        getHourlyNBSTATRow(filename, NBSTATFoldername)
        print("Done - %s" % filename)

if __name__ == '__main__':
    # date = "2018-03-07"
    dateList = ["2018-09-10", "2018-09-11", "2018-09-12",
                "2018-09-13", "2018-09-14", "2018-09-15", ]
    # dateList = ["2018-08-13", "2018-09-12"]
    # dateList = ["2018-06-27", "2018-07-04"]
    # dateList = ["2018-09-09"]
    for date in dateList:
        foldername = "../../data/%s/inbound/" % date
        NBSTATFoldername = "../../result/NBSTAT/%s/" % date
        if not os.path.exists(NBSTATFoldername):
            os.makedirs(NBSTATFoldername)
        getDailyNBSTATRow(foldername, NBSTATFoldername)