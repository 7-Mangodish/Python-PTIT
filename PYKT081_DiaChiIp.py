
def check(l):
    if l!=4: 
        return False
    for i in l:
        if i.isdigit() == False:
            return False
        if int(i) <0 or int(i) >255:
            return False
    return True


t= int(input())
for _ in range(t):
    s= input()
    l=s.split('.')
    if check(l):
        print('YES')
    else:
        print('NO')
    
"""
2
     19a    . # &*^%   1  6 8    .   -  1.    1
256.255.255.255
"""