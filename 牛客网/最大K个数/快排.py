#coding=utf-8

# 快排即每次将某个数排到它应在的位置
# 快排时间复杂度最坏为n_2 平均为nlogn

def quick_sort(lst):
    if not lst:
        return []
    pivot = lst[0]
    left = quick_sort([x for x in lst[1:] if x<pivot])
    right = quick_sort([x for x in lst[1:] if x>=pivot])
    return left+[pivot]+right

# 归并排序
# 时间复杂度nlogn

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    l, r, res = 0, 0, []
    while l<len(left) and r < len(right):
        if left[l]<=right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res += left[l:]
    res += right[r:]
    return res


# 堆排序
def shift_up(lst, temp, begin, end):
    if lst==[]:
        return []
    i, j = begin, begin*2+1
    while j<end:
        if j+1 < end and lst[j+1]>lst[j]:
            j += 1                        # 左边小于右边，指向右边
        if temp>lst[j]:
            break
        else:
            lst[i] = lst[j]         # 如果子节点大于根节点，将子节点的值赋予根节点
            i, j = j, 2*j + 1       # 然后对于子节点进行调整
    lst[i] = temp               # 将最初的根节点值赋予相应的节点

def head_sort(lst):
    if lst == []:
        return []
    end = len(lst)
    mid = end//2 - 1
    for i in range(mid , -1, -1): # 从叶子结点开始进行
        shift_up(lst, lst[i], i, end)
    for i in range(end-1, 0, -1): # 堆构建好后进行排序
        temp = lst[i]              # 将堆顶元素放到最后一位
        lst[i] = lst[0]
        lst[0] = lst[i]
        shift_up(lst, temp, 0, i)  # 从堆顶开始调整
    return lst


# 冒泡排序n_2
def bubble_sort(lst):
    if lst==[]:
        return []
    for i in range(len(lst)):
        for j in range(1, len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst

# 直接选择排序
def select_sor(lst):
    if lst==[]:
        return []
    for i in range(len(lst)-1):
        smallest = i
        for j in range(i, len(lst)):
            if lst[j] < lst[smallest]:
                smallest = j
        lst[i], lst[smallest] = lst[smallest], lst[i]
    return lst
