import functools as f

def mul(n):
    mu= 1
    while n>0:
        mu*=n%10
        n//=10
    return mu

def cmp(a, b):
    if mul(a)>mul(b):
        return 1
    elif mul(a)<mul(b):
        return -1
    else:
        if a>b:
            return 1
        else:
            return -1

t= int(input())
for i in range(t):
    n= int(input())
    l=[int(x)for x in input().split()]
    l.sort(key= f.cmp_to_key(cmp))
    for i in l:
        print(i, end=' ')
    print()