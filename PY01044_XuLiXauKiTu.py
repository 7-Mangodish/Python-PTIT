"""
Lap trinh huong doi tuong
Ngon ngu lap trinh C++
"""
s1=set({})
s2=set({})
s1= {x.lower() for x in input().split()}
s2= {x.lower() for x in input().split()}
union=s1 | s2
intersection= s1 & s2
union= list(union)
union.sort()
intersection= list(intersection)
intersection.sort()

for i in union:
    print(i, end=" ")
print()
for i in intersection:
    print(i, end=' ')
    