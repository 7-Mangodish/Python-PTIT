
def check(s):
    l =0
    r = len(s)-1
    while(l<r):
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True

with open('E:\CODE\Python\ThucHanh\VANBAN.in') as f:
    l = f.readlines()

d = dict()
ans =0
for i in l:
    tmp = i.split()
    for j in tmp: 
        if check(j):
            ans = max(ans, len(j))
            if j in d.keys():
                d[j] = d[j] +1
            else:
                d[j] =1

for i in d.keys():
    if len(i) == ans:
        print(i, d.get(i))