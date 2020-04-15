n = 11111
base = 1
a, b = divmod(n, base)
temp_str = str(n)
length = len(temp_str)
ans = 0
for i in range(length):
    base = 10**(i+1)
    base2 = 10**(i)
    a, b = divmod(n, base)
    a1, b1 = divmod(b, 10**(i))
    if i==0:
        if temp_str[-1]>='1':
            ans += a+1
        else:
            ans += a
    elif i==length-1:
        if temp_str[0]=='1':
            ans += b1 + 1
        else:
            ans += base2
    else:
        if temp_str[len(temp_str)-1-i]=='0':
            ans += (a)*base2
        elif temp_str[len(temp_str)-1-i]=='1':
            ans += (a)*base2 + b1+1
        else:
            ans += (a+1)*base2
    print(ans, base, i, temp_str[len(temp_str)-1-i])



print(ans)