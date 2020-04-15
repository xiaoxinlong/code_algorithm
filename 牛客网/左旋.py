# -*- coding:utf-8 -*-
from collections import deque

s = 'abcXYZdef'
n = 3
a = deque(s[::-1])
a.rotate(n)
print(list(a)[::-1])
