n = int(input())

con = 1
while con < n:
    sum = con
    tmp = con
    while tmp > 0:
        sum += tmp%10
        tmp = tmp//10
    if sum==n:
        break
    con += 1
if con == n:
    print(0)
else:
    print(con)
