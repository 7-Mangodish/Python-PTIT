from math import*

def check(s):
    for i in range(0, len(s)-1, 1):
        if(s[i] == s[i+1]):
            return False
    s1=s[0]
    s2=s[1]
    for i in s:
        if i!= s1 and i!=s2:
            return False
    return True

if __name__ == '__main__':
    t=int(input())
    while(t>0):
        s= input()
        if(check(s)):
            print('YES')
        else:
            print('NO')
        t-=1
