s = input()
sec = 0
for i in s:
    if ord(i) <= ord('C'):
        sec += 3
    elif ord(i) <= ord('F'):
        sec += 4
    elif ord(i) <= ord('I'):
        sec += 5
    elif ord(i) <= ord('L'):
        sec += 6
    elif ord(i) <= ord('O'):
        sec += 7
    elif ord(i) <= ord('S'):
        sec += 8
    elif ord(i) <= ord('V'):
        sec += 9
    else:
        sec += 10
print(sec)
