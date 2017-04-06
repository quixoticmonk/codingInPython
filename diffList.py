List1 = [2, 3, 3, 4, 5]
List2 = [2, 3, 4, 1, 7, 8]

outputList = []

for x in List1:
    if x not in List2:
        outputList.append(x)
    else:
        continue

for x in List2:
    if x not in List1:
        outputList.append(x)
    else:
        continue

print(outputList)
