s= input()
if len(s)==1:
    print(s)
else:
    while len(s)>1:
        ind = len(s)//2
        n1= int(s[:ind])
        n2= int(s[ind:])
        s= str(n1+n2)
        print(s)