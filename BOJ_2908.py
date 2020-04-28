def f(n):
    rev = ""
    while n/10 > 0:
        rev += str(n % 10)
        n = int(n/10)
    return int(rev)


# n1, n2 = input().split()
# print(max(f(int(n1)), f(int(n2))))
# n1="1234"
# print(n1[::-1])

print(max(input()[::-1].split()))