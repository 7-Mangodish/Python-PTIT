from math import*

nmax= 10**5+1
l= list(range(nmax))
def seive():
    l[0]=0; l[1]=0
    for i in range(2, isqrt(nmax)+1, ):
        if l[i]!=0:
            for j in range(i*i, nmax, i):
                l[j]=0


if __name__ =='__main__':
    seive()
    a=[0]
    for i in range(len(l)):
       if l[i]!=0:
            a=a+[i]
    n,x= map(int, input().split())
    # print(a)
    for i in range(n+1):
        x+=a[i]
        print(x, end=' ')