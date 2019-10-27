# coding:utf-8
# 前提是已经排好序


def binary_search(alist, item):
    """二分查找(递归版本)"""
    n = len(alist)
    mid = n // 2
    if n > 0:
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False


def binary_search_2(alist, item):
    """非递归版本"""
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == "__main__":
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(binary_search(li, 31))
    print(binary_search(li, 100))
    print(binary_search_2(li, 31))
    print(binary_search_2(li, 100))
