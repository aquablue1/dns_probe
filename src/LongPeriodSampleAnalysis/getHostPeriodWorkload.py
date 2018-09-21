"""
" Get the workload of a certain host(IP) in a certain period.
" Accept List:period and String:IP as input.
" Return List<int>: as the description of the workload.
" By Zhengping on 2018-09-20
"""

from src.util.FileReader import fileReader


def _getFilenames(periodList):
    fatherFoldername = "../../result/LongPeriodSample/"
    # filenames = []
    for date in periodList:
        filename = fatherFoldername + "/%s/dailyDstIPCount_%s.log" % (date, date)
        yield filename
    # return filenames


def getPeriodWorkload(periodList, host):
    countList = []
    for filename in _getFilenames(periodList):
        file = fileReader(filename)
        isFound = False
        count = 100
        for line in file:
            if line.split("\t")[1] == host:
                count = int(line.split("\t")[2])
                isFound = True
        if not isFound:
            # raise ValueError("Hostname:%s not found in file %s" % (host, filename))
            count = 0
        countList.append(count)
    return countList


if __name__ == '__main__':
    periodList = ["2018-05-02", "2018-05-09", "2018-05-16", # "2018-05-23",
                  "2018-05-30", "2018-06-06", "2018-06-13", "2018-06-20",
                  "2018-06-27", "2018-07-04", "2018-07-11", "2018-07-18",
                  "2018-07-25", "2018-08-01", "2018-08-08",
                  "2018-09-09", "2018-09-10", "2018-09-11", "2018-09-12",
                  "2018-09-13", "2018-09-14", "2018-09-15", ]
    IP = "136.159.205.39"
    print(getPeriodWorkload(periodList, IP))