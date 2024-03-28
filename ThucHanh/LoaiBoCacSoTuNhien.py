
with open('Data.in') as f:
    lines = f.readlines()
for l in lines:
    l = l.rstrip()

a=[]
for l in lines:
    tmp = l.split()
    for j in tmp:
        a.append(j)
ans=[]
for i in a:
    if len(i) >10:
        ans.append(i)
    try:
        tmp= int(i)
    except:
        ans.append(i)
ans.sort()
for i in ans:
    print(i, end=' ')