
def sol(a1, a2):
     i1, i2= 0, 0
     ans=[]
     while i1 <len(a1) and i2< len(a2):
        if i1 >= len(a1) or i2 >= len(a2):
            break
        if a1[i1]== a2[i2]:
            ans.append(a1[i1])
            i1+=1
            i2+=1
        elif a1[i1] < a2[i2]:
            i1+=1
        else:
            i2+=1
     return ans
 

t= int(input())
for _ in range(t):
     x, y, z= map(int, input().split())
     l1= [int(x) for x in input().split()]
     l2= [int(x) for x in input().split()]
     l3= [int(x) for x in input().split()]
     tmp= sol(l1, l2)
     ans= sol(tmp, l3)
     if len(ans)==0:
        print('NO')
     else:
        for i in ans:
             print(i, end=' ')
        print() 

"""
3
6 5 8
1 5 10 20 40 80
5 7 20 80 100
3 4 15 20 30 70 80 120
3 5 4
1 5 5
3 4 5 5 10
5 5 10 20
3 3 3
1 2 3
4 5 6
7 8 9
"""

