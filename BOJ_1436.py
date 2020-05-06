# a=6666
# print(str(a))
# print(type(a))
# c=str(a).find("66")
# print(a)
# print(c)

cnt = 0
i=666
n=int(input())
while cnt < n:
    if str(i).find("666") != -1:

        cnt+=1
    i+=1
print(i-1)