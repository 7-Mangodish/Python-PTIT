
def check(a):
    for i in range(len(a)-1):
        tmp1 = [a[i]]
        tmp2 = {a[i]}
        for j in range(len(a)):
            tmp1.append(a[j])
            tmp2.add(a[j])
            if len(tmp1) != len(tmp2):
                return False
    return True
            
t= int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    if check(a):
        print('YES')
    else:
        print('NO')

"""
5
5
1 2 3 4 5
7
1 2 3 4 3 4 1
5
1 1 1 1 1
5
1 2 5 2 1
5
5 5 2 5 5
"""