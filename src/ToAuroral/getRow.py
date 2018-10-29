"""
" Get the overall sessions that goes to the auroral host (i.e. 136.159.142.4/5)
"""

from src.util.FolderReader import folderReader
from src.util.FileReader import fileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
import os


def getHourlyAuroralRow(filename, AuroralFoldername):
    file = fileReader(filename)
    AuroralFilename = AuroralFoldername + "/" + filename.split("/")[-1]
    AuroralDNSList = ["136.159.142.4", "136.159.142.5"]
    dump_str = ""
    for line in file:
        dstIP = line.split("\t")[FieldToLoc["dstIP"]]
        if dstIP in AuroralDNSList:
            dump_str += (line + "\n")
    AuroralFile = fileWriter(AuroralFilename)
    AuroralFile.writeString(dump_str)


def getDailyAuroralRow(foldername, AuroralFoldername):
    folder = folderReader(foldername)
    for filename in folder:
        getHourlyAuroralRow(filename, AuroralFoldername)
        print("Done - %s" % filename)

if __name__ == '__main__':
    date = "2018-09-12"
    foldername = "../../data/%s/inbound/" % date
    AuroralFoldername = "../../result/ToAuroral/%s/" % date
    if not os.path.exists(AuroralFoldername):
        os.makedirs(AuroralFoldername)
    getDailyAuroralRow(foldername, AuroralFoldername)