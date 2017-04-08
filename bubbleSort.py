# Bubble Sort
import random

# generate a lis of numbers
numlist = random.sample(range(1, 20), 5)
print(numlist)

# Setting the out loop variable i
i = len(numlist) - 1


while i > 1:
    j = 0
    while j < i:
        print("is {} > {}".format(numlist[j], numlist[j + 1]))
        if numlist[j] > numlist[j + 1]:
            print("Swtich {} with {}".format(numlist[j], numlist[j + 1]))
            temp = numlist[j + 1]
            numlist[j + 1] = numlist[j]
            numlist[j] = temp

        else:
            print("Dont Switch")
        j += 1
    i -= 1


print(numlist)
