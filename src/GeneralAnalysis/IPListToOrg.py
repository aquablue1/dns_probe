"""
" Note: The method in this class is extremely slow since it has to meet the
" current-limiting requirement. current limited at 120/minute
" phrase a list of IPs into their corresponding organization.
" accept a list as input
" return a dict with key being IP and value being organization as output.
" By Zhengping on 2018-08-14
"""

from src.util.IPToOrg import getOrg
from time import sleep


def ipListToOrg(ipList, cachedSet=None):
    orgDict = {}
    for ip in ipList:
        # If the IP already queried before, simply read the cache
        if cachedSet is not None and ip in cachedSet:
            orgDict[ip] = cachedSet[ip]
        else:
            orgDict[ip] = getOrg(ip)
            sleep(0.5)
    return orgDict


if __name__ == '__main__':
    ipList = ["136.159.16.14", "136.159.2.4", "8.8.8.8", "216.218.192.166"]
    print(ipListToOrg(ipList))
