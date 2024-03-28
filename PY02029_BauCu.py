
m, n = map(int, input().split())
l= [int(x) for x in input().split()]
# list luu tan suat
ts=[0]*1000
for x in l:
    ts[x]+=1
# list de tim tan suat lon thu 2
val=[]
for x in ts:
    if x!=0 and x not in val:
        val.append(x)
val.sort()
if len(val)==1:
    print('NONE')
else:
    tsOfAns= val[-2]
    ans= ts.index(tsOfAns)
    print(ans)
# print(val)
"""
10 4
2 3 1 2 3 4 1 2 3 2
8 4
1 2 3 4 4 3 2 1
8 4
1 2 2 3 3 4 4 4 
"""