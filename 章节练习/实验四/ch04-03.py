str = input("请输入一段英文文本")
s = str.split()
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        continue
    else:
        print(s[i], end=' ')
print(s[i + 1])
