# 2 Con tro
t = int(input())
for _ in range(t):
    n = int(input())
    ar = [int(x) for x in input().split()]
    ar.sort()
    cnt =0
    for i in range(n-2):
        l = i+1
        r = n-1
        while l<r:
            if ar[i] + ar[l] + ar[r] ==0:
                cnt +=1 
                l+=1 # Kiem tra xem lieu con so nao thoa man hay k
            elif ar[i] + ar[l] + ar[r] >0:
                r-=1
            else:
                l+=1
    print(cnt)
            

"""
2
5
0 -1 2 -3 1 
5
1 -2  1  0  5
"""