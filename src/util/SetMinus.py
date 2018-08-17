"""
" Get rid of all elements appeared in list A out of list B
" Accept two non-empty lists
" return the minus result of the lists.
" By Zhengping on 2018-08-15
"""

def setMinus(listA, listB):
    resultList = []
    for elem in listA:
        if elem in listB:
            continue
        resultList.append(elem)
    return resultList


if __name__ == '__main__':
    listA = [1,2,3,4]
    listB = [2,3,4,5,6]
    print(setMinus(listA, listB))