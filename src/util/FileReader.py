"""
" Class defined to read file line by line
" Ignore lines beginning with "#"
" Simply use it as an iterator
" By Zhengping on 2018-08-08
"""


import os


class fileReader():
    def __init__(self, filename):
        self.filename = filename
        self.hasNext = True

    def __iter__(self):
        try:
            self.file = open(self.filename)
        except FileNotFoundError:
            print("Filename %d not found in file system." % self.filename)
        return self

    def __next__(self):
        """
        read file line by line. skip the lines beginning with "#" since they are comments
        :return: None if reaches the end of line, else return string of line.
        """
        nextLine = self.file.readline()
        while nextLine != "" and nextLine[0] == "#":
            nextLine = self.file.readline()
        if nextLine == "":
            # print("Reach the end of current line - %s" % self.filename)
            self.hasNext = False
            raise StopIteration
        else:
            return nextLine.strip()


if __name__ == '__main__':
    filename = "../../data/Conn_WeeklySummary_2018-03.log"
    newFile = fileReader(filename)

    for line in newFile:
        # line_list = line.split("\t")
        print(line)
