n = int(input())
arr=[]
for i in range(n):
    a, b= map(int,input().split())
    arr.append(a)
    arr.append(b)
    #arr.append((a,b))
print(arr)

# for i in arr:
#     rank = 1
#     for j in arr:
#         if i[0] < j[0] and i[1] < j[1]:
#             rank += 1
#     print(rank)
for i in range(n):
    rank = 1
    for j in range(n):
        if arr[2*i]<arr[2*j] and arr[2*i+1]<arr[2*j+1]:
            #print(arr[2*i], arr[2*j], arr[2*i+1], arr[2*j+1])
            rank += 1
    print(rank)