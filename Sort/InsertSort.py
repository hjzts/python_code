def InsertSort(a):
    n = len(a)
    for i in range(1, n):
        x = a[i]
        j = i - 1
        while j >= 0:
            if x <= a[j]:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = x
        print(a)


a = [8, 5, 6, 4, 3, 7, 10, 2]
InsertSort(a)
