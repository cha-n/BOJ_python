n = int(input())
for i in range(n):
    for j in range(n):
        a=i
        b=j
        while a!= 0 or b!=0:
            if a%3 ==1 and b%3==1:
                print(" ", end="")
                break
            else:
                a/=3
                b/=3
        if a==0 and b==0:
            print("*", end="")
    print()
#
# n = 27
# arr = [["*"]*(n)]*(n)
# print(arr)
# for i in range(n//3):
#     for j in range(n//3):
#         if i%3 == 1 and j%3 == 1:
#             arr[i][j] = " "
#
# print(" 만들어")
# for i in range(n//3):
#     for j in range(n//3):
#         print(arr[i][j],end="")
#     print()
#
#
#
#
#
# def star(n):
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if cnt != n * n // 2:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#             cnt += 1
#         print()
#
#
# def blank(n):
#     for i in range(n):
#         for j in range(n):
#             print("O", end="")
#         print()
# # n = 3
# # cnt = 0
# # # for i in range(n):
# # #     for j in range(n):
# # #         if cnt != n*n//2:
# # #             print("*", end="")
# # #         else:
# # #             print(" ", end="")
# # #         cnt += 1
# # #     print()
# #
# # for i in range(2):
# #     blank(3)
# #     star(3)
# #
# #
# # m = 9
# # cnt = 0
# # # print("for")
# # # print(3*3//2)
# # # for i in range(0,m,3):
# # #     for j in range(0,m,3):
# # #
# # #         if cnt != 3*3//2:
# # #             star(3)
# # #         else:
# # #             blank(3)
# # #         cnt += 1
# # #     print()