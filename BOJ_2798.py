n, m = map(int, input().split())
arr= list(map(int, input().split()))

res_arr=[]
res = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum=arr[i]+arr[j]+arr[k]
            if sum<=m:
                res = max(res,sum)
            #res_arr.append(sum)
            #print("i = ", i, ", j = ", j, ", k = ", k, ", sum = ", sum)
print(res)
# res_arr.sort()
# for i in range(len(res_arr)):
#     if res_arr[i]> m:
#         break
#
# print(res_arr[i-1])


# arr = [5,6,7,8,9]
# n = len(arr)
# m = 21
# res_arr = []
# for i in range(n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             sum=arr[i]+arr[j]+arr[k]
#             res_arr.append(sum)
#             print("i = ", i, ", j = ", j, ", k = ", k, ", sum = ", sum)
# print(res_arr)
# res_arr.sort()
# print(res_arr)
# for i in range(len(res_arr)):
#     if res_arr[i]> m:
#         break
# print(i)
# print(res_arr[i-1])