"""
" Class used to write files to a/multiple files.
" By Zhengping on 2018-08-09
"""


import os, errno


class fileWriter():
    def __init__(self, filename):
        self.filename = filename


    def writeString(self, string, isOverWrite=False):
        if isOverWrite:
            try:
                os.remove(self.filename)
            except OSError as osE:
                if osE.errno != errno.ENOENT:
                    raise
        with open(self.filename, 'a') as outF:
            outF.write(string)
        return True


class batchFileWriter():
    def __init__(self, foldername):
        self.foldername = foldername

    def writeString(self, filename, string, isOverWrite=False):
        fullFilename = self.foldername + "/" + filename
        if isOverWrite:
            try:
                os.remove(fullFilename)
            except OSError as osE:
                if osE.errno != errno.ENOENT:
                    raise
        with open(fullFilename, 'a') as outF:
            outF.write(string)
        return True
