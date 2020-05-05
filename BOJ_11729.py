def hanoi(n, frm, tmp, to):
    if n == 1:
        print(frm, to)
    else:
        hanoi(n-1, frm, to, tmp)
        print(frm, to)
        hanoi(n-1, tmp, frm, to)

N = int(input())
print(pow(2,N) -1)
hanoi(N, 1,2,3)