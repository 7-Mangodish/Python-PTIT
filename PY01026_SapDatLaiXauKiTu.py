

t=int(input())
for i in range(1, t+1):
    s1= list(input())
    s1.sort()
    s2= list(input())
    s2.sort()
    print('Test ', i, ':',sep='', end=' ')
    if s1==s2:
        print('YES')
    else:
        print('NO')
"""
4
testing
intestg
abc
aabbbcccc
abcabcbcc
aabbbcccc
abc
xyz
"""