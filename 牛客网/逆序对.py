# -*- coding:utf-8 -*-
class Solution:
    @classmethod
    def InversePairs(self, data):
        # write code here
        global count
        count = 0
        def merge_sort(nums):
            global count
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            l, r = len(left)-1, len(right)-1
            res = []
            while l>=0 and r>=0:
                if left[l] <= right[r]:
                    res.append(right[r])
                    r -= 1
                else:
                    count += r+1
                    res.append(left[l])
                    l -= 1
            if l >= 0:
                res = res + left[:l+1][::-1]
            if r >=0 :
                # count += (r+1)*len(left)-1
                res =  res + right[:r+1][::-1]
            return res[::-1]
        merge_sort(data)
        return count%1000000007