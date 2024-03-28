

if __name__ =='__main__':
    t=int(input())
    while t>0:
        s =input()
        mul= 1
        for i in s:
            if int(i)!=0:
                mul *= int(i)
        print(mul)
        t-=1