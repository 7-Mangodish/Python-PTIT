import functools as f

def cmp(a, b):# a: phan tu dung sau, b: dung truoc
    if a[1] < b[1]:
        return 1
    elif a[1] > b[1]:
        return -1
    else:
        if a[2] > b[2]:
            return 1
        elif a[2] < b[2]:
            return -1
        else:
            return b[0] < a[0]

if __name__ =='__main__':
    t= int(input())
    li=[]
    for _ in range(t):
        s= input()
        ex, cnt= map(int, input().split())
        li.append([s, ex, cnt])
    li.sort(key= f.cmp_to_key(cmp))
    for i in li:
        for j in i:
            print(j, end=" ")
        print()
"""
2
Nguyen Van Nam
168 600
Tran Thi Ngoc
168 600
"""