from math import*

def fix(l):
    for i in range(len(l)):
        tmp= l[i]-9
        if tmp>0:
            l[i]= chr(64+tmp)

def sol(l, k):
    l.reverse()
    ans=[]
    s=0
    for i in range(len(l)):
        tmp= int(l[i])
        ind = i%k
        if i%k==0:
            ans.append(s)
            s=0
        s+=(tmp *(2**ind))
    if s!=0:
        ans.append(s)
    ans.reverse()
    ans.pop()
    fix(ans)
    for i in ans:
        print(i, end='')
    print()

if __name__ == '__main__':
    with open('Data.in') as f:
        lines= f.readlines()
    for line in lines:
        line= line.rstrip()
    ind = 1
    while ind< len(lines):
        b= int(lines[ind].rstrip())
        a= list(lines[ind+1].rstrip())
        # print(a, b)
        sol(a, int(log(b,2)))
        ind+=2
"""
2
8
10010100010010101
2
10010100010010101
"""
