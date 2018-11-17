"""
" Check if the daily folder contains 24 files as required
" By Zhengping on 2018-11-10
"""

from src.util.FileReader import fileReader
from src.util.FolderReader import folderReader
import os


def doDailyCheck(date, cookieList):
    for cookie in cookieList:
        folder = "../../result/To%s/%s" % (cookie, date)
        try:
            count = len(os.listdir(folder))
        except FileNotFoundError as e:
            print(e)
        if count != 24:
            print("Date: %s,\tCookie: %s,:\tCount: %d" % (date, cookie, count))


if __name__ == '__main__':
    dateList = []
    for i in range(1, 31):
        date = "2018-09-%s" % (str(i).zfill(2))
        dateList.append(date)
    print(dateList)
    cookieList = ["205Unknown", "Akamai", "Auroral",
                  "CampusNew", "CampusOne", "CampusTwo",
                  "CPSC", "Phys", "Other"]

    for date in dateList:
        # print("date: %s" %(date))
        doDailyCheck(date, cookieList)

			
