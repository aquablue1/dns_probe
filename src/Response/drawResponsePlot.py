"""
" Draw the hourly valid response count based on the given dataList.
" Accept parameters:
" By Zhengping on 2018-10-29
"""

from src.util.FileReader import fileReader
from src.util.FolderReader import folderReader
from src.util.DNSFieldLocMap import FieldToLoc
from src.util.FileLineCounter import lineCount
from src.paint.Plot import plot


class ListPlot():
    def __init__(self, dateList, target, cookie):
        self.dateList = dateList
        self.cookie = cookie
        self.target = target
        if target == "response":
            self.superfoldername = "../../result/Response/To%s" % cookie
        elif target == "overall":
            self.superfoldername = "../../result/To%s" % cookie
        elif target == "responseless":
            self.superfoldername = "../../result/ResponseLess/To%s" % cookie
        else:
            raise ValueError("Invalid target name.")

    def yDataGen(self):
        yData = []
        for date in self.dateList:
            foldername = self.superfoldername + "/" + date
            # print(foldername)
            folder = folderReader(foldername)
            for filename in folder:
                # print(filename)
                yData.append(lineCount(filename))
        return yData

    def xDataGen(self):
        xData = list(range(len(self.dateList) * 24))
        return xData

    def doPaint(self):
        xData = self.xDataGen()
        yData = self.yDataGen()
        p = plot()
        p.setLabel("Date", "%s session count" % self.target)
        xTick = [i*24 for i in range(len(self.dateList))]
        xTickReal = self.dateList
        p.setTicks("x", xTick, xTickReal)
        p.doPaint(xData, yData, "%s" % self.cookie)
        p.doShow()




if __name__ == '__main__':
    target = "responseless"
    dataList = ["2018-09-10", "2018-09-11",
                "2018-09-12", "2018-09-13", "2018-09-14",
                "2018-09-15"]
    cookie = "Other"
    cookieList = ["Akamai", "Auroral",
                      "CampusNew", "CampusOne", "CampusTwo",
                      "CPSC", "Phys", "Other"]
    for cookie in cookieList:
        listP = ListPlot(dataList, target, cookie)
        listP.doPaint()