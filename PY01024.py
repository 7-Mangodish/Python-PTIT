from math import*

def check(s):
    sum=0
    for i in range(0, len(s)):
        sum+=int(s[i])

    if sum%10 !=0:
        return False
    for i in range(0, len(s)-1, 1):
        if abs(int(s[i]) - int(s[i+1]) )!=2:
            return False
    return True

if __name__=='__main__':
    t=int(input())
    while t>0:
        s=input()
        if check(s):
            print('YES')
        else:
            print('NO')
        t-=1