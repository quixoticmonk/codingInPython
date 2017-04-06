sampleList = []
sampleList2 = [2, 3, 4, 5, 6, 7]


def checkList(inputList):
    if len(inputList) == 0:
        print(" The list used is empty")
    else:
        print(" The list has {} elements".format(len(inputList)))


checkList(sampleList2)
checkList(sampleList)
