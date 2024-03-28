t= int(input())
line=[]
for _ in range(t):
    tmp= [x for x in input().split()]
    line.append(len(tmp))
w= 0 
ans=[]
cntLine=0 # Dem so dong cua the tho 7 
for i in line:
    tmp=0
    if i==8 or i ==6:
       tmp=1
    else:
        tmp=2
        cntLine+=1
    if tmp != w or cntLine==4:
        ans.append(tmp)
        cntLine=0
        w=tmp 
print(len(ans))
for _ in ans:
    print(_)
"""
12
Minh ve minh co nho ta
Muoi lam nam ay thiet tha man nong
Minh ve minh co nho khong
Nhin cay nho nui nhin song nho nguon
Mot canh hai canh lai ba canh
Tran troc ban khoan giac chang lanh
Canh bon canh nam vua chop mat
Sao vang nam canh mong hon bay
Mot canh hai canh lai ba canh
Tran troc ban khoan giac chang lanh
Canh bon canh nam vua chop mat
Sao vang nam canh mong hon bay
"""
