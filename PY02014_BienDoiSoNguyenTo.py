from math import*

Nmax= 10005
p=[1]*Nmax
a=[]
def seive():
    p[0]=p[1]=0
    for i in range(2, isqrt(Nmax)):
        if p[i]==1:
            j= i*i
            while j<Nmax:
                p[j]=0
                j+=i
    for i in range(Nmax):
        if p[i]==1:
            a.append(i)

# tim gia tri nho hon gan nhat tai n
def Small(n):
    l=0
    r= len(a)-1
    pos= Nmax
    while l<=r:
        m= (l+r)//2
        if a[m] == n:# neu ton tai trong day a -> la so nguyen to
            return m
        elif a[m]<n: # Xet xem lieu co so nao nho hon n dang sau no khong
            pos= m
            l= m+1
        else:
            r= m-1
    return pos
# Tra ve index ma a[index] la phan tu dau tien lon hon n 
def Greater(n):
    l=0
    r= len(a)-1
    pos =Nmax
    while l <=r:
        m=(l+r)//2
        if a[m] ==n: # neu ton tai trong day a -> la so nguyen to
            return m
        elif a[m]> n:# Xet xem lieu co so nao nho hon n dang sau no khong
            pos= m
            r= m-1
        else:
            l= m+1
    return pos

seive()
n= int(input())
l=[int(x) for x in input().split()]
ans=[0]*len(l)
for i in range(len(l)):
    i1= Small(l[i]); i2= Greater(l[i])
    # print(a[i1], a[i2])
    ans[i]= min(abs(a[i1] - l[i]), abs(a[i2] - l[i]))
print(max(ans))
"""
8
13 5 8 7 9 15 26 34
"""