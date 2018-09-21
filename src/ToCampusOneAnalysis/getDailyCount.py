"""
" Get the daily count of src of DNS sessions that sent to campusOne ns.
" By Zhengping on 2018-08-14
"""

from src.GeneralAnalysis.DailySrcCount import dailySrcCount
from src.GeneralAnalysis.DailyDstCount import dailyDstCount
from src.GeneralAnalysis.DailyQueryCount import dailyNameCount


def getDailySrcCount(date, foldername):
    campusOneSrcCounter = dailySrcCount(date, foldername)
    campusOneSrcCounter.getDailySrcCount()


def getDailyDstCount(date, foldername):
    campusOneDstCounter = dailyDstCount(date, foldername)
    campusOneDstCounter.getDailyDstCount()


def getDailyNameCount(date, foldername):
    campusOneNameCounter = dailyNameCount(date, foldername)
    campusOneNameCounter.getDailyNameCount()


if __name__ == '__main__':
    date = "2018-03-07"
    dateList = ["2018-09-09", "2018-09-10", "2018-09-11", "2018-09-12",
                "2018-09-13", "2018-09-14", "2018-09-15", ]
    for date in dateList:
        foldername = "../../result/ToCampusOneAnalysis/"
        getDailySrcCount(date, foldername)
        getDailyDstCount(date, foldername)
        getDailyNameCount(date, foldername)