"""
" Phrase an IP to its organization.
" Using ip-api.com as source
" Warning: querying ration should be lower than 150/minute. Otherwise, the IP will be banned
" By Zhengping on 2018-08-14
"""

import sys
import urllib.request
import json


def getOrg(ip):
    api = "http://ip-api.com/json/%s" % ip
    try:
        result = urllib.request.urlopen(api).read()
        result = json.loads(result)
    except:
        print("Cannot find: %s" % api)
        return None
    return result["org"]



if __name__ == '__main__':
    ip = "8.8.8.8"
    print(getOrg(ip))