def maxHeapify(heap, start, end):
    son = start * 2
    while son <= end:
        if son + 1 <= end and heap[son + 1] > heap[son]:
            son = son + 1
        if heap[son] > heap[start]:
            heap[start], heap[son] = heap[son], heap[start]
            start, son = son, son * 2
        else:
            break

def HeapSort(a):
    heap = [None] + a
    root = 1
    l = len(heap)
    for i in range(l // 2, root - 1, -1):
        maxHeapify(heap, i, l - 1)
    for i in range(l - 1, root - 1, -1):
        heap[i], heap[root] = heap[root], heap[i]
        maxHeapify(heap, root, i - 1)
    return heap[root:]


# a = [23, 4353, 454, 21, 453, 459, 435, 32, 21, 6, 7647, 324]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
HeapSort(a)
print(a)
