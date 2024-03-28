from math import *

def check(str):
    cnt =0
    for i in range(0,len(str), 1 ):
        if str[i] >='a' and str[i]<='z':
            cnt-=1
        else:
            cnt+=1
    if(cnt<=0):
        return False
    return True

if __name__ == '__main__':
    str =input()
    if(check(str)):
        print(str.upper())
    else:
        print(str.lower())