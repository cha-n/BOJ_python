T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        X = N // H
        Y = H
    else:
        X = N // H + 1
        Y = N % H
    if X < 10:
        X = '0' + str(X)
    else:
        X = str(X)
    Y = str(Y)
    print(Y+X)
