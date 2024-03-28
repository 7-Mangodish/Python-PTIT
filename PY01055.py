from math import*

def check(s):
    if s[0] == s[1]:
        return False
    for i in range (0, len(s)-2, 2):
        if s[i]!=s[i+2]:
            return False
    return True

if __name__ =='__main__':
    t =int(input())
    while t>0:
        s= input()
        if len(s) %2 ==1 and check(s):
            print('YES')
        else:
            print('NO')
        t-=1
        