from math import*

Nmax= 10**6+100
p=[0]*Nmax
def Seive():
    p[0]= p[1]=1
    for i in range(2, isqrt(Nmax)+1):
        if p[i]==0:
            ind= i*i
            while ind <Nmax:
                p[ind]=1
                ind+=i

if __name__== '__main__':
    Seive()
    t= int(input())
    for _ in range(t):
        cnt=0
        n= int(input())
        for i in range(n-6):
            if p[i]==0 and p[i+2]==0 and p[i+6]==0:
                # print(i, i+2, i+6)
                cnt+=1
            if p[i]==0 and p[i+4]==0 and p[i+6]==0:
                # print(i, i+4, i+6)
                cnt+=1
        print(cnt)
            # if p[i]==0:
            #     print(i, end=' ')

"""
2
15
25
"""