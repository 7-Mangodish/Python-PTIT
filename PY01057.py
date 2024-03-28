from math import*

def IsPrime(c):
    if c=='2' or c=='3' or c=='5' or c=='7':
        return True
    return False

def check(s):
    for i in range(len(s)):
        if IsPrime(str(i)) != IsPrime(s[i]):
            return False
    return True
        

if __name__ =='__main__':
    t =int(input())
    while t>0:
        s= input()
        if check(s):
            print('YES')
        else:
            print('NO')
        t-=1

