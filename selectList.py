def selectList(inputList, n):
    returnList = []
    for x in inputList:
        if len(x) > n:
            returnList.append(x)
        else:
            continue
    return returnList


inputList = ['abc', 'werrdef', 'sdffdsf', 'sdfsdfs', 'weada', 'aagw', 'fwfe', 'sd']
returnList = selectList(inputList, 3)
print(returnList)
