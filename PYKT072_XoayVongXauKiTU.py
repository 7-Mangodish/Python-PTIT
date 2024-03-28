Nmod= 10**9 + 7
def cntDiff(x, y):
    a=[_ for _ in x]
    b=[_ for _ in y]
    ind=0
    while ind <len(a) and a!=b:
        tmp=b.pop(0)
        b.append(tmp)
        ind+=1
    if ind == len(a):
        return -1
    return ind


def sol():
    n=int(input())
    l=[]
    for _ in range(n):
        s= [x for x in list(input())]
        l.append(s)
    #print(cntDiff(l[0], l[2]))
    ans=[]
    for i in range(len(l)):
        cnt=0
        for j in range(len(l)):
            if i !=j:
                tmp= cntDiff(l[i], l[j])
                if tmp==-1:
                    print(-1)
                    return
                cnt+=tmp
        ans.append(cnt)
    print(min(ans))
    
    

if __name__=='__main__':
    sol()

"""
4
xzzwo
zwoxz
zzwox
xzzwo

3
aa
aa
aa

2
molzv
lzvmo
"""