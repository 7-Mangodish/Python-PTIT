from math import*

def sol(s):
    tmp=s[0]
    cnt=1
    ans=' '
    for i in range(1, len(s), 1):
        if s[i]!=tmp:
            ans+= str(cnt) +tmp
            cnt=1
            tmp=s[i]
        else:
            cnt+=1
    print(ans)

if __name__ == '__main__':
    t =int(input())
    while(t>0):
        s=input()
        sol(s)
        t-=1