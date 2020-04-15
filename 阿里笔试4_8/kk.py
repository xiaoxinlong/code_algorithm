# 判断一个无序数组中，有多少对数之和小于等于K.


def solution(arr, K):
    arr = sorted(arr)

    left = 0
    right = len(arr) - 1
    count = 0

    while left < right:
        if arr[left] + arr[right] <= K:
            count += (right - left)
            left += 1
        else:
            right -= 1

    return count



print(solution([0,1,2,3,4,5],6))