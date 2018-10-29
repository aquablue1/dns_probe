"""
" Get the row reverse DNS data from original CPSC DNS traffic.
" Filter based on the cookie ".in-addr.arpa"
" Dump all data into two files, each file correspond to one destination DNS server.
" Because there is evidence shows that these two DNS servers have different PTR behaviors.
" By Zhengping on 2018-08-19
"""

from src.util.FileReader import fileReader
from src.util.FolderReader import folderReader
from src.util.DNSFieldLocMap import FieldToLoc
from src.util.FileWriter import fileWriter


def getHourlyData_AsString(filename):
    file = fileReader(filename)
    ns1 = "136.159.2.1"
    ns2 = "136.159.2.4"
    cookie = ".in-addr.arpa"
    ret_str_ns1 = ""
    ret_str_ns2 = ""
    for line in file:
        if cookie in line.split("\t")[FieldToLoc["query"]]:
            # if it is reverse DNS query
            if line.split("\t")[FieldToLoc["dstIP"]] == ns1:
                # If it is reverse DNS query to ns1:
                ret_str_ns1 += (line + "\n")
            else:
                # Else, it is reverse quety to ns2.
                ret_str_ns2 += (line + "\n")
    return ret_str_ns1, ret_str_ns2


def dumpHourlyData(filename, ns1OutputFilename, ns2OutputFilename):
    ret_str_ns1, ret_str_ns2 = getHourlyData_AsString(filename)
    ns1OutputF = fileWriter(ns1OutputFilename)
    ns1OutputF.writeString(ret_str_ns1)
    ns2OutputF = fileWriter(ns2OutputFilename)
    ns2OutputF.writeString(ret_str_ns2)


def getDailyReverseDNSRow(foldername, outputFoldername, date):
    ns1OutputFilename = outputFoldername + "reverseDNSToRow_NS1_%s.log" % date
    ns2OutputFilename = outputFoldername + "reverseDNSToRow_NS2_%s.log" % date
    folder = folderReader(foldername)
    for filename in folder:
        dumpHourlyData(filename, ns1OutputFilename, ns2OutputFilename)


if __name__ == '__main__':
    date = "2018-03-07"
    foldername = "../../result/ToCPSC/%s/" % date
    outputFoldername = "../../result/ToCPSC/ReverseAnalysis/"
    getDailyReverseDNSRow(foldername, outputFoldername, date)
