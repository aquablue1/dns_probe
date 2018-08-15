"""
" Get the major statistics of a series (list) of data.
" Five M are:
" Min, Max, Mean, Median and Mode
"""

import numpy as np



class fiveM():
    def __init__(self, dataList):
        self.min = np.min(dataList)
        self.max = np.max(dataList)
        self.mean = np.mean(dataList)
        self.madian = np.median(dataList)
        self.mode = np.bincount(dataList).argmax()




if __name__ == '__main__':
    a = [1,2,3,4,5,5,66,6,6,6,6,6,7]
    m = fiveM(a)
    print(m.mode)
    print(m.max)


