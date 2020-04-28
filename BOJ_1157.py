# s = input()
# s = s.upper()
# cnt = [0]*(ord('Z')-ord('A')+1)
#
# for i in range(ord('Z')-ord('A')+1):
#     cnt[i] = s.count(chr(i+65))
# if cnt.count(max(cnt)) > 1:
#     print("?")
# else:
#     print(chr(cnt.index(max(cnt))+ord('A')))

n = [3, 6, 5, 3]
print(n.index(3))   # 0
print(max(n))       # 6
print(n.count(3))   # 2