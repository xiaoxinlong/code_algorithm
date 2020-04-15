class Solution:
    @classmethod
    def minimumValueAfterDispel(self , nums ):
        # write code here
        nums = sorted(nums)
        sum_nums  = sum(nums)
        dec = 0
        for a in range(len(nums)):
            ab = a
            for b in range(a+1):
                while(ab<len(nums) and nums[ab]<nums[a]+nums[b]):
                    ab += 1
                tmp = nums[b]*(a-b)+nums[a]*(ab-a)+(nums[a]+nums[b])*(len(nums)-ab)
                dec = max(dec, tmp)
        for a in range(len(nums)):
            b = 0
            for ab in range(a, len(nums)):
                while(b<a and nums[b]<nums[ab]-nums[a]):
                    b += 1
                tmp = (nums[ab]-nums[a])*(a-b)+nums[a]*(ab-a)+(nums[ab])*(len(nums)-ab)
                dec = max(dec, tmp)
        for b in range(len(nums)):
            a = b
            for ab in range(b, len(nums)):
                while(a<ab and nums[a]<nums[ab]-nums[b]):
                    a += 1
                tmp = nums[b]*(a-b)+(nums[ab]-nums[b])*(ab-a)+(nums[ab])*(len(nums)-ab)
                dec = max(dec, tmp)
        return sum_nums - dec



print(Solution.minimumValueAfterDispel(nums=[2, 3, 3, 3, 3, 4, 4, 4, 4, 4]))