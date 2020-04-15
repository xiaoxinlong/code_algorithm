# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        numbers = '0123456789'
        dot = '.'
        e = 'eE'
        symbol = '+-'
        all_s = numbers + dot + e

        has_e = 0
        has_dot = 0
        pre = 0
        sym = 0

        if s[0] in '+-':
            s = s[1:]
            sym = 1
        elif s[0] not in numbers:
            return False

        for i in range(len(s)):
            if s[i] in 'eE':
                if has_e: return False
                if i == len(s) - 1:
                    return False
                has_e = True
            elif s[i] in '+-':
                if sym and s[i - 1] not in 'eE':
                    return False
                if not sym and i > 0 and s[i - 1] not in 'eE':
                    return False
                sym = 1
            elif s[i] == '.':
                if has_dot or has_e:
                    return False
                has_dot = 1
            elif s[i] not in numbers:
                return False
        return True


