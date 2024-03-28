from math import*

nmax= 10**18
a= log(nmax, 2)
b= log(nmax, 3)
c= log(nmax, 5)
ans= []

def ktao():
    for i in range(int(a)+1):
        for j in range(int(b)+1):
            for k in range(int(c)+1):
                ans.append( (5**k)*(3**j)*(2**i))
    ans.sort()

def bi_search(x):
    l= 0
    r= len(ans)-1
    while l<=r:
        m= (l+r)//2
        if ans[m]== x:
            return m+1
        elif ans[m] <x:
            l= m+1
        else:
            r= m-1
    return 'Not in sequence'

if __name__ =='__main__':
    ktao()
    t= int(input())
    # for i in range(11):
    #     print(ans[i])
    for i in range(t):
        n= int(input())
        print(bi_search(n))


