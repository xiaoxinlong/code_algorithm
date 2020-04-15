class Solution:
    def __init__(self):
        self.nums = []
    def Insert(self, num):
        # write code here
        if self.nums==[]:
            self.nums.append(num)
        else:
            for i in range(len(self.nums)):
                if self.nums[i]>=num:
                    self.nums = self.nums[:i]+[num]+self.nums[i:]
                    return
            self.nums.append(num)
    def GetMedian(self):
        # write code here
        length = len(self.nums)
        if length%2==1:
            return self.nums[length//2]
        else:
            return (self.nums[length//2-1]+self.nums[length//2])/2

if __name__=='__main__':
    data = [5,2,3,4,1,6,7,0,8]
    s = Solution()
    for i in data:
        s.Insert(i)
        # print(s.nums)
        print(s.GetMedian())