with open('CONTACT.in') as f:
    l= f.readlines()
ans=[]
for i in l:
    i= i.rstrip().lower()
    if i not in ans:
        ans.append(i)
ans.sort()
for i in ans:
    print(i)

    