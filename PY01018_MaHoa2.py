p='ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True:
    ip= input()
    if ip=='0':
        break
    k, s= map(str, ip.split())
    k=int(k)
    ans=''
    for i in s:
        if i=='_':
            ans+=p[(26+k)%28 ]
        elif i=='.':
            ans+= p[(27+k)%28]
        else:
            ans+= p[ (ord(i)-65+k)%28 ]
    ans=list(ans)
    ans.reverse()
    for i in ans:
        print(i, end='')
    print()
    
"""
1 ABCD
14 ROAD
0
"""