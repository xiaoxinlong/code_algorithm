#coding=utf-8

# 继MIUI8推出手机分身功能之后，MIUI9计划推出一个电话号码分身的功能：首先将电话号码中的每个数字加上8取个位，然后使用对应的大写字母代替
# （"ZERO", "ONE", "TWO", "THREE", "FOUR",
# "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"），
# 然后随机打乱这些字母，所生成的字符串即为电话号码对应的分身。

# 0 : Z
# 0124: 0
# 2 : W
# 0+3+4 : R
# 3+8 : H
# 4 : U  45: F
# 5+7 : V
# 6 : X
# 7+6 : S
# 238 : T   8 : G
# 5689 : I

# from collections import Counter
# n = raw_input()
# for i in range(int(n)):
#     S = Counter(raw_input())
#     print  '0'*S['G']+\
#             '1'*(S['I']-S['F']-S['G']-S['X']+S['U'])+\
#             '2'*S['Z']+\
#             '3'*(S['O']-S['U']-S['Z']-S['W'])+\
#             '4'*S['W']+\
#             '5'*(S['R']-S['Z']-S['U'])+\
#             '6'*S['U']+\
#             '7'*(S['F']-S['U'])+\
#             '8'*S['X']+\
#             '9'*(S['S']-S['X'])

from collections import Counter
temp_data = input()
N = int(temp_data.split()[0])

telephone_number = []
for i in range(N):
    temp_data = input()
    temp_count = Counter(temp_data)

    num_0 = temp_count['Z']
    num_2 = temp_count['W']
    num_4 = temp_count['U']
    num_6 = temp_count['X']
    num_8 = temp_count['G']                                # 0
    num_1 = temp_count['O'] - num_0 - num_2 -num_4
    num_5 = temp_count['F'] - num_4
    num_7 = temp_count['S'] - num_6
    num_3 = temp_count['H'] - num_8
    num_9 = temp_count['I'] - num_5 - num_6 - num_8

    temp_c = [num_8,num_9,num_0, num_1,num_2,num_3,num_4,num_5,num_6,num_7]
    temp_str = "".join([str(i) if c>0 else "" for i,c in enumerate(temp_c)])
    telephone_number.append(temp_str)
    print(temp_str)

# for i in telephone_number:
    # print(i)
