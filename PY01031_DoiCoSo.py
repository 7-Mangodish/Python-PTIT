
def sol(l):
    for i in range(len(l)):
        if l[i] >9:
            l[i]-=9
            l[i]= chr(l[i]+64)

def testcase(n,  k):
    ans=[]
    while n!=0:
        ans.append(n%k)
        n//=k
    ans.reverse()
    sol(ans)
    for i in ans:
        print(i, end='')
    print()

t= int(input())
for _ in range(t):
    n, k= map(int, input().split()) 
    testcase(n,k)
