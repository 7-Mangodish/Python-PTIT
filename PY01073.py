from itertools import*

if __name__ =='__main__':
    l = list(input())
    li = permutations(l)
    for i in li:
        for x in i:
            print(x, sep= '', end= '')
        print()