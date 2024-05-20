from fractions import Fraction as f
n=int(input())
m=[]
for i in range(1, n):
    for j in range(1, n):
        c=f(j, i)
        if c.numerator + c.denominator == n and f(j, i)<1:
            m.append(f(j, i))
print(max(m), sep='\n')
