from math import*


if __name__== '__main__':
    s =input()
    rev_s=''
    for i in range(len(s)-1, -1, -1):
        rev_s+= s[i]
    ans=''
    for i in range (0, len(rev_s), 1):
        if i%3 ==0  and i!=0:
            ans+= ',' + rev_s[i]
        else:
            ans+= rev_s[i]
    for i in range(len(ans)-1, -1, -1):
        print(ans[i], sep='', end='')

