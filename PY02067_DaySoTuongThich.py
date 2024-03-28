
def sol(k, a):
    res= 1
    for i in range(1, k+1):
        l= []
        ok= True
        for j in a:
            l.append(j//i)
        for j in range(len(l)):
            if a[j] // l[j] != i:
                ok= False
                break
        if ok== True:
            res=i
    v=[]
    for i in a:
        v.append(i//res)
    print(v)
        

t= int(input())
a=[int(x) for x in input().split()]
k= min(a)
ind =[x//k for x in a]
sol(k, a)
