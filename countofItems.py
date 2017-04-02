sampleList = ['abc', 'xyz', 'aba', '1221', 'Tan', '2', 'unau']


def countOfItems(inputList):
    count = 0
    for i in inputList:
        if(len(i) >= 2 and i[0] == i[-1]):
            count += 1
        else:
            continue
    return count

countitems = countOfItems(sampleList)
print(countitems)
