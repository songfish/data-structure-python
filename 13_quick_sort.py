# coding:utf-8
def quick_sort(alist, first, last):
    # 最坏时间复杂度是O(n^2)【每次分出来一个】，最优时间复杂度O(nlogn)【每次折半分】。
    # 不稳定
    # 终止条件
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    # 从循环退出时，low = high
    alist[high] = mid_value
    # 对low左边的列表排序
    quick_sort(alist, first, low-1)
    # 对low右边的列表排序
    quick_sort(alist, low+1, last)
    # 最后两行是顺序执行，时间复杂度相加


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    n = len(li)
    quick_sort(li, 0, n - 1)
    print(li)
