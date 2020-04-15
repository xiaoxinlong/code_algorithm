# -*- coding:utf-8 -*-
class Solution:
    @classmethod
    def StrToInt(self, s):
        # write code here
        if len(s)==0:
            return 0
        numbers_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        num_dict = {i: j for i, j in zip(numbers_char, numbers)}
        # 第一个字符
        symbol = 0
        ss = s
        if s[0] == '-':
            symbol = 1
            ss = s[1:]
        elif s[0] == '+':
            symbol = 0
            ss = s[1:]
        elif s[0] not in num_dict:
            return 0

        if len(ss)==0:
            return 0
        ans = 0
        for i in ss:
            if i in num_dict:
                ans = ans * 10 + num_dict[i]
            else:
                return 0
        return ans if symbol == 0 else -ans


if __name__=='__main__':
    print(Solution.StrToInt(s='123'))