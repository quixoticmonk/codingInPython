def insertionSort(A):
    i = len(A)
    for index in range(i - 1, -1, 0):
        while A(index) > A(index + 1) and
