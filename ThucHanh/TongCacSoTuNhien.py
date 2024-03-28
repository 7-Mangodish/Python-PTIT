from math import*

l=[]

ok= False

def init(n):
    l.append(n)

def sinh():
    ind=len(l)-1
    # Dem so luong chu so 1 tu cuoi len dau
    while ind >=0 and l[ind]==1:
        ind-=1
    if ind<0:
        return False
  
    l[ind]-=1
    k= len(l)-ind
    # bieu dien theo l[ind]
    q= k//l[ind]
    r= k%l[ind]
    for i in range(ind+1, len(l)):
        l.pop()
    for i in range(q):
        l.append(l[ind])
    if r!=0:
        l.append(r)

if __name__=='__main__':
    # t= int(input())
    # while t>0:
        n=int(input())
        init(n)
        ans=[]
        while True:
            print(l)
            tmp= [x for x in l]
            ans.append(tmp)
            if(sinh()==False):
                break
        # print(len(ans))
        # for i in ans:
        #     print('(', sep='',end='')
        #     for j in range(len(i)):
        #         if j==len(i)-1:
        #             print(i[j], end=')')
        #         else:
        #             print(i[j], sep=' ', end='')
        #     print()