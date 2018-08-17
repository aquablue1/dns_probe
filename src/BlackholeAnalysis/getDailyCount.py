"""
" get the daily count of blackhole related sessions
" By Zhengping on 2018-08-13
"""

from src.util.FileLineCounter import lineCount
from src.util.FolderReader import folderReader

def dailyCount(foldername):
    folder = folderReader(foldername)
    sumCount = 0
    for filename in folder:
        sumCount += lineCount(filename)

    return sumCount


if __name__ == '__main__':
    date = "2018-03-07"
    foldername = "../../result/Blackhole/%s/" % date
    print(dailyCount(foldername))