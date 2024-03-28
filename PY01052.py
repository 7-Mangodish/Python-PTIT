from math import*

def check(n):
    if n<2:
        return False
    for i in range(2, isqrt(n)+1, 1):
        if n%i ==0:
            return False
    return True

if __name__ =='__main__':
    t=int(input())
    while t>0:
        s =input()
        sum=0   
        for i in s:
            sum += int(i)
        if check(sum):
            print('YES')
        else:
            print('NO')
        t-=1