def RadixSort(a):
    base = 1
    maxv = max(a)
    while base < maxv:
        bucket = []
        for idx in range(10):
            bucket.append([])
        for num in a:
            idx = num // base % 10
            bucket[idx].append(num)
        l = 0
        for idx in range(10):
            for v in bucket[idx]:
                a[l] = v
                l += 1
        print(a)
        base *= 10


a = [3121, 897, 3122, 3, 23, 5, 55, 7, 97, 123, 456, 1327]
RadixSort(a)
