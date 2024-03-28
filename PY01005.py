from math import *

def check(str):
    cnt=0
    for i in range(0, len(str), 1):
        if str[i] == '4' or str[i] =='7':
            cnt+=1
    if cnt==4 or cnt==7:
        return True
    return False

if __name__=='__main__':
    str =input()
    if check(str):
        print('YES')
    else:
        print('NO')