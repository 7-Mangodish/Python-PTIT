
while True:
    n= int(input())
    if n==0:
        break
    s=set({})
    for i in range(n):
        m= int(input())
        s.add(m)
    if len(s)==1:
        print('BANG NHAU')
    else:
        print(min(s), max(s))
"""
5
1
2
3
4
5
3
001
22
33333333333333333333333333333333333
3
1
1
1
0
"""
