from math import*

def sol(s1):
    s2 =list(reversed(s1))
    for i in range(0, len(s1)-1, 1):
        if abs( ord(s1[i]) - ord(s1[i+1])) != abs( ord(s2[i]) - ord(s2[i+1])):
            return False
    return True

if __name__ =='__main__':
    t= int(input())
    while t>0:
        s = input()
        s= list(s)
        if sol(s):
            print('YES')
        else:
            print('NO')
        t-=1
