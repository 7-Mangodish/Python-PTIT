n= int(input())
l= [int(x) for x in input().split()]
l.sort()
m1= l[0]*l[1]
m2= l[0]*l[1]*l[2]
m3= l[-1]*l[-2]
m4= l[-1]*l[-2]*l[-3]
m5= l[0]*l[1]*l[-1]
m6= l[-1]*l[-2]*l[0]
ans= max(m1, m2, m3, m4, m5, m6)
print(ans)
"""
6
5 10 -2 3 5 2
"""