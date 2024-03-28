from math import*

# Ham comb(n,k): To hop chap k cua n
# Ham perm(n,k): Chinh hop chap k cua n
n= int(input())
l=[]
for i in range(n):
    l.append(list(input()))
# print(l)
# for i in l:
#     print(i)

ans= 0
for i in l:
    cnt= i.count('C')
    ans+= comb(cnt, 2)

for i in range(n):
    cnt=0
    for j in range(n):
        if l[j][i]=='C':
            cnt+=1
    ans+= comb(cnt, 2)
print(ans)

"""
4
CC..
C..C
.CC.
.CC.
"""