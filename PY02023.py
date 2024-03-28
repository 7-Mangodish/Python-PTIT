from math import*
import functools

def sum(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s
def condition(a, b):
    if sum(a)>sum(b):
        return 1
    elif sum(a)<sum(b):
        return -1
    else:
        if a>b:
            return 1
        else :
            return -1

t= int(input())
while t>0:
    n= int(input())
    l= [int(x) for x in input().split()]
    l.sort(key=functools.cmp_to_key(condition))
    for i in l:
        print(i, end=' ')
    print()
    t-=1