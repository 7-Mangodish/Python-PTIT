from math import*

if __name__ == '__main__':
    t=int(input())
    while(t>0):
        s= input()
        if s[ len(s)-2:] == '86':
            print('YES')
        else:
            print('NO')
        t-=1