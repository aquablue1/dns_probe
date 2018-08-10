"""
" Add two numbers when sometimes one element is dash
" Typically seen in data exchange volume records in CONN files
" By Zhengping on 2018-08-09
"""


def resolveStringAsInt(num):
    if num == "-":
        return 0
    else:
        return int(float(num))


def skipDashAdd(ele1, ele2):
    return resolveStringAsInt(ele1) + resolveStringAsInt(ele2)
