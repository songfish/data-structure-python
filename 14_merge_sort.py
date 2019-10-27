# coding:utf-8
def merge_sort(alist):
    # 最坏最优时间复杂度为O(nlogn)
    # 稳定
    # 用空间换时间，有额外的开销
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:  # = 保证稳定
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]  # 切片之后超限会返回空列表
    result += right_li[right_pointer:]
    return result


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    sorted_li = merge_sort(li)
    print(sorted_li)

# 代码执行流程
# merge_sort [54, 26, 93, 17, 77, 31, 44, 55, 20]
#    left_li = merge_sort [54, 26, 93, 17] = [17, 26, 54, 93]
#       left_li = merge_sort [54, 26] = [26, 54]
#           left_li = merge_sort([54]) = [54]
#                   return [54]
#           right_li = merge_sort [26] = [26]
#           result = [26, 54]
#       right_li = merge_sort [93, 17] = [17, 93]
#           left_li = merge_sort [93] = [93]
#           right_li = merge_sort [17] = [17]
#           result = [17, 93]
#           return result
#       result = [17,26,54,93]
#       return result
#    right_li = merge_sort [77, 31, 44, 55, 20]


