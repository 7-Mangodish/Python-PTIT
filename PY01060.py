from math import*

def sum(s):
    res =0
    for i in range (1,len(s),2):
            res+=int(s[i])
    return res

def mul(s):
    res= 1
    for i in range(0, len(s), 2):
        if int(s[i])!=0:
            res*= int(s[i])
    return res

if __name__ =='__main__':
    t =int(input())
    while t>0:
        s = input()
        print( mul(s), sum(s))
        t-=1
