from math import *

if __name__ =='__main__':
    t =int(input())
    while t>0:
        str =input()
        tmp1 =str[:2]
        tmp2 =str[len(str)-2:]
        if tmp1 ==tmp2:
            print('YES')
        else:
            print('NO')
