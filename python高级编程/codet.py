
from collections import deque
from collections import Counter
import queue

# q = deque()
# q.append()
# q.appendleft()
# q.pop()
# q.popleft()
#
# q1 = queue.Queue()
# q1.put()
# q1.get()

temp = input()

ans = ""
t = set()
for i in temp:
    if i not in t:
        t.add(i)
        ans += i
print(ans)
