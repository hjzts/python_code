def ShellSort(a):
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            x = a[i]
            j = i
            while j >= gap:
                if x < a[j - gap]:
                    a[j] = a[j - gap]
                else:
                    break
                j -= gap
            a[j] = x
        print(a)
        gap = gap // 2


a = [8, 5, 6, 4, 3, 7, 10, 2]
ShellSort(a)
