# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        position = {}
        counter = {}
        for i,item in enumerate(s):
            if item not in counter:
                counter[item] = 1
                position[item] = i
            else:
                counter[item] += 1
        for key in counter.keys():
            if counter[key]==1:
                return position[key]
        return -1


if __name__=='__main__':
    cl = Solution()
    temp_out = cl.FirstNotRepeatingChar('google')
    print(temp_out)

