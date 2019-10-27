# coding:utf-8
def quick_sort(alist, first, last):
    if last == first:
        return
    left_pointer, right_pointer = first, last
    pivot = alist[first]
    while left_pointer < right_pointer:
        while left_pointer < right_pointer and alist[right_pointer] > pivot:
            right_pointer -= 1
        alist[left_pointer] = alist[right_pointer]
        while left_pointer < right_pointer and alist[left_pointer] < pivot:
            left_pointer += 1
        alist[right_pointer] = alist[left_pointer]
    alist[left_pointer] = pivot
    quick_sort(alist, first, left_pointer-1)
    quick_sort(alist, left_pointer+1, last)


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    n = len(li)
    quick_sort(li, 0, n-1)
    print(li)
