A, B, C = map(int, input().split())
cnt = 0

if B>C or (B==C and A>0):
    cnt = -2
else:
    cnt = int(A/(C-B))
print(cnt+1)