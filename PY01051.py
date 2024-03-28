from math import*

def check(s):
    if len(s)<=1:
        return False
    l=0; r=len(s)-1
    while l<r:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True
if __name__ =='__main__':
    t=int(input())
    while t>0:
        s =input()
        sum=0   
        for i in s:
            sum += int(i)
        if check(str(sum)):
            print('YES')
        else:
            print('NO')
        t-=1
