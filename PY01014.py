from math import*

if __name__=='__main__':
    a,k,n =map(int, input(). split())
    min= (int(a/k) + 1) * k - a
    max= (int(n/k) + 1) * k - a
    if min+k >max:
        print("-1")
    else:
        for i in range(min, max, k):
            print(i,end=' ')
        
    
