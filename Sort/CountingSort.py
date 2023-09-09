def CountingSort(a):
    n = len(a)
    cntlen = max(a) + 1
    cnt = [0] * cntlen
    for val in a:
        cnt[val] += 1
    print(cnt)
    n = 0
    for val in range(0, cntlen):
        while cnt[val] > 0:
            cnt[val] -= 1
            a[n] = val
            n += 1


a = [2, 3,1, 3, 2, 1, 4, 2, 4, 6, 2]
CountingSort(a)
print(a)
