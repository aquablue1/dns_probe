"""
" Draw the plot of NBSTAT graph.
" By Zhengping on 2018-11-05
"""


from src.util.FileReader import fileReader
from src.util.FolderReader import folderReader
from src.util.DNSFieldLocMap import FieldToLoc
from src.util.FileLineCounter import lineCount
from src.paint.Plot import plot


class ListPlot():
    def __init__(self, dateList ):
        self.dateList = dateList
        self.superfoldername = "../../result/NBSTAT/"


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
        p.setLabel("Date", "Number of inbound NBSTAT session per hour")
        xTick = [i*24+12 for i in range(len(self.dateList))]
        xTickReal = self.dateList
        p.setTicks("x", xTick, xTickReal)
        p.doPaint(xData, yData, "NBSTAT")
        for i in range(0, 24*len(self.dateList)+1, 24):
            p.plt.axvline(x=i, linestyle="--", color="grey")
        p.doShow()




if __name__ == '__main__':
    dataList = ["2018-09-10", "2018-09-11",
                "2018-09-12", "2018-09-13", "2018-09-14",
                "2018-09-15"]
    listP = ListPlot(dataList)
    listP.doPaint()