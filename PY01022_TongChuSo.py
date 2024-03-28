def sol(s):
    sum=0
    for i in s:
        sum+=ord(i) - ord('0')
    # if s[0]=='-':
    #     sum+=1
    return str(sum)

s= input()
ans=0
while len(s) >1:
    s= sol(s)
    ans+=1
print(ans)