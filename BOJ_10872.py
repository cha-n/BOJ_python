def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n-1)

print(fac(int(input())))


# def fac(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         res = 1
#         for i in range(1,n+1):
#             res *= i
#         return res
#
# print(fac(int(input())))

# import math
# print(math.factorial(int(input())))