from math import*

def sol1(n):
    ans =0
    for i in range (2, n+1, 2):
        ans+=(1/i)
    print('%.6f' %ans)

def sol2(n):
    ans=0
    for i in range (1, n+1, 2):
        ans += (1/i)
    print('%.6f' %ans)

if __name__=='__main__':
    t=int(input())
    while(t>0):
        n =int(input())
        if (n%2==0):
            sol1(n)
        else:
            sol2(n)
        t-=1

