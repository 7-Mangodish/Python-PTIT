from math import*

if __name__ == '__main__':
    n, k=map(int, input().split())
    cnt=0
    for i in range(10**(k-1), 10**k):
        if( gcd(i, n)==1):
            if(cnt <10):
                cnt+=1
                print(i, sep='', end=' ')
            else:
                print()
                print(i, sep='', end=' ')
                cnt=1