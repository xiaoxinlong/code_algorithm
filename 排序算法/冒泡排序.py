
import random

# 选择排序
# 扫描，每次扫描最小的放到指定位置
def select_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]

def select_sort2(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]

# 冒泡排序 在扫描的同时进行挪动
def bubble_sort(arr):
    n = len(arr)
    k = n
    for i in range(n):
        flag = True
        for j in range(1, k):  # range(1,k)只会在更新i之后才会更新
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j] = arr[j], arr[j-1]
                k = j
                flag = False
        if flag:
            break
    return arr

# 插入排序，往已经排序好的序列插入
def insert_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = i-1
        mark = arr[i]
        # 从后往前扫
        while key>=0 and arr[key]>mark:
            arr[key+1] = arr[key]
            key -= 1
        arr[key+1] = mark
    return arr

def shell_sort(arr):
    count = len(arr)
    gap = round(count/2)
    while gap >= 1:
        for i in range(gap, count):
            temp = arr[i]
            j = i
            while j-gap>=0 and arr[j-gap]>temp:  # 插入排序，大于该元素的值均后移
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap = round(gap/2)
    return arr


def merge_sort(arr):
    if len(arr)<=1:
        return arr

    median = len(arr)//2
    left = merge_sort(arr[:median])
    right = merge_sort(arr[median:])
    return merge(left, right)

def merge(left, right):
    res = []
    i = j = k = 0
    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res += left[i:] + right[j:]
    return res


def quick_sort(arr):
    return qsort(arr,0,len(arr)-1)

def qsort(arr,start,end):
    if start<end:
        left = start
        right = end
        key = arr[start]
    else:
        return arr

    while left<right:
        while left<right and arr[right]>=key:
            right -= 1
        if left<right:
            arr[left] = arr[right] # 找到一个小于key的数，放到left处，初始时left为start,数通过key保存
            left += 1
        while left<right and arr[left]<key:
            left += 1
        if left<right:
            arr[right] = arr[left] # 找到一个大于key的数
            right -= 1
    arr[left] = key
    qsort(arr,start,left-1)
    qsort(arr,left+1,end)
    # return 其实可以不需要
    return arr


def heap_sort(arr):
    n = len(arr)
    first = n//2-1 # 表示最后一个非叶子结点
    for start in range(first, -1, -1):
        max_heapify(arr, start, n-1)
    for end in range(n-1,0,-1):
        arr[end], arr[0] = arr[0], arr[end]
        max_heapify(arr,0, end-1)
    return arr


def max_heapify(arr, start, end):
    """
    :param arr:
    :param start: 调整起点
    :param end: 调整边界， 为了让后面对堆排序更简单
    :return:
    """
    root = start
    while True:   # 内部在不断的对子树进行重排
        child = root*2 + 1
        if child>end:
            break
        if child+1<=end and arr[child]<arr[child+1]:
            child += 1
        if arr[root]<arr[child]:
            arr[root],arr[child] = arr[child],arr[root]
            root = child
        else:
            break

# 最小堆
def heap_min_sort(arr):
    n = len(arr)
    first = n//2-1 # 表示最后一个非叶子结点
    for start in range(first, -1, -1):
        min_heapify(arr, start, n-1)
    for end in range(n-1,0,-1):
        arr[end], arr[0] = arr[0], arr[end]
        min_heapify(arr,0, end-1)
    return arr
def min_heapify(arr, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child>end:
            break
        if child+1<=end and arr[child]>arr[child+1]:
            child += 1
        if arr[root]>arr[child]:
            arr[root],arr[child] = arr[child],arr[root]
            root = child
        else:
            break   # 出现子节点与父节点符合定义，由于我们是从最后一个非叶子结点开始的，
                    # 可以认为之后都是满足定义的





def RadixSort(arr):
    def digit(num,d):
        p = 10**(d-1)
        return num//p % 10

    def Maxbit(arr):
        max_data = max(arr)
        bit_num = len(str(max_data))
        return bit_num

    if len(arr)<=1:
        return arr
    n = len(arr)

    for d in range(1, Maxbit(arr)+1):  # 对每个位进行排序
        buckets = [[] for _ in range(10)]
        for i in range(0, n):
            buckets[digit(arr[i],d)].append(arr[i])
        print(buckets)
        temp = []
        for bucket in buckets:
            temp += bucket
        arr = temp
    return arr





def get_rand_list(num=10,low=0,high=100):
    # random.randrange(low,high)
    data = [random.randint(low,high) for _ in range(num)]
    return data

if __name__=='__main__':
    data = get_rand_list(num=15)
    print(data)
    print(RadixSort(data))
    print(heap_sort(data))