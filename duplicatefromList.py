sampleList = [2, 3, 3, 4, 5, 6, 7, 2, 3, 6, 7, 8, 9, 0]


def removeDuplicates(inputList):
    returnList = []
    for element in inputList:
        if element not in returnList:
            returnList.append(element)

    return returnList


returnedList = removeDuplicates(sampleList)
print(returnedList)
