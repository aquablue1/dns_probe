"""
" Get the overall sessions that goes to the phys DNS servers (136.159.51.4, 136.159.51.5, 136.159.52.10)
"""

from src.util.FolderReader import folderReader
from src.util.FileReader import fileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
import os


def getHourlyPhysRow(filename, PhysFoldername):
    file = fileReader(filename)
    PhysFilename = PhysFoldername + "/" + filename.split("/")[-1]
    PhysDNSList = ["136.159.51.4", "136.159.51.5", "136.159.52.10"]
    dump_str = ""
    for line in file:
        dstIP = line.split("\t")[FieldToLoc["dstIP"]]
        if dstIP in PhysDNSList:
            dump_str += (line + "\n")
    PhysFile = fileWriter(PhysFilename)
    PhysFile.writeString(dump_str)


def getDailyPhysRow(foldername, PhysFoldername):
    folder = folderReader(foldername)
    for filename in folder:
        getHourlyPhysRow(filename, PhysFoldername)
        print("Done - %s" % filename)

if __name__ == '__main__':
    date = "2018-09-12"
    foldername = "../../data/%s/inbound/" % date
    PhysFoldername = "../../result/ToPhys/%s/" % date
    if not os.path.exists(PhysFoldername):
        os.makedirs(PhysFoldername)
    getDailyPhysRow(foldername, PhysFoldername)