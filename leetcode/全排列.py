import itertools

a = itertools.permutations([i for i in range(6)])
for i in a:
    print(i)