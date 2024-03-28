from math import*
from itertools import*
res =[]

if __name__ =='__main__':
    n, k= map(int, input().split())
    l =input().split()

    for i in l:
        if int(i) not in  res:
            res.append(int(i))
    res.sort()

    li =list(combinations(res, k))
    for x in li:
        for i in x:
            print(i, sep= '', end=' ')
        print()

    