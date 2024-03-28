from math import*

def checkTN(n):
    l=0; r=len(n)-1
    while l<r:
        if n[l]!=n[r]:
            return False
        l+=1; r-=1
    return True

def check(n):
    for i in range(0, len(n), 1):
        if (int(n[i])-48)%2 !=0:
            return False
    return True

if __name__ =='__main__':
    t=int(input())
    while t>0:
        n  =int(input())
        ind =1
        while 10 ** ind <n:
            for i in range (10**ind, 10**(ind+1), 1):
                if i<n and check(str(i)) and checkTN(str(i)):
                    print(i, end=' ')
            ind+=2
        print()
        t-=1
            

