n =int(input())
li= input().split()
l=[]
for i in li:
    tmp= int(i)
    if(len(l)==0):
        l.append(tmp)
    else:
        x= l[-1]
        if (x+tmp)%2==0:
            l.pop()
        else:
            l.append(tmp)
print(len(l))
