n = [-1]*26
str = input()
print(n)
for i in range(len(str)):
    if n[ord(str[i])-97] == -1:
        n[ord(str[i])-97] = i

for i in range(len(n)):
    print(n[i], end=" ")