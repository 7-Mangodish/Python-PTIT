from math import *

def check(str):
    for i in range(0, len(str), 1):
        if str[i] != '4' and str[i] !='7':
            return False
    return True

if __name__=='__main__':
    t=int(input())
    while(t>0):
        str =input()
        if check(str):
            print('YES')
        else:
             print('NO')
        t-=1