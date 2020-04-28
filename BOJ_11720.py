n=int(input())
n_arr=input()
sum=0

for i in n_arr:
    sum+=int(i)
print(sum)

input()
print(sum(map(int,input())))