from math import*

def fix(l):
    for i in range(len(l)):
        tmp= l[i]-9
        if tmp>0:
            l[i]= chr(64+tmp)


def sol(s, k):
    l= list(s)
    l.reverse()
    sum= 0
    ans=[]
    for i in range(len(l)):
        tmp= int(l[i])
        ind= i%k
        if i%k==0:
            ans.append(sum)
            sum=0
        sum+= (tmp*(2**ind))
    if sum!=0:
        ans.append(sum)
    ans.reverse()
    ans.pop()
    fix(ans)
    for i in ans:
        print(i, sep='', end='')
            


if __name__=='__main__':
    t= int(input()) 
    while t>0:
        n= int(input())
        s= input()
        sol(s, int(log(n,2)))
        print()
        t-=1