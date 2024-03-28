t= int(input())
for _ in range(t):
    s=input()
    ans=[]
    sum=0
    for i in s:
        if i.isalpha():
            ans.append(i)
        else:
            sum+= int(i)
    ans.sort()
    for i in ans:
        print(i, end='')
    print(sum)
"""
2
AC2BEW3
ACCBA10D2EW30
"""