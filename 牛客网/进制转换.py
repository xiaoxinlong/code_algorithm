#coding=utf-8

#进制转换

#2->8
n = '1010'
print(oct(int(n,2)))

#10->2
n = '-10'
print(bin(int(n,10)))
print(bin(10))

#位运算
print(bin(-10 & 0xffffffff))
