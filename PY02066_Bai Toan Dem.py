
n= int(input())
l= []
while True:
    if len(l) ==n:
        break
    tmp= [int(x) for x in input().split()]
    for i in tmp:
        l. append(i)

cnt=[0] * 500
ok= False
for i in l:
    cnt[i] =1
for i in range(1,max(l)+1):
    if cnt[i]==0:
        print(i)
        if ok== False:
            ok= True
if ok== False:
    print('Excellent!')
"""
7
4 5 7 8 9
10 11
5
1 2 3
4
5
"""