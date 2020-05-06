board_white = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
board_black = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']

n, m = map(int, input().split())
arr=[]
for i in range(n):
    s=input()
    arr.append(s)
#print(arr)

min_res = 64
x = n-8+1
y = m-8+1

for i in range(x):
    for j in range(y):
        min_white = 0
        min_black = 0

        for p in range(i,i+8):
            for q in range(j,j+8):
                if arr[p][q] != board_white[p-i][q-j]:
                   # print("W", p, q)
                    min_white += 1
                if arr[p][q] != board_black[p - i][q - j]:
                   # print("B", p, q)
                    min_black += 1
        min_res = min(min_res, min(min_white,min_black))
        #print("min_res:", min_res)
print(min_res)
# n, m = map(int, input().split())
# arr=[]
# for i in range(n):
#     s=input()
#     arr.append(s)
# #print(arr)
#
# min_res = 10000
# x = n-8+1
# y = m-8+1
# #print(x,y)
#
# #print(arr)
#
# for start_x in range(x):
#     for start_y in range(y):
#         cnt1 = 0
#         cnt2 = 0
#         i = start_x
#         j = start_y
#         #print("start : (",i,",",j,")")
#
#         #(i,j) = W
#         if (arr[i][j]=='W'):    #(i,j) : W
#             #print(i, j, 'W')
#             for p in range(8):
#                 for q in range(8):
#                     if ((i+p)+(j+q)) % 2 == 0:
#                         if arr[i+p][j+q] == 'B':
#                             cnt1+=1
#                         else:
#                             cnt2+=1
#                     else:
#                         if arr[i + p][j + q] == 'W':
#                             cnt1 += 1
#                         else:
#                             cnt2+=1
#             print("W > cnt1=", cnt1, "cnt2 = ", cnt2)
#         #(i,j)==B
#         else:
#             #print(i, j, 'B')
#
#             for p in range(8):
#                 for q in range(8):
#                     if ((i+p)+(j+q)) % 2 == 0:
#                         if arr[i+p][j+q] == 'W':
#                             cnt1 +=1
#                         else:
#                             cnt2 += 1
#                     else:
#                         if arr[i + p][j + q] == 'B':
#                             cnt1 += 1
#                         else:
#                             cnt2 +=2
#             print("B > cnt1=", cnt1, "cnt2 = ", cnt2)
#
#         #print("cnt1 = ", cnt1, "cnt2 = ", cnt2)
#         min_cnt=min(cnt1, cnt2)
#         min_res=min(min_cnt, min_res)
# print(min_res)

# n, m = map(int, input().split())
# arr=[]
# for i in range(n):
#     s=input()
#     arr.append(s)
# #print(arr)
#
# min_res = 10000
# x = n-8+1
# y = m-8+1
# #print(x,y)
#
# #print(arr)
#
# for start_x in range(x):
#     for start_y in range(y):
#         cnt1 = 0
#         cnt2 = 0
#         i = start_x
#         j = start_y
#         #print("start : (",i,",",j,")")
#         if (arr[i][j]=='W'):    #(i,j) : W
#             #print(i, j, 'W')
#             for p in range(8):
#                 for q in range(8):
#                     if ((i+p)+(j+q)) % 2 == 0:
#                         if arr[i+p][j+q] == 'B':
#                             cnt1+=1
#                         else:
#                             cnt2+=1
#                     else:
#                         if arr[i + p][j + q] == 'W':
#                             cnt1 += 1
#                         else:
#                             cnt2+=1
#         else:    #(i,j) : B
#             #print(i, j, 'B')
#             #print("**",arr[i][j],i,j)
#             for p in range(8):
#                 for q in range(8):
#                     if ((i+p)+(j+q)) % 2 == 0:
#                         if arr[i+p][j+q] == 'B':
#                             cnt1 +=1
#                         else:
#                             cnt2 += 1
#                     else:
#                         if arr[i + p][j + q] == 'W':
#                             cnt1 += 1
#                         else:
#                             cnt2 +=2
#         #print("cnt1=", cnt1, "cnt2 = ", cnt2)
#         #print("cnt1 = ", cnt1, "cnt2 = ", cnt2)
#         min_cnt=min(cnt1, cnt2)
#         min_res=min(min_cnt, min_res)
# print(min_res)



###주석제거하면 print문 있는 원래 코드
# n, m = map(int, input().split())
# arr=[]
# for i in range(n):
#     s=input()
#     arr.append(s)
# #print(arr)
#
# min_res = 10000
# x = n-8+1
# y = m-8+1
# print(x,y)
#
# print(arr)
#
# for start_x in range(x):
#     for start_y in range(y):
#         cnt1 = 0
#         cnt2 = 0
#         i = start_x
#         j = start_y
#         print("start : (",i,",",j,")")
#         if (arr[i][j]=='W'):    #(i,j) : W
#             print(i, j, 'W')
#             for p in range(8):
#                 for q in range(8):
#                     if ((i+p)+(j+q)) % 2 == 0:
#                         if arr[i+p][j+q] == 'B':
#                             cnt1+=1
#                         else:
#                             cnt2+=1
#                     else:
#                         if arr[i + p][j + q] == 'W':
#                             cnt1 += 1
#                         else:
#                             cnt2+=1
#         else:    #(i,j) : B
#             print(i, j, 'B')
#             #print("**",arr[i][j],i,j)
#             for p in range(8):
#                 for q in range(8):
#                     if ((i+p)+(j+q)) % 2 == 0:
#                         if arr[i+p][j+q] == 'B':
#                             cnt1 +=1
#                         else:
#                             cnt2 += 1
#                     else:
#                         if arr[i + p][j + q] == 'W':
#                             cnt1 += 1
#                         else:
#                             cnt2 +=2
#         print("cnt1=", cnt1, "cnt2 = ", cnt2)
#         #print("cnt1 = ", cnt1, "cnt2 = ", cnt2)
#         min_cnt=min(cnt1, cnt2)
#         min_res=min(min_cnt, min_res)
# print(min_res)
# if min_cnt==64:
#     print(0)
# else:
#     print(min_res)




# for start_x in range(x):
#     for start_y in range(y):
#         cnt = 0
#         i = start_x
#         j = start_y
#         #print("start : (",i,",",j,")")
#         if (arr[i][j]=='W'):    #(i,j) : W
#             #print('W')
#             for p in range(8):
#                 for q in range(8):
#                     if ((i+p)+(j+q)) % 2 == 0:
#                         if arr[i+p][j+q] == 'B':
#                             cnt+=1
#                     else:
#                         if arr[i + p][j + q] == 'W':
#                             cnt += 1
#         else:    #(i,j) : B
#             #print("**",arr[i][j],i,j)
#             for p in range(8):
#                 for q in range(8):
#                     if ((i+p)+(j+q)) % 2 == 0:
#                         if arr[i+p][j+q] == 'B':
#                             cnt+=1
#                     else:
#                         if arr[i + p][j + q] == 'W':
#                             cnt += 1
#         #print("cnt=", cnt)
#         min_cnt=min(min_cnt, cnt)
# if min_cnt==64:
#     print(0)
# else:
#     print(min_cnt)
