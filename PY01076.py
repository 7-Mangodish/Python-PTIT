from math import*

if __name__ =='__main__':
    t= int(input())
    while t>0:
        n=int(input())
        m=int(input())
        print(gcd(m,n))
        t-=1