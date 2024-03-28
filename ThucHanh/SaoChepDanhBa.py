from math import*

def sol(n, k):
    center= 2**(n-1)
    if k <center:
        return sol(n-1, k)
    if k >center:
        return sol(n-1, k-center)
    return n

if __name__=='__main__':
    t= int(input())
    while t>0:
        n, k= map(int, input().split())
        ans= sol(n,k)
        print(chr(64+ans))
        t-=1
"""
2
3 2
4 8
"""