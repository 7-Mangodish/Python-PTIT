
ans= list()
s= input()
for i in range(0, len(s), 2):
    if i+1 >= len(s):
        break
    s1= s[i] + s[i+1]
    if int(s1) not in ans:
        ans.append(int(s1))
ans.sort()
for i in ans :
    print(i, end=' ')
'124356141111434356149'
