inputList1 = [1, 2, 3, 4, 5, 131, 3, 12]
inputList2 = [12, 22, 32, 42, 52, 131, 32, 122]


def compareLists(inputList1, inputList2):
    count = 0
    for x in inputList1:
        if x in inputList2:
            count += 1
        else:
            continue
    return count


count = compareLists(inputList1, inputList2)
if count != 0:
    print("Lists have {} matches".format(count))
else:
    print(" lists have no matches")
