"""
" Classify the different inbound DNS traffic in a day.
" Take advantage of the getRow function in those To*** folders.
" By Zhengping on 2018-10-24
"""

# from src.ToAkamai import getRow as getAkamaiRow
# from src.To205Unknown import getRow as get205UnknownRow
# from src.ToAuroral import getRow as getAuroralRow
# from src.ToCampusNew import getRow as getCampusNewRow
# from src.ToCampusOne import getRow as getCampusOneRow
# from src.ToCampusTwo import getRow as getCampusTwoRow
# from src.ToCPSC import getRow as getCPSCRow
# from src.ToPhys import getRow as getPhysRow
# from src.ToOther import  getRow as getOtherRow

import os
import importlib

def generateFoldername(date, cookie):
    rootFolder = "../../result/To%s/" % cookie
    foldername = rootFolder + "/%s/" % date
    return foldername

def createIfFirst(foldername):
    if os.path.exists(foldername):
        # Exist before, simply returns False
        return False
    else:
        os.makedirs(foldername)
        return True

def doBatchedClassify(date, cookieList = None):
    if not cookieList:
        cookieList = ["205Unknown", "Akamai", "Auroral",
                      "CampusNew", "CampusOne", "CampusTwo",
                      "CPSC", "Phys", "Other"]
    inputFoldername = "../../data/%s/inbound/" % date
    for cookie in cookieList:
        if createIfFirst(generateFoldername(date, cookie)):
            # First generate this Foldername, do classify for it.
            outputFoldername = "../../result/To%s/%s/" % (cookie, date)
            module = importlib.import_module("src.To%s.getRow" % (cookie))
            func = getattr(module, "getDaily%sRow" % (cookie))
            func(inputFoldername, outputFoldername)
            print("Done %s." % cookie)

if __name__ == '__main__':
    date = "2018-09-09"
    doBatchedClassify(date)

