from math import*

def sol(n, k):
    ans=[]
    while  n >0:
        tmp =n%k
        ans.append(tmp)
        n//=k
    for i in range (len(ans)):
        if ans[i] >9:
            tmp= ans[i]-9+64
            ans[i]=chr(tmp)
    ans.reverse()
    for i in ans:
        print(i, sep='', end='')

if __name__ == '__main__':
    t =int(input())
    while t>0:
        n, b= map(int, input().split())
        sol(n,b)
        print()
        t-=1
