"""
" Get the daily count of src of DNS sessions that sent to campusTwo ns.
" By Zhengping on 2018-09-23
"""

from src.GeneralAnalysis.DailySrcCount import dailySrcCount
from src.GeneralAnalysis.DailyDstCount import dailyDstCount
from src.GeneralAnalysis.DailyQueryCount import dailyNameCount
from src.GeneralAnalysis.DailyTypeCount import dailyTypeCount


def getDailySrcCount(date, foldername):
    campusTwoSrcCounter = dailySrcCount(date, foldername)
    campusTwoSrcCounter.getDailySrcCount()


def getDailyDstCount(date, foldername):
    campusTwoDstCounter = dailyDstCount(date, foldername)
    campusTwoDstCounter.getDailyDstCount()


def getDailyNameCount(date, foldername):
    campusTwoNameCounter = dailyNameCount(date, foldername)
    campusTwoNameCounter.getDailyNameCount()

def getDailyTypeCount(date, foldername):
    campusTwoTypeCounter = dailyTypeCount(date, foldername)
    campusTwoTypeCounter.getDailyTypeCount()


if __name__ == '__main__':
    date = "2018-03-07"
    # dateList = ["2018-09-09", "2018-09-10", "2018-09-11", "2018-09-12",
                # "2018-09-13", "2018-09-14", "2018-09-15", ]
    dateList = ["2018-08-13", "2018-09-12"]
    dateList = ["2018-03-07"]
    dateList = ["2018-09-19"]
    for date in dateList:
        foldername = "../../result/ToCampusTwo/"
        getDailySrcCount(date, foldername)
        getDailyDstCount(date, foldername)
        getDailyNameCount(date, foldername)
        getDailyTypeCount(date, foldername)