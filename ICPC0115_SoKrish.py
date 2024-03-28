from math import*

gt= [1]*10

def init():
    for i in range(1,10):
        gt[i]= i*gt[i-1]

def check(n):
    beg= n
    s=0
    while n>0:
        s+= gt[n%10]
        n//=10
    if s!= beg:
        return False
    return True

if __name__=='__main__':
    t =int(input())
    init()
    while t>0:
        n= int(input())
        if check(n):
            print('Yes')
        else:
            print(('No'))
        t-=1