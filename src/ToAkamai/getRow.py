"""
" Get the overall sessions that goes to the akamai hosts (i.e. 136.159.222.244)
"""

from src.util.FolderReader import folderReader
from src.util.FileReader import fileReader
from src.util.FileWriter import fileWriter
from src.util.DNSFieldLocMap import FieldToLoc
import os


def getHourlyAkamaiRow(filename, AkamaiFoldername):
    file = fileReader(filename)
    AkamaiFilename = AkamaiFoldername + "/" + filename.split("/")[-1]
    AkamaiDNSList = ["136.159.222.244"]
    dump_str = ""
    for line in file:
        dstIP = line.split("\t")[FieldToLoc["dstIP"]]
        if dstIP in AkamaiDNSList:
            dump_str += (line + "\n")
    AkamaiFile = fileWriter(AkamaiFilename)
    AkamaiFile.writeString(dump_str)


def getDailyAkamaiRow(foldername, AkamaiFoldername):
    folder = folderReader(foldername)
    for filename in folder:
        getHourlyAkamaiRow(filename, AkamaiFoldername)
        print("Done - %s" % filename)

if __name__ == '__main__':
    date = "2018-09-12"
    foldername = "../../data/%s/inbound/" % date
    AkamaiFoldername = "../../result/ToAkamai/%s/" % date
    if not os.path.exists(AkamaiFoldername):
        os.makedirs(AkamaiFoldername)
    getDailyAkamaiRow(foldername, AkamaiFoldername)