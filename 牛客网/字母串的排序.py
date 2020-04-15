# -*- coding:utf-8 -*-
import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss)==0:
            return []
        temp = itertools.permutations(ss)
        temp = [''.join(i) for i in temp]
        temp = list(set(temp))
        temp = sorted(temp)
        return temp


class Solution1:
    def Permutation(self, ss):
        # write code here
        result_set = set()
        if not ss:
            return []
        def permutation(cs, current_s):
            if not cs:
                result_set.add(current_s)
                return
            for index, c in enumerate(cs):
                new_cs = [char for i,char in enumerate(cs) if index!=i]
                permutation(new_cs, current_s+cs[index])
            return
        permutation([c for c in ss], "")
        return sorted(list(result_set))

if __name__=='__main__':
    s = Solution()
    print(s.Permutation('abc'))
    itertools.count()
    for key, group in itertools.groupby('AAABBBCCAAA'):
        print(key, list(group))