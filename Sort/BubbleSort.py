def BubbleSort(a):
    n = len(a)
    for i in range(n - 1, -1, -1):
        flag = 0
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                flag = 1
        print(a)
        if flag == 0:
            break


# a = [5, 6, 8, 4, 3, 7, 10, 2]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
BubbleSort(a)
