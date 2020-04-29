X = int(input())
n = 1
p = 0
p = p + n
while X > p:
    n = n+1
    p = p+n
p = p-n
if n % 2 == 0:
    print(str(X-p)+"/"+str(n-(X-p)+1))
else:
    print(str(n-(X-p)+1)+"/"+str(X-p))

