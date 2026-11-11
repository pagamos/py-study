import numpy as np

# Exercises based on the following matrices
# Screen view, number of clicks, duration in seconds
matrix = np.array([[10, 5, 120], [8, 7, 100], [15, 3, 240], [20, 10, 300], [25, 12, 360]])

def sampleGettingSpecificValues():
    print('The whole first session: ', matrix[0])
    print('Duration of first session: ', matrix[0, 2])
    print('Screen View of all sessions: ', matrix[:, 0])

def calculateDotProductOf(s1, s2):
    print('Calculating dot product of session indexes ', str(s1), ', ', str(s2))
    print(np.dot(matrix[s1], matrix[s2]))

def calculateTheMean(listNumbers):
    print('The mean of:', listNumbers, ' is', np.mean(listNumbers))
    return np.mean(listNumbers)

def calculateTheMedian(listNumbers):
    print('The median of:', listNumbers, ' is', np.median(listNumbers))
    return np.median(listNumbers)

def calculateTheVarianceManually(listNumbers):
    mean =  calculateTheMean(listNumbers)
    total = 0

    for item in listNumbers:
        diff = item - mean
        print(diff * diff)
        total += diff * diff

    ret = total / len(listNumbers)

    print('The variance of:', listNumbers, ' is', ret)
    return ret


def calculateTheVariance(listNumbers):
    print('The variance of:', listNumbers, ' is', np.var(listNumbers))
    return np.var(listNumbers)


def calculateStandardDeviation(listNumbers):
    print('The variance of:', listNumbers, ' is', np.std(listNumbers))
    return np.var(listNumbers)
