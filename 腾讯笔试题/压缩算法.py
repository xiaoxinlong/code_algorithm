import pdb

s = 'HG[3|B[2|CA]]F'
# s = input()
queue = []
length = len(s)
ans = []
i = 0
while(i<len(s)):
    if s[i]=='[' or s[i]=='|':
        queue.append(i)
        i += 1
    if s[i]==']':
        k = queue[-1]
        queue.pop()
        left = queue[-1]
        queue.pop()
        num = int(s[left+1:k])
        s1 = s[k+1:i]
        s2 = s1*num
        s = s[:left] + s2 + s[i+1:]
        i = left+len(s2)-1
    i += 1
print(s)
print('HGBCACABCACABCACAF')