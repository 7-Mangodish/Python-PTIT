from math import*

Nmax=int(1e6)
def check(n):
    if len(n)%2 ==1:
        return False
    l=0; r=len(n)-1

    while (l<r):
        if( int(n[l]) %2 ==1):
            return False
        if(n[l] != n[r]):
            return False
        l+=1
        r-=1
    return True

if __name__ =='__main__':
    t=int(input())
    lt =[]
    for i in range (10, Nmax, 2):
        if(check(str(i))):
            lt.append(i)
    while(t>0):
        n= int(input())
        ind=0
        while(ind <len(lt) and lt[ind] <n):
            print(lt[ind], sep='', end=' ')
            ind+=1
        print()
        t-=1

    
