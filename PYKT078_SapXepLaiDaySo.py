import functools as f

if __name__=='__main__':
    t= int(input())
    for _ in range(t):
        n, m= map(int, input().split())
        l= [ int(x) for x in input().split()]
        a=[]
        b=[]
        for i in l:
            if i <0:a.append(i)
            else: b.append(i)
        ind=0
        for i in range(1, len(b)):
            if b[i] > b[ind]:
                ind=i
        for i in a: 
            print(i, end=' ')
        b.insert(ind, m)
        for i in b:
            print(i, end=' ')
        print()
"""
1
5 3
-1 2 3 4 -1
"""