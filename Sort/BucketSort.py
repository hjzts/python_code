def SelectionSort(a):
    n = len(a)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]


def BucketSort(a):
    minV = min(a)
    maxV = max(a)
    bucketCount = 3
    bucket = [[], [], []]
    perBucket = (maxV - minV + bucketCount) // bucketCount

    for num in a:
        bucketIndex = (num - minV) // perBucket
        bucket[bucketIndex].append(num)

    for i in range(bucketCount):
        SelectionSort(bucket[i])

    idx = 0
    for i in range(bucketCount):
        for v in bucket[i]:
            a[idx] = v
            idx += 1
    print(bucket)
    print(a)


a = [7, 11, 5, 9, 8, 6, 3, 12, 1, 10, 4, 2]
BucketSort(a)
