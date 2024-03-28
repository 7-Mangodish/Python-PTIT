cnt =[0]*1000
ans= list()
s= input()
for i in range(0, len(s)-1, 2):
    if i+1 >= len(s):
        break
    n= int(s[i] + s[i+1])
    if n not in ans:
        cnt[n]+=1
        ans.append(n)
    else:
        cnt[n] +=1
for i in ans:
    print(i, cnt[i])
'124356141111434356149'