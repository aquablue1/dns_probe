"""
" There are two distinct DNS servers with in CPSC
" The workload between them is not balanced
" This script is designed to briefly analysis the difference between these two servers
" Input: the ToCPSCAnalysis/%date/*.log. Output, basic analysis results
" By Zhengping on 2018-08-16
"""

from src.GeneralAnalysis.DailyCountByField import dailyCountByField


def getDailySrcCountByDst(date, foldername):
    toField = "srcIP"
    filterField = "dstIP"
    filterNS1 = "136.159.2.1"
    filterNS2 = "136.159.2.4"
    cpscNS1Counter = dailyCountByField(date, foldername, toField, filterField, filterNS1)
    cpscNS1Counter.getDailyCount()

    cpscNS2Counter = dailyCountByField(date, foldername, toField, filterField, filterNS2)
    cpscNS2Counter.getDailyCount()


def getDailyNameCountByDst(date, foldername):
    toField = "query"
    filterField = "dstIP"
    filterNS1 = "136.159.2.1"
    filterNS2 = "136.159.2.4"
    cpscNS1Counter = dailyCountByField(date, foldername, toField, filterField, filterNS1)
    cpscNS1Counter.getDailyCount()

    cpscNS2Counter = dailyCountByField(date, foldername, toField, filterField, filterNS2)
    cpscNS2Counter.getDailyCount()


def getDailySrcPortCountByDst(date, foldername):
    toField = "srcPort"
    filterField = "dstIP"
    filterNS1 = "136.159.2.1"
    filterNS2 = "136.159.2.4"
    cpscNS1Counter = dailyCountByField(date, foldername, toField, filterField, filterNS1)
    cpscNS1Counter.getDailyCount()

    cpscNS2Counter = dailyCountByField(date, foldername, toField, filterField, filterNS2)
    cpscNS2Counter.getDailyCount()


if __name__ == '__main__':
    date = "2018-03-07"
    foldername = "../../result/ToCPSC/"
    # getDailySrcCountByDst(date, foldername)
    # getDailyNameCountByDst(date, foldername)
    # getDailySrcPortCountByDst(date, foldername)