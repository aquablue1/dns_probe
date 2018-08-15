"""
" Get the daily count of src of DNS sessions that sent to cpsc ns.
" By Zhengping on 2018-08-14
"""

from src.GeneralAnalysis.DailySrcCount import dailySrcCount
from src.GeneralAnalysis.DailyDstCount import dailyDstCount
from src.GeneralAnalysis.DailyQueryCount import dailyNameCount


def getDailySrcCount(date, foldername):
    cpscSrcCounter = dailySrcCount(date, foldername)
    cpscSrcCounter.getDailySrcCount()


def getDailyDstCount(date, foldername):
    cpscDstCounter = dailyDstCount(date, foldername)
    cpscDstCounter.getDailyDstCount()


def getDailyNameCount(date, foldername):
    cpscNameCounter = dailyNameCount(date, foldername)
    cpscNameCounter.getDailyNameCount()


if __name__ == '__main__':
    date = "2018-03-07"
    foldername = "../../result/ToCPSCAnalysis/"
    getDailySrcCount(date, foldername)
    getDailyDstCount(date, foldername)
    getDailyNameCount(date, foldername)