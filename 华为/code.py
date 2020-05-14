import random

def solution(s):
    temp_s = str(s)
    temp_s = temp_s[2:]
    temp_s = '0'*(32-len(temp_s)) + temp_s
    new_s = temp_s[::-1]
    t = int(new_s,base=2)
    t = bin(t)
    return t

if __name__=='__main__':
    a = random.randint(0,1000)+2**31
    print(bin(a))
    print(solution(bin(a)))