from math import*

def check(s):
        if len(l) <3:
            return False
        ind =1
        while( ind<len(l) and l[ind]>l[ind-1] ):
            ind+=1
        if ind == len(l) or ind == 1:
            return False
        while(ind <len(l) and l[ind]<l[ind-1]):
            ind+=1
        if ind == len(l):
            return True
        return False
    
if __name__=='__main__':
    t= int(input())
    while(t>0):
        l= input()
        if(check(l)):
             print('YES')
        else:
             print('NO')
        t-=1

        
