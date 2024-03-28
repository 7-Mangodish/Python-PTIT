

l=[]
ans =[]
l.append('1')
l.append('2')
while(len(ans) <= 1100):
    t = l.pop(0)
    if(t.count('2') > len(t)/2):
        ans.append(int(t))
    l.append(t+ '0')
    l.append(t+'1')
    l.append(t+'2')

ans.sort()
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        print(ans[i], end=' ')
    print()