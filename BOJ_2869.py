A, B, V = map(int, input().split())

X = V - A
Y = A - B
if X % Y != 0:
    print(int(X/Y) + 2)
else:
    print(int(X/Y) + 1)