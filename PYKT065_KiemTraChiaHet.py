
while True:
    s= input()
    if s=='-1':
        break
    l, r= map(int, s.split())
    n= int(input())

    ans =0
    for i in range(l, r+1):
        ok =True
        for j in range(2, n+1):
            if(i % j ==0):
                ok = False
                break
        if ok ==True:
            ans +=1
    
    print(ans)

"""
1 10
10
2001 2309
50
34 2003
50
-1
"""      