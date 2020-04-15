#
# 计算有多少对符合条件的数对
# @param a int整型一维数组 数组a
# @param b int整型一维数组 数组b
# @return int整型
#
class Solution:
    @classmethod
    def countLR(self, a, b):
        # write code here
        n = len(a)
        sum_a = [0] * n
        ans = 0
        temp = 0
        for i in range(n):
            temp += a[i]
            sum_a[i] = temp

        print(sum_a)
        for l in range(n):
            for r in range(l, n):
                if sum_a[r] - sum_a[l] + a[l] == b[r] + b[l]:
                    ans += 1
        return ans

print(Solution.countLR([1,2,3,4],[2,1,4,5]))