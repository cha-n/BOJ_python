N = int(input())
d = 0
n = 1 + 6*d
while N > n:
    d += 1
    n = n + 6*d
print(d+1)
