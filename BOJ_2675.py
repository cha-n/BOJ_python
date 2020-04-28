# T = int(input())
# for i in range(T):
#     R, S = input().split()
#     R = int(R)
#     for i in range(len(S)):
#         for j in range(R):
#             print(S[i], end="")
#     print()
#     # R = int(input())
#     # S = input()
#     # for i in range(len(S)):
#     #     for j in range(R):
#     #         print(S[i], end="")
#     # print()


T = int(input())
result = ""
for i in range(T):
    R, S = input().split()
    R = int(R)
    for j in S:
        result = result+(j*R)
    print(result)
    result = ""

# A="C"
# print(A*5)