"""
" Draw the workload plot of the given source (IP).
" By Zhengping on 2018-09-23
"""

from src.paint.AdvancedPlot import advancedPlot
from src.LongPeriodSampleAnalysis.getHostPeriodWorkload import getPeriodWorkload

def drawHostPeriodWorkload(periodList, hostList):
    adPlot = advancedPlot()
    for host in hostList:
        workloads = getPeriodWorkload(periodList, host)
        adPlot.doPaint(range(len(periodList)), workloads, host)
        adPlot.setTicks('x', range(len(periodList)), periodList, rotation=20)

        yReal = [0, 500_000, 1_000_000, 1_500_000, 2_000_000,
                 2_500_000, 3_000_000, 3_500_000, 4_000_000,
                 4_500_000, 5_000_000, 5_500_000, 6_000_000,
                 6_500_000, 7_000_000, 7_500_000, 8_000_000,
                 8_500_000, 9_000_000, 9_500_000, 10_000_000,
                 10_500_000, 11_000_000, 11_500_000, 12_000_000
                 ]
        yTick = ["0", "0.5", "1", "1.5", "2",
                 "2.5", "3", "3.5", "4",
                 "4.5", "5", "5.5", "6",
                 "6.5", "7", "7.5", "8",
                 "8.5", "9", "9.5", "10",
                 "10.5","11","11.5","12"
                 ]
        adPlot.setTicks("y", yReal, yTick)
    adPlot.setLabel("Date", "Number of received DNS queries (million)")
    adPlot.setLim("y", [0, 6_000_000])
    adPlot.doShow()


if __name__ == '__main__':
    periodList = [
        "2018-05-02", "2018-05-09", "2018-05-16",  "2018-05-23",
        "2018-05-30", "2018-06-06", "2018-06-13", "2018-06-20",
        "2018-06-27", "2018-07-04", "2018-07-11", "2018-07-18",
        "2018-07-25", "2018-08-01", "2018-08-08",
        "2018-08-15", "2018-08-22", "2018-08-29", "2018-09-05", "2018-09-12", "2018-09-19"
        # "2018-09-13", "2018-09-14", "2018-09-15",
    ]
    periodList = ["2018-06-12", "2018-06-13", "2018-06-14", "2018-06-15", "2018-06-16",
                "2018-06-17", "2018-06-18", "2018-06-19", "2018-06-20"]
    periodList = ["2018-06-27", "2018-06-28", "2018-06-29", "2018-06-30", "2018-07-01",
                  "2018-07-02", "2018-07-03", "2018-07-04"]
    hostList = ["136.159.1.21", "136.159.34.201", "136.159.2.1","136.159.2.4"]
    # hostList = ["136.159.222.244", "136.159.222.10", "136.159.222.2"]
    # hostList = ["136.159.205.37", "136.159.205.38", "136.159.205.39"]
    # hostList = ["136.159.236.253"]
    drawHostPeriodWorkload(periodList, hostList)