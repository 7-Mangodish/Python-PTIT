s= set({})
cnt=10
while True:
    l =[int(x)%42 for x in input().split()]
    cnt-= len(l)
    tmp_s= set(l)
    s= s|tmp_s
    if cnt==0:
        break
print(len(s))