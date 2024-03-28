
a=[]
# Dem so luong phan tu trong mang
def init(n):
    a.append(n)

def sinh():
    i= len(a)-1
    while i>=0 and a[i] ==1:
        i-=1
    if i<0:
        return False
    # Dem so chu so 1 tu cuoi 
    tmp= len(a)-i
    a[i]-=1
    # Bieu dien thong qua a[i]
    q= tmp //a[i]
    r= tmp %a[i]
    for j in range(len(a)-i-1):
        a.pop()
    for j in range(q):
        a.append(a[i])
    if r!=0:
        a.append(r)
t= int(input())
for _ in range(t):
    n= int(input())
    init(n)
    ans=[]
    while True:
        tmp=[x for x in a]
        ans.append(tmp)
        if sinh()==False:
            break
    print(len(ans))
    for i in ans:
        print('(', end='')
        for j in range(len(i)):
            if j!= len(i)-1:
                print(i[j], end=' ')
            else:
                print(i[j], end='')
        print(')', end=' ')
    print()
    a.clear()
"""
2
4
5
"""
