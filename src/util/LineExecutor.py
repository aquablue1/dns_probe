import os


class lineExecutor():
    def __init__(self, line):
        self.line = line
        self.splitter="\t"
        self.line_list = self.line.split(self.splitter)

    def setSplitter(self, splitter="\t"):
        if self.splitter != splitter:
            self.splitter = splitter
            self.line_list = self.line.split(self.splitter)

    def getAsList(self):
        return self.line_list


if __name__ == '__main__':
    line = "2018-03-11	6592787023	3007968651"
    lineExe = lineExecutor(line)
    print(lineExe.getAsList())