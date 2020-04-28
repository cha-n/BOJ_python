# N = int(input())
# cnt = 0
# for j in range(N):
#     s = input()
#     for i in range(len(s)):
#         a = s.find(s[i], 0, i)
#         if a != -1:
#             if s[i] != s[i - 1]:
#                 if i == len(s) - 1:
#                     i -= 1
#                 break;
#     if i == len(s) - 1:
#         cnt += 1
# print(cnt)
# for i in range(len(s)):
#     a = s.find(s[i], 0, i)
#     print(s[i], a)
#     if a != -1:
#         if s[i] != s[i-1]:
#             if i == len(s)-1:
#                 i -= 1
#             break;
#
# if i == len(s)-1:
#     cnt += 1
# print(cnt)

a=input()
print(list(a))
print(sorted(a, key=a.find):)