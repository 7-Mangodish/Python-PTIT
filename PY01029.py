from math import*

if __name__ =='__main__':
    t =int(input())
    while t>0:
        num1 = int(input())
        tmp = list(str(num1))
        tmp.reverse()
        num2=0
        for i in tmp:
            num2= num2*10 +int(i)
        if(gcd(num1, num2) ==1):
            print('YES')
        else:
            print('NO')
        t-=1