from random import *
a = [[0 for i in range(5)] for j in range(5)]
for i in range(len(a)):
    for j in range(len(a)):
        a[i][j] = randint(1, 75)
        if i == 2 and j == 2:
            a[i][j] = 0
for i in a:
    print(*i)
