
def sol(s):
    ans=''
    for i in range(0, len(s), 1):
        if '0' <=s[i] and s[i] <='9':
            for j in range(0, int(s[i]), 1):
                ans+=s[i-1]
    print(ans)


if __name__=='__main__':
    t=int(input())
    while(t>0):
        str= input()
        sol(str)
        t-=1
