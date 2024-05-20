from itertools import product
h = product(['x', 'y', 'nx', 'ny'], repeat=3)
c = 0
for i in list(h)[13:]:
    print(i)
print(c)