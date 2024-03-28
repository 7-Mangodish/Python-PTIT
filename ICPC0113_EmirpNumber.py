from math import*

Nmax= 10**6+5
p= [0]*(10**6+5) 
def Seive():
    p[1]=p[0]=1
    for i in range(2,isqrt(Nmax)+1):
        if p[i]==0:
            j= i*i
            while j<Nmax:
                p[j]= 1
                j+=i

def Check(n):
    n=list(str(n))
    tmp= list(reversed(n))   
    for i in range(len(n)):
        if n[i]!=tmp[i]:
            return True
    return False

if __name__ =='__main__':
    Seive()
    t = int(input())
    for _ in range(t):
        n = int(input())
        ans=[]
        for i in range(2, n):
            rev_i=0
            tmp=i
            while tmp >0:
                rev_i = rev_i*10 + tmp%10
                tmp//=10
            if p[i]==0 and p[rev_i]==0 and rev_i <n and Check(i):
                if i not in ans:
                    ans.append(i)
                    ans.append(rev_i)
        for i in ans:
            print(i, end=' ')
        print()


        
        