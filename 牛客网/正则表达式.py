import re

s = 'aaabaaca'
patten = 'a.*a'

s = 'aaaa'
patten = re.compile(patten+"$")
result = patten.match(s)
print(patten)
print(result.group())

data1 = re.findall(pattern=patten,string=s)
data2 = re.match(patten,s)
print(data1)
print(data2.group())
print('ss')