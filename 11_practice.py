# coding:utf-8
def insert_sort(alist):
    n = len(alist)
    for j in range(n-1):
        i = j+1
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break


if __name__ == "__main__":
    if __name__ == "__main__":
        li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        print(li)
        insert_sort(li)
        print(li)

