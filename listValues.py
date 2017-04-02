def findLargest(inputList):
    inputList.sort()
    largestValue = inputList[-1]
    return largestValue


def findSmallest(inputList):
    inputList.sort()
    smallestValue = inputList[0]
    return smallestValue


inputList = [1, 2, 3, 4, 2, 67, 12, 9, 2, 3, 4, 5, 7, 0]
large = findLargest(inputList)
small = findSmallest(inputList)
print(large, small)
