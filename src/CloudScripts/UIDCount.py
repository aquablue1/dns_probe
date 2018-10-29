"""
" Scripts used to count the number of Unique ID in both DNS and CONN files.
" Output the result in one single file.
" By Zhengping on 2018-10-22
"""

import gzip
import os
from datetime import datetime
from collections import Counter


def write_to_log(log_filename, info):
    """
    write runtime log.
    :param log_filename:
    :param info:
    :return:
    """
    f = open(log_filename, "a")
    f.write("== Time: %s ==\n" % datetime.now())
    f.write(str(info) + "\n")
    f.close()


def doUIDCollect(filename, cookie=None):
    with gzip.open(filename, 'rb') as f:
        if cookie == "conn":
            count = 0
            for line in f:
                if line[0] == "#":
                    continue
                line_list = line.split("\t")
                if line_list[7] == "dns":
                    count += 1
            return count
        elif cookie == "dns":
            c = Counter()
            for line in f:
                if line[0] == "#":
                    continue
                line_list = line.split("\t")
                uid = line_list[1]
                c[uid] += 1
            return len(c)


def output_String(OutputString, outputFilename):
    with open(outputFilename, 'a') as f:
        f.write(OutputString+"\n")


if __name__ == '__main__':
    data_folder = "/data3/"
    date_format = '%Y-%M-%d'
    search_key = "2018-09-19"

    search_key_list = ["2018-06-28", "2018-06-29", "2018-06-30", "2018-07-01", "2018-07-02", "2018-07-03"]
    search_key_list = ["2018-09-12"]
    search_hour = "12"

    log_file = "../runtimeInfo_UIDCount_%s.log" % search_key
    outputDict = {}
    for i in range(24):
        key = "%02d" % i
        outputDict[key] = [0, 0]
    if not os.path.exists("../result/result_UIDCount/"):
        os.makedirs("../result/result_UIDCount/")
    for search_key in search_key_list:
        output_filename = "../result/result_UIDCount/%s.log" % (search_key)
        for daily_folder in os.listdir(data_folder):
            if os.path.isdir(data_folder + daily_folder) and search_key in daily_folder:
                date = daily_folder
                write_to_log(log_file, "Now Inside: %s" % daily_folder)
                yyyymm = year_month = date[0:7]
                for trace_filename in os.listdir(data_folder + daily_folder + "/"):
                    if "dns.%s" % search_hour in trace_filename:
                        inbound_list_tmp = []
                        hour = trace_filename[4:6]
                        write_to_log(log_file, "Start searching in DNS file --> %s" % trace_filename)
                        DNSCount = doUIDCollect(data_folder + daily_folder + "/" + trace_filename, "dns")
                        outputDict[hour][0] += DNSCount
                    if "conn.%s" % search_hour in trace_filename:
                        inbound_list_tmp = []
                        hour = trace_filename[5:7]
                        write_to_log(log_file, "Start searching in DNS file --> %s" % trace_filename)
                        CONNCount = doUIDCollect(data_folder + daily_folder + "/" + trace_filename, "conn")
                        outputDict[hour][1] += CONNCount
                print(outputDict)
                output_String("#\tHour\tDNS UID Count\tCONN UID Count\n", output_filename)
                for hour in outputDict.keys():
                    outputStr = "%s\t%d\t%d\n" % (hour, outputDict[hour][0], outputDict[hour][1])
                    output_String(outputStr, output_filename)



