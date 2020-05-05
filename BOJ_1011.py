T = int(input())
for i in range(T):
    x, y = map(int,input().split())

    if y - x == 3:
        print(3)
    else:
        half = (x + y) / 2
        cnt = 1
        k = 1
        x = x + k
        k_arr = [1]
        while x < half:
            k = k + 1
            k_arr.append(k)
            x = x + k
            cnt += 1

        if x == half:
            print(cnt * 2)
        else:
            if x + (sum(k_arr) - k_arr[-1]) == y:
                print(cnt * 2 - 1)
            elif x + (sum(k_arr) - k_arr[-1]) > y:
                print(cnt * 2 - 1)
            else:
                print(cnt * 2)

# # x = int(input())
# # y = int(input())
# x = 45
# y = 50
# if y - x == 3:
#     print(3)
# else:
#     half = (x + y) / 2
#     cnt = 1
#     k = 1
#     x = x + k
#     k_arr = [1]
#     while x < half:
#         k = k + 1
#         k_arr.append(k)
#         #print("k_arr = ", k_arr)
#         x = x + k
#         cnt += 1
#
#     #print("x = ", x, "sum(k_arr) = ", sum(k_arr) - k_arr[-1])
#     #print(x + sum(k_arr) - k_arr[-1])
#     if x == half:
#         print(cnt * 2)
#     else:
#         if x + (sum(k_arr) - k_arr[-1]) == y:
#             print(cnt * 2 - 1)
#         else:
#             print(cnt * 2)
#
#
# # else:
# #     if x == y-1:
# #         print(cnt+1)
# #     else:
# #         print("x!=half", cnt*2 -1)



T = int(input())
for i in range(T):
    x, y = map(int,input().split())

    half = (x + y) / 2
    cnt = 1
    k = 1
    x = x + k
    k_arr = [1]
    while x < half:
        k = k + 1
        k_arr.append(k)
        x = x + k
        cnt += 1

    if x == half:
        print(cnt * 2)
    else:
        if x + (sum(k_arr) - k_arr[-1]) == y:
            print(cnt * 2 - 1)
        elif x + (sum(k_arr) - k_arr[-1]) > y:
            print(cnt * 2 - 1)
        else:
            print(cnt * 2)


