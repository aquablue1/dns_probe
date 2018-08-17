"""
" Get the daily Name count of cpsc related traffic
" By Zhengping on 2018-08-16
"""

from src.GeneralAnalysis.DailyQueryCount import dailyNameCount


def getDailyNameCount(date, foldername):
    nameCounter = dailyNameCount(date, foldername)
    nameCounter.getDailyNameCount()


if __name__ == '__main__':
    date = "2018-03-07"
    foldername = "../../result/CPSCRow/"
    getDailyNameCount(date, foldername)