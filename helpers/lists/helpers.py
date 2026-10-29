import math

def isEven(num):
    return num % 2 == 0

def findLargestNumber(list):
    ret = list[0]
    
    for item in list:
        if item > ret:
            ret = item
    
    return ret

def calculateFactorial(num):
    if num < 2:
        return 1
    else:
        return num * calculateFactorial(num -1)

def calculateAvarage(list):
    total = 0

    for item in list:
        total = total + item

    return total / len(list)

def countDigits(num):
    
    return len(str(num))
