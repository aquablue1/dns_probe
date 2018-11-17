"""
" Classify the resopnse of dns request into six main categories.
" By Zhengping on 2018-10-22
"""

from src.util.FileReader import fileReader
from src.util.FolderReader import folderReader
from src.util.DNSFieldLocMap import FieldToLoc
from src.util.FileLineCounter import lineCount
from collections import Counter

codeTypeDict = {1: "Campus IP",
                2: "Akamai Node",
                3: "pool.ntp.org",
                4: "Auroral",
                5: "UofC Domain",
                6: "Others"}

def responseClassify(query, response):
    if response.startswith("136.159."):
        # Campus IP
        return 1
    elif "akamai" in query or response.startswith("23.") or response.startswith("204.237.") or response.startswith("184.50."):
        # Akamai Node
        return 2
    elif response.startswith("pool.ntp.org"):
        return 3
    elif "auroral" in response:
        return 4
    elif "ucalgary" in response or "uc" in response or "uofc" in response:
        return 5
    else:
        return 6


def getHourlyAnalysis(filename):
    file = fileReader(filename)
    hourlyCounter = Counter()
    for line in file:
        response = line.split("\t")[FieldToLoc["answers"]]
        query = line.split("\t")[FieldToLoc["query"]]
        hourlyCounter[responseClassify(query, response)] += 1
    return hourlyCounter

def getDailyAnalysis(date, cookie):
    foldername = "../../result/Response/To%s/%s/" % (cookie, date)
    folder = folderReader(foldername)
    dailyCounter = Counter()
    for filename in folder:
        dailyCounter += getHourlyAnalysis(filename)
    print(dailyCounter)
    print(sum(dailyCounter.values()))


if __name__ == '__main__':
    date = "2018-09-12"
    cookie = "Phys"
    getDailyAnalysis(date, cookie)

    foldername = "../../result/To%s/%s" % (cookie, date)
    lineC = 0
    folder = folderReader(foldername)
    for filename in folder:
        lineC += lineCount(filename)
    print(lineC)