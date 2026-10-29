import math

def removeDuplicates(list):
    ret = []
    for item in list:
        if item not in ret:
            ret.append(item)
    return ret

def splitInChunks(items, chunk):
    ret = []
    newList = []
    i = 0

    for item in items:
        newList.append(item)
        i += 1

        if i == chunk:
            ret.append(newList)
            newList = []
            i = 0

    if newList:
        ret.append(newList)

    return ret

def findCommonElements(listOne, listTwo):
    ret = []
    for item in listOne:
        if item in listTwo:
            ret.append(item)
    return ret

def rotateList(list):
    ret = []
    i = len(list) - 1
    while i >= 0:
        ret.append(list[i])
        i -= 1
    return ret

def findSecondLargest(list):
    largest = list[0]
    second = float('-inf')
    i = 0
    while i < len(list):
        if list[i] > largest:
            second = largest
            largest = list[i]
        elif list[i] < largest and list[i] > second:
            second = list[i]
        i += 1
    
    return second
