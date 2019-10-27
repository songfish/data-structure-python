# coding:utf-8
def heapify(array, n, i):
    largest = i
    left = 2 * i + 1 # 叶子结点没有left和right
    right = 2 * i + 2
    if left < n and array[left] > array[i]:
        largest = left
    if right < n and array[largest] < array[right]:
        largest = right
    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        heapify(array, n, largest)


def heap_sort(array):
    n = len(array)
    # 构造最大堆
    for i in range(n-1, -1, -1):
        heapify(array, n, i)
    for j in range(n-1, 0, -1):
        array[j], array[0] = array[0], array[j]
        heapify(array, j, 0)


if __name__ == "__main__":
    L = [12, 11, 13, 5, 6, 7]
    heap_sort(L)
    n = len(L)
    print("排序后")
    for i in range(n):
        print("%d" % L[i])
