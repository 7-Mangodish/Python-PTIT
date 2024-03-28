
def sol(n):
    s=0
    ans=[]
    for i in range(len(n)):
        ind = i%3
        if ind ==0:
            ans.append(s)
            s=0
        s+=(n[i]*(2**ind))
    if s!=0:
        ans.append(s)
    ans.reverse()
    ans.pop()
    for i in ans:
        print(i,end='')
    print()
    
s=[int(x) for x in input()]
s.reverse()
sol(s)