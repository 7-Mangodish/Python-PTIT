from math import*

def sol(s):
    l1= list(s)
    l2 =list(reversed(l1))
    for i in range(len(l1)-1):
        if abs(ord(l1[i]) - ord(l1[i+1])) != abs(ord(l2[i]) - ord(l2[i+1])):
            return False
    return True

if __name__ =='__main__':
    t =int(input())
    while t>0:
        s= input()
        if sol(s):
            print('YES')
        else:
            print('NO')
        t-=1