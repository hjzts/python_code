def SelectionSort(a):
    n = len(a)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
        print(a)


# a = [8, 5, 6, 4, 3, 7, 10, 2]
a = [38, 356, 98, -102, 126, 46, 65, -9, 100, 0, 21, 2, 90, 8, 18, 12, 78, 16, 189, 23]
SelectionSort(a)
