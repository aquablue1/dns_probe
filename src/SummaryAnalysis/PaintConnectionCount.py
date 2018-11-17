"""
" Script to count the number of connections  based on the time period and cookie
" Input files should have two columns, first is timestamp, second is the number of session
" By Zhengping on 2018-11-16
"""

import sys
from src.paint.Plot import plot
from src.util.FolderReader import folderReader
from src.util.FileReader import fileReader


def dataGen(dateList, cookie):
    folderName = "../../result_summary/connectionCount/To%s" % (cookie)
    yData = []
    xData = []
    index = 0
    for date in dateList:
        filename = folderName + "/%s.log" % (date)
        file = fileReader(filename)
        for line in file:
            count = int(line.strip().split("\t")[1])
            # if 429<=index<=561:
                # count = int(count/2)
            yData.append(count)
            xData.append(index)
            index += 1
    return xData, yData

def doDraw(dateList, cookie):
    xData, yData = dataGen(dateList, cookie)
    p = plot()
    p.doPaint(xData, yData, cookie)
    p.setLim('y', [0, max(yData)+10000])
    p.doShow()


if __name__ == '__main__':
    dateList = ["2018-09-%s" % (str(day).zfill(2)) for day in range(1, 31)]
    cookie = "Akamai"
    doDraw(dateList, cookie)