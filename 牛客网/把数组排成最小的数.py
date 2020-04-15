# -*- coding:utf-8 -*-
import itertools



a = [1,1,1,10,9]
a = [str(i) for i in a]

count = itertools.permutations(a)
ans_ser = set([int(''.join(i)) for i in count])
print(min(ans_ser))