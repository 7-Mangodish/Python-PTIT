import itertools as iter

t = int(input())
for i in range(t):
    n = int(input())
    l = list(range(1, n+1))
    ans = list(iter.permutations(l))
    ans.reverse()
    print(len(ans))
    for i in ans:
        for j in i:
            print(j, end='')
        print(end=' ')
    print()