import random

def QuickSortPivot(a, start, end):
    randIdx = random.randint(start,end)
    a[start],a[randIdx] = a[randIdx],a[start]
    pivot = start
    j = start + 1
    for i in range(start + 1, end + 1):
        if a[i] <= a[pivot]:
            a[i], a[j] = a[j], a[i]
            j += 1
    a[pivot], a[j - 1] = a[j - 1], a[pivot]
    pivot = j - 1
    print(a[pivot], a[start:pivot], a[pivot + 1:end + 1])
    return pivot


def QuickSort(a, start, end):
    if start >= end:
        return
    pivot = QuickSortPivot(a, start, end)
    QuickSort(a, start, pivot - 1)
    QuickSort(a, pivot + 1, end)


a = [8, 5, 12, 6, 4, 3, 7, 9, 2, 1, 10, 11]
QuickSort(a,0,11)
print(a)
