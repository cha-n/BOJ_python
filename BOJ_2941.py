s = input()
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in cro:
    s=s.replace(i,'.')
print(len(s))






# cnt = 0
# i = 0
# while i < len(s):
#     if s[i] == 'c':
#         if s[i+1] == '=' or s[i+1] == '-':
#             i = i+2
#             cnt += 1
#         else:
#             i += 1
#             cnt += 1
#     elif s[i] == 'd':
#         if s[i+1] == 'z':
#             if s[i+2] == '=':
#                 i += 3
#                 cnt += 1
#             else:
#                 i += 2
#                 cnt += 1
#         else:
#             i += 1
#             cnt += 1
#     elif s[i] == 'l':
#         if s[i+1] == 'j':
#             i += 2
#             cnt += 1
#         else:
#             i += 1
#             cnt += 1
#     elif s[i] == 'n':
#         if s[i+1] == 'j':
#             i += 2
#             cnt += 1
#         else:
#             i += 1
#             cnt += 1
#     elif s[i] == 's':
#         if s[i+1] == '=':
#             i += 2
#             cnt += 1
#         else:
#             i += 1
#             cnt += 1
#     elif s[i] == 'z':
#         if s[i+1] == '=':
#             i += 2
#             cnt += 1
#         else:
#             i += 1
#             cnt += 1
#     else:
#         i += 1
#         cnt += 1
# print(cnt)



