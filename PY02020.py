from math import*

n= int(input())
l= [float(x) for x in input().split()]
minVal= min(l)
maxVal= max(l)
sum=0.0
cnt=0
for i in l:
    if i != minVal and i != maxVal:
        sum+=i
        cnt+=1
print('%.2f'%(sum/cnt))