# 문자열 -> 배열 -> 문자열
a = input()
arr = []
for i in a:
    arr.append(i)

str_ = ""
arr.sort(reverse=True)

for i in arr:
    str_ += i
print(str_)

arr = ['s','e','a']
print(''.join(arr))

arr = ['o','c','e','a','n']
joinRes = str.join('', arr)
print(joinRes)      #ocean

lst = ['a','b','c','d']
print('+'.join(lst))    #a+b+c+d
